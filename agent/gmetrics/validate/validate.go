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

// Handler for /validate content.
// Validates cadvisor dependencies - kernel, os, docker setup.

package validate

import (
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"os"
	"path"
	"strings"

	"github.com/google/cadvisor/container/docker"
	"github.com/google/cadvisor/manager"
	"github.com/google/cadvisor/utils"

	"github.com/opencontainers/runc/libcontainer/cgroups"
)

const (
	ValidatePage  = "/validate/"
	Supported     = "[支持，但是不推荐]"
	Unsupported   = "[不支持]"
	Recommended   = "[支持并推荐]"
	Unknown       = "[未知]"
	VersionFormat = "%d.%d%s"
	OutputFormat  = "%s: %s\n\t%s\n\n"
)

func getMajorMinor(version string) (int, int, error) {
	var major, minor int
	var ign string
	n, err := fmt.Sscanf(version, VersionFormat, &major, &minor, &ign)
	if n != 3 || err != nil {
		log.Printf("为 %s 解析版本信息失败:", version)
		return -1, -1, err
	}
	return major, minor, nil
}

func validateKernelVersion(version string) (string, string) {
	desc := fmt.Sprintf("内核版本是 %s. 版本 >= 2.6 是支持的。 3.0+ 是推荐的。\n", version)
	major, minor, err := getMajorMinor(version)
	if err != nil {
		desc = fmt.Sprintf("无法解析内核版本。 %s", desc)
		return Unknown, desc
	}

	if major < 2 {
		return Unsupported, desc
	}

	if major == 2 && minor < 6 {
		return Unsupported, desc
	}

	if major >= 3 {
		return Recommended, desc
	}

	return Supported, desc
}

func validateDockerVersion(version string) (string, string) {
	desc := fmt.Sprintf("Docker 版本是 %s. 版本 >= 1.0 是支持的。 1.2+ 是推荐的\n", version)
	major, minor, err := getMajorMinor(version)
	if err != nil {
		desc = fmt.Sprintf("无法解析 Docker 版本。 %s\n\t", desc)
		return Unknown, desc
	}
	if major < 1 {
		return Unsupported, desc
	}

	if major == 1 && minor < 2 {
		return Supported, desc
	}

	return Recommended, desc
}

func getEnabledCgroups() (map[string]int, error) {
	out, err := ioutil.ReadFile("/proc/cgroups")
	if err != nil {
		return nil, err
	}
	cgroups := make(map[string]int)
	for i, line := range strings.Split(string(out), "\n") {
		var cgroup string
		var ign, enabled int
		if i == 0 || line == "" {
			continue
		}
		n, err := fmt.Sscanf(line, "%s %d %d %d", &cgroup, &ign, &ign, &enabled)
		if n != 4 || err != nil {
			if err == nil {
				err = fmt.Errorf("解析 /proc/cgroup 入口失败: %s", line)
			}
			return nil, err
		}
		cgroups[cgroup] = enabled
	}
	return cgroups, nil
}

func areCgroupsPresent(available map[string]int, desired []string) (bool, string) {
	for _, cgroup := range desired {
		enabled, ok := available[cgroup]
		if !ok {
			reason := fmt.Sprintf("缺少 cgroup %s. 可用的 cgroup: %v\n", cgroup, available)
			return false, reason
		}
		if enabled != 1 {
			reason := fmt.Sprintf("没有启用 Cgroup %s。 可用的 cgroup: %v\n", cgroup, available)
			return false, reason
		}
	}
	return true, ""
}

func validateCPUCFSBandwidth(availableCgroups map[string]int) string {
	ok, _ := areCgroupsPresent(availableCgroups, []string{"cpu"})
	if !ok {
		return "\tCpu cfs bandwidth status unknown: cpu cgroup not enabled.\n"
	}
	mnt, err := cgroups.FindCgroupMountpoint("/", "cpu")
	if err != nil {
		return "\tCpu cfs bandwidth status unknown: cpu cgroup not mounted.\n"
	}
	_, err = os.Stat(path.Join(mnt, "cpu.cfs_period_us"))
	if os.IsNotExist(err) {
		return "\tCpu cfs bandwidth is disabled. Recompile kernel with \"CONFIG_CFS_BANDWIDTH\" enabled.\n"
	}

	return "\tCpu cfs bandwidth is enabled.\n"
}

func validateMemoryAccounting(availableCgroups map[string]int) string {
	ok, _ := areCgroupsPresent(availableCgroups, []string{"memory"})
	if !ok {
		return "\tHierarchical memory accounting status unknown: memory cgroup not enabled.\n"
	}
	var enabled int
	if cgroups.IsCgroup2UnifiedMode() {
		enabled = 1
	} else {
		mnt, err := cgroups.FindCgroupMountpoint("/", "memory")
		if err != nil {
			return "\tHierarchical memory accounting status unknown: memory cgroup not mounted.\n"
		}
		hier, err := ioutil.ReadFile(path.Join(mnt, "memory.use_hierarchy"))
		if err != nil {
			return "\tHierarchical memory accounting status unknown: hierarchy interface unavailable.\n"
		}
		n, err := fmt.Sscanf(string(hier), "%d", &enabled)
		if err != nil || n != 1 {
			return "\tHierarchical memory accounting status unknown: hierarchy interface unreadable.\n"
		}
	}
	if enabled == 1 {
		return "\tHierarchical memory accounting enabled. Reported memory usage includes memory used by child containers.\n"
	}
	return "\tHierarchical memory accounting disabled. Memory usage does not include usage from child containers.\n"

}

func validateCgroups() (string, string) {
	requiredCgroups := []string{"cpu", "cpuacct"}
	recommendedCgroups := []string{"memory", "blkio", "cpuset", "devices", "freezer"}
	availableCgroups, err := getEnabledCgroups()
	desc := fmt.Sprintf("\tFollowing cgroups are required: %v\n\tFollowing other cgroups are recommended: %v\n", requiredCgroups, recommendedCgroups)
	if err != nil {
		desc = fmt.Sprintf("Could not parse /proc/cgroups.\n%s", desc)
		return Unknown, desc
	}
	ok, out := areCgroupsPresent(availableCgroups, requiredCgroups)
	if !ok {
		out += desc
		return Unsupported, out
	}
	ok, out = areCgroupsPresent(availableCgroups, recommendedCgroups)
	if !ok {
		// supported, but not recommended.
		out += desc
		return Supported, out
	}
	out = fmt.Sprintf("Available cgroups: %v\n", availableCgroups)
	out += desc
	out += validateMemoryAccounting(availableCgroups)
	out += validateCPUCFSBandwidth(availableCgroups)
	return Recommended, out
}

func validateDockerInfo() (string, string) {
	info, err := docker.ValidateInfo()
	if err != nil {
		return Unsupported, fmt.Sprintf("Docker setup is invalid: %v", err)
	}

	desc := fmt.Sprintf("Storage driver is %s.\n", info.Driver)
	return Recommended, desc
}

func validateCgroupMounts() (string, string) {
	const recommendedMount = "/sys/fs/cgroup"
	desc := fmt.Sprintf("\tAny cgroup mount point that is detectible and accessible is supported. %s is recommended as a standard location.\n", recommendedMount)
	mnt, err := cgroups.FindCgroupMountpoint("/", "cpu")
	if err != nil {
		out := "Could not locate cgroup mount point.\n"
		out += desc
		return Unknown, out
	}
	mnt = path.Dir(mnt)
	if !utils.FileExists(mnt) {
		out := fmt.Sprintf("Cgroup mount directory %s inaccessible.\n", mnt)
		out += desc
		return Unsupported, out
	}
	mounts, err := ioutil.ReadDir(mnt)
	if err != nil {
		out := fmt.Sprintf("Could not read cgroup mount directory %s.\n", mnt)
		out += desc
		return Unsupported, out
	}
	mountNames := "\tCgroup mount directories: "
	for _, mount := range mounts {
		mountNames += mount.Name() + " "
	}
	mountNames += "\n"
	out := fmt.Sprintf("Cgroups are mounted at %s.\n", mnt)
	out += mountNames
	out += desc
	info, err := ioutil.ReadFile("/proc/mounts")
	if err != nil {
		out := "Could not read /proc/mounts.\n"
		out += desc
		return Unsupported, out
	}
	out += "\tCgroup mounts:\n"
	for _, line := range strings.Split(string(info), "\n") {
		if strings.Contains(line, " cgroup ") {
			out += "\t" + line + "\n"
		}
	}
	if mnt == recommendedMount {
		return Recommended, out
	}
	return Supported, out
}

func validateIoScheduler(containerManager manager.Manager) (string, string) {
	var desc string
	mi, err := containerManager.GetMachineInfo()
	if err != nil {
		return Unknown, "Machine info not available\n\t"
	}
	cfq := false
	for _, disk := range mi.DiskMap {
		desc += fmt.Sprintf("\t Disk %q Scheduler type %q.\n", disk.Name, disk.Scheduler)
		if disk.Scheduler == "cfq" {
			cfq = true
		}
	}
	// Since we get lot of random block devices, report recommended if
	// at least one of them is on cfq. Report Supported otherwise.
	if cfq {
		desc = "At least one device supports 'cfq' I/O scheduler. Some disk stats can be reported.\n" + desc
		return Recommended, desc
	}
	desc = "None of the devices support 'cfq' I/O scheduler. No disk stats can be reported.\n" + desc
	return Supported, desc
}

func HandleRequest(w http.ResponseWriter, containerManager manager.Manager) error {
	// Get cAdvisor version Info.
	versionInfo, err := containerManager.GetVersionInfo()
	if err != nil {
		return err
	}

	out := fmt.Sprintf("cAdvisor 版本: %s\n\n", versionInfo.CadvisorVersion)

	// No OS is preferred or unsupported as of now.
	out += fmt.Sprintf("操作系统版本: %s\n\n", versionInfo.ContainerOsVersion)

	kernelValidation, desc := validateKernelVersion(versionInfo.KernelVersion)
	out += fmt.Sprintf(OutputFormat, "内核版本", kernelValidation, desc)

	cgroupValidation, desc := validateCgroups()
	out += fmt.Sprintf(OutputFormat, "Cgroup 选项", cgroupValidation, desc)

	mountsValidation, desc := validateCgroupMounts()
	out += fmt.Sprintf(OutputFormat, "Cgroup 挂载选项", mountsValidation, desc)

	dockerValidation, desc := validateDockerVersion(versionInfo.DockerVersion)
	out += fmt.Sprintf(OutputFormat, "Docker 版本", dockerValidation, desc)

	dockerInfoValidation, desc := validateDockerInfo()
	out += fmt.Sprintf(OutputFormat, "Docker 驱动选项", dockerInfoValidation, desc)

	ioSchedulerValidation, desc := validateIoScheduler(containerManager)
	out += fmt.Sprintf(OutputFormat, "块设备选项", ioSchedulerValidation, desc)

	// Output debug info.
	debugInfo := containerManager.DebugInfo()
	for category, lines := range debugInfo {
		out += fmt.Sprintf(OutputFormat, category, "", strings.Join(lines, "\n\t"))
	}

	_, err = w.Write([]byte(out))
	return err
}
