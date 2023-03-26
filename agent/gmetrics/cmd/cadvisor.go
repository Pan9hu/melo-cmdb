// Copyright 2014 Google Inc. All Rights Reserved.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

package main

import (
	"crypto/tls"
	"flag"
	"fmt"
	"net/http"
	"net/http/pprof"
	"os"
	"os/signal"
	"runtime"
	"strings"
	"syscall"

	cadvisorhttp "github.com/google/cadvisor/cmd/internal/http"
	"github.com/google/cadvisor/container"
	"github.com/google/cadvisor/manager"
	"github.com/google/cadvisor/metrics"
	"github.com/google/cadvisor/utils/sysfs"
	"github.com/google/cadvisor/version"

	// Register container providers
	_ "github.com/google/cadvisor/cmd/internal/container/install"

	// Register CloudProviders
	_ "github.com/google/cadvisor/utils/cloudinfo/aws"
	_ "github.com/google/cadvisor/utils/cloudinfo/azure"
	_ "github.com/google/cadvisor/utils/cloudinfo/gce"

	"k8s.io/klog/v2"
)

var argIP = flag.String("listen_ip", "", "要侦听的IP，默认为所有IP。")
var argPort = flag.Int("port", 8080, "要侦听的端口。")
var maxProcs = flag.Int("max_procs", 0, "可以同时使用的CPU的最大数量。默认情况下小于1（核心数量）。")

var versionFlag = flag.Bool("version", false, "打印cAdvisor版本并退出。")

var httpAuthFile = flag.String("http_auth_file", "", "Web UI的HTTP身份验证文件。")
var httpAuthRealm = flag.String("http_auth_realm", "localhost", "Web UI的HTTP身份验证领域。")
var httpDigestFile = flag.String("http_digest_file", "", "Web UI的HTTP摘要文件。")
var httpDigestRealm = flag.String("http_digest_realm", "localhost", "Web UI的HTTP摘要文件。")

var prometheusEndpoint = flag.String("prometheus_endpoint", "/metrics", "在上公开Prometheus度量的端点。")

var enableProfiling = flag.Bool("profiling", false, "通过web接口主机启用分析：port/debug/prof/")

var collectorCert = flag.String("collector_cert", "", "收集器的证书，公开给端点以进行基于证书的身份验证。")
var collectorKey = flag.String("collector_key", "", "收集器证书的密钥。")

var storeContainerLabels = flag.Bool("store_container_labels", true, "将容器标签和环境变量转换为每个容器的prometheus度量上的标签。如果flag设置为false，那么只有导出的度量是容器名称、第一个别名和镜像名称。")
var whitelistedContainerLabels = flag.String("whitelisted_container_labels", "", "要转换为每个容器的prometheus度量上的标签的容器标签的逗号分隔列表。store_container_labels必须设置为false才能生效。")

var envMetadataWhiteList = flag.String("env_metadata_whitelist", "", "与指定前缀匹配的环境变量键的逗号分隔列表，需要为容器收集，目前仅支持containerd和docker运行时。")

var urlBasePrefix = flag.String("url_base_prefix", "", "前缀路径，将在所有路径前加前缀，以支持某些反向代理。")

var rawCgroupPrefixWhiteList = flag.String("raw_cgroup_prefix_whitelist", "", "逗号分隔的cgroup路径前缀列表，即使指定了-docker_only，也需要收集该前缀。")

var perfEvents = flag.String("perf_events_config", "", "JSON文件的路径，该文件包含要测量的性能事件的配置。空值已禁用性能事件测量。")

var resctrlInterval = flag.Duration("resctrl_interval", 0, "重新控制mon组更新间隔。零值禁用更新mon组。")

var (
	// Metrics to be ignored.
	// Tcp metrics are ignored by default.
	ignoreMetrics = container.MetricSet{
		container.MemoryNumaMetrics:              struct{}{},
		container.NetworkTcpUsageMetrics:         struct{}{},
		container.NetworkUdpUsageMetrics:         struct{}{},
		container.NetworkAdvancedTcpUsageMetrics: struct{}{},
		container.ProcessSchedulerMetrics:        struct{}{},
		container.ProcessMetrics:                 struct{}{},
		container.HugetlbUsageMetrics:            struct{}{},
		container.ReferencedMemoryMetrics:        struct{}{},
		container.CPUTopologyMetrics:             struct{}{},
		container.ResctrlMetrics:                 struct{}{},
		container.CPUSetMetrics:                  struct{}{},
	}

	// Metrics to be enabled.  Used only if non-empty.
	enableMetrics = container.MetricSet{}
)

func init() {
	optstr := container.AllMetrics.String()
	flag.Var(&ignoreMetrics, "disable_metrics", fmt.Sprintf("要禁用的以逗号分隔的Metric列表。选项为 %s。", optstr))
	flag.Var(&enableMetrics, "enable_metrics", fmt.Sprintf("要启用的以逗号分隔的Metric列表。如果已设置，则覆盖“disable_metrics”。选项为 %s。", optstr))

	// Default logging verbosity to V(2)
	_ = flag.Set("v", "2")
}

func main() {
	klog.InitFlags(nil)
	defer klog.Flush()
	flag.Parse()

	if *versionFlag {
		fmt.Printf("cAdvisor版本 %s (%s)\n", version.Info["version"], version.Info["revision"])
		os.Exit(0)
	}

	var includedMetrics container.MetricSet
	if len(enableMetrics) > 0 {
		includedMetrics = enableMetrics
	} else {
		includedMetrics = container.AllMetrics.Difference(ignoreMetrics)
	}
	klog.V(1).Infof("开启的Metric: %s", includedMetrics.String())
	setMaxProcs()

	memoryStorage, err := NewMemoryStorage()
	if err != nil {
		klog.Fatalf("无法初始化存储驱动: %s", err)
	}

	sysFs := sysfs.NewRealSysFs()

	collectorHTTPClient := createCollectorHTTPClient(*collectorCert, *collectorKey)

	resourceManager, err := manager.New(memoryStorage, sysFs, manager.HousekeepingConfigFlags, includedMetrics, &collectorHTTPClient, strings.Split(*rawCgroupPrefixWhiteList, ","), strings.Split(*envMetadataWhiteList, ","), *perfEvents, *resctrlInterval)
	if err != nil {
		klog.Fatalf("无法创建管理器: %s", err)
	}

	mux := http.NewServeMux()

	if *enableProfiling {
		mux.HandleFunc("/debug/pprof/", pprof.Index)
		mux.HandleFunc("/debug/pprof/cmdline", pprof.Cmdline)
		mux.HandleFunc("/debug/pprof/profile", pprof.Profile)
		mux.HandleFunc("/debug/pprof/symbol", pprof.Symbol)
	}

	// Register all HTTP handlers.
	err = cadvisorhttp.RegisterHandlers(mux, resourceManager, *httpAuthFile, *httpAuthRealm, *httpDigestFile, *httpDigestRealm, *urlBasePrefix)
	if err != nil {
		klog.Fatalf("无法注册HTTP处理器: %v", err)
	}

	containerLabelFunc := metrics.DefaultContainerLabels
	if !*storeContainerLabels {
		whitelistedLabels := strings.Split(*whitelistedContainerLabels, ",")
		containerLabelFunc = metrics.BaseContainerLabels(whitelistedLabels)
	}

	// Register Prometheus collector to gather information about containers, Go runtime, processes, and machine
	cadvisorhttp.RegisterPrometheusHandler(mux, resourceManager, *prometheusEndpoint, containerLabelFunc, includedMetrics)

	// Start the manager.
	if err := resourceManager.Start(); err != nil {
		klog.Fatalf("无法启动管理器 %v", err)
	}

	// Install signal handler.
	installSignalHandler(resourceManager)

	klog.V(1).Infof("启动的cAdvisor版本: %s-%s 在端口 %d", version.Info["version"], version.Info["revision"], *argPort)

	rootMux := http.NewServeMux()
	rootMux.Handle(*urlBasePrefix+"/", http.StripPrefix(*urlBasePrefix, mux))

	addr := fmt.Sprintf("%s:%d", *argIP, *argPort)
	klog.Fatal(http.ListenAndServe(addr, rootMux))
}

func setMaxProcs() {
	// TODO(vmarmol): 如果我们有一个有效的CPU掩码，请考虑限制。
	// 除非用户指定了一个值，否则允许使用与核心数量一样多的线程。
	var numProcs int
	if *maxProcs < 1 {
		numProcs = runtime.NumCPU()
	} else {
		numProcs = *maxProcs
	}
	runtime.GOMAXPROCS(numProcs)

	// 检查设置是否成功。
	actualNumProcs := runtime.GOMAXPROCS(0)
	if actualNumProcs != numProcs {
		klog.Warningf("指定了 %v 的最大进程，但使用了 %v ", numProcs, actualNumProcs)
	}
}

func installSignalHandler(containerManager manager.Manager) {
	c := make(chan os.Signal, 1)
	signal.Notify(c, os.Interrupt, syscall.SIGTERM)

	// Block until a signal is received.
	go func() {
		sig := <-c
		if err := containerManager.Stop(); err != nil {
			klog.Errorf("无法停止容器管理器: %v", err)
		}
		klog.Infof("根据指定的信号退出: %v", sig)
		os.Exit(0)
	}()
}

func createCollectorHTTPClient(collectorCert, collectorKey string) http.Client {
	//Enable accessing insecure endpoints. We should be able to access metrics from any endpoint
	tlsConfig := &tls.Config{
		InsecureSkipVerify: true,
	}

	if collectorCert != "" {
		if collectorKey == "" {
			klog.Fatal("如果设置了collector_cert值，则必须指定collector_key值。")
		}
		cert, err := tls.LoadX509KeyPair(collectorCert, collectorKey)
		if err != nil {
			klog.Fatalf("无法使用收集器证书和密钥: %s", err)
		}

		tlsConfig.Certificates = []tls.Certificate{cert}
		tlsConfig.BuildNameToCertificate() //nolint: staticcheck
	}

	transport := &http.Transport{
		TLSClientConfig: tlsConfig,
	}

	return http.Client{Transport: transport}
}
