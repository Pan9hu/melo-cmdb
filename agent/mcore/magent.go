package main

import (
	"encoding/json"
	amqp "github.com/rabbitmq/amqp091-go"
	"io"
	"log"
	"net/http"
	"strings"
)

var (
	mMetricsHealthUrl = "http://127.0.0.1:8080/health"
	MeloAPIServerUrl  = "http://127.0.0.1:8000/api/version"
	AMQPUrl           = "amqp://guest:guest@127.0.0.1:5762"
)

func init() {
	// TODO 加载平台配置
}

func main() {
	log.Println("[Info] Starting mAgent...")

	// 启动mMetrics，然后启动mAgent程序
	log.Println("[Info] check mMetrics health...(HTTP Ping Method)")
	chResponse, err := http.Get(mMetricsHealthUrl)
	if err != nil {
		log.Fatalln("[Error] mMetrics health check failed, because: ", err.Error())
		return
	}
	if chResponse.StatusCode != 200 {
		log.Println("[Warning] mMetrics health check failed, status code: ", chResponse.StatusCode)
	}

	// 健康检查并，获取Melo API Server 版本
	log.Println("[Info] Fetch api-server version...")
	fvResponse, err := http.Get(MeloAPIServerUrl)
	if err != nil {
		log.Fatalln("[Error] Melo API Server health check failed, because:", err.Error())
	}
	if fvResponse.StatusCode != 200 {
		log.Println("[Warning] Melo API Server health check failed, status code:", fvResponse.StatusCode)
	}

	var version map[string]any
	versionBody, err := io.ReadAll(fvResponse.Body)
	if err != nil {
		log.Panicln("[Error] read Melo API Server version endpoint response data failed,because: ", err.Error())
	}
	err = json.Unmarshal(versionBody, &version)
	if err != nil {
		log.Panicln("[Error] Melo API Server version endpoint response data unmarshal failed,because: ", err.Error())
	}
	log.Println("[Success] connect to Melo API Server ok, version =", version["data"].(map[string]any)["version"])

	//链接 RabbitMQ 集群，等待任务执行
	mqConn, err := amqp.Dial(AMQPUrl)
	if err != nil {
		log.Fatalln("[Error] RabbitMQ connection failed, because:", err.Error())
	}
	defer func(mqConn *amqp.Connection) {
		_ = mqConn.Close()
	}(mqConn)

	//创建通道
	channel, err := mqConn.Channel()
	if err != nil {
		log.Panicln("[Error] create amqp connection channel failed, because:", err.Error())
	}

	err = channel.ExchangeDeclare("job", "fanout", true, false, false, false, nil)
	if err != nil {
		log.Panicln("[Error] can not declare exchange, because:", err.Error())
	}

	queue, err := channel.QueueDeclare("m_agent_q", true, false, false, false, nil)
	if err != nil {
		log.Panicln("[Error] can not declare queue, because:", err.Error())
	}
	err = channel.QueueBind(queue.Name, "", "jobs", false, nil)
	if err != nil {
		log.Panicln("[Error] can not bind queue, because:", err.Error())
	}

	for {
		// 获取队列任务消息
		messages, messageErr := channel.Consume(queue.Name, "", true, false, false, false, nil)
		if messageErr != nil {
			log.Panicln("[Error] can not bind queue, because:", messageErr.Error())
		}

		for message := range messages {
			// MSG_TYPE#DATA
			// e.g. OP_SYNC_REPO #https://github.com/xxx/demo.git -> /etc/demo-Application/
			var content map[string]string
			err = json.Unmarshal(message.Body, &content)
			if err != nil {
				log.Panicln("[Error] channel message unmarshal failed,because: ", err.Error())
			}
			jobType := strings.Split(content["task"], "#")[0]

			switch jobType {
			case "OP_SYNC_REPO":
				go func() {
					// 执行同步仓库的任务
					log.Println("[Info] running OP_SYNC_REPO job.")
				}()
			}
		}
	}
}
