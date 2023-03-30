<template>
  <div class="machine-view">
    <n-page-header>
      <template #header>
        <n-breadcrumb>
          <n-breadcrumb-item>业务概念</n-breadcrumb-item>
          <n-breadcrumb-item>机器</n-breadcrumb-item>
        </n-breadcrumb>
      </template>
    </n-page-header>
    <div class="op-area">
      <n-input style="width: 700px; margin-right: 10px;" v-model:value="machineID" type="text"
               placeholder="按照 ID 搜索, 与其他条件互斥" />
      <n-select v-model:value="machineTypeSearchOptionValue" :options="machineTypeSearchOptions"
                placeholder="选择机器类型" style="width: 420px; margin-right: 10px;"/>
      <n-select v-model:value="machineStatusSearchOptionValue" :options="machineStatusSearchOptions"
                placeholder="选择机器状态" style="width: 420px; margin-right: 10px;"/>
      <n-input style="margin-right: 10px;" size=small v-model:value="group" type="text"
               placeholder="按照群组搜索, 支持全文搜索.."/>
      <n-input style="width: 800px; margin-right: 10px;" size=small v-model:value="resPool" type="text"
               placeholder="按照资源池搜索, 支持全文搜索.." />
      <n-tooltip placement="top" trigger="hover">
        <template #trigger>
          <n-button secondary tertiary circle style="margin-left: 5px" type="info">
            <template #icon>
              <n-icon>
                <search-outlined/>
              </n-icon>
            </template>
          </n-button>
        </template>
        <span>按照指定条件进行搜索</span>
      </n-tooltip>
      <n-tooltip placement="top" trigger="hover">
        <template #trigger>
          <n-button secondary tertiary circle style="margin-left: 5px" type="error">
            <template #icon>
              <n-icon>
                <close-outlined/>
              </n-icon>
            </template>
          </n-button>
        </template>
        <span>清空搜索条件</span>
      </n-tooltip>
    </div>
    <n-data-table striped :columns="columns" :data="machines" :pagination="pagination"/>
    <div style="width: 100%; min-height: 20px;"></div>
  </div>
</template>

<script setup>
import {h, reactive, ref} from "vue";
import {NButton, NTag} from "naive-ui";
import {SearchOutlined, CloseOutlined} from "@vicons/antd"

let machineTypeSearchOptionValue = ref(null);
let machineID = ref("")
let group = ref("")
let resPool = ref("")

let machineTypeSearchOptions = [
  {
    label: "全部",
    value: null

  }, {
    label: "物理机",
    value: "物理机"
  }, {
    label: "虚拟机",
    value: "虚拟机"
  }, {
    label: "容器",
    value: "容器"
  },
];

let machineStatusSearchOptionValue = ref(null);

let machineStatusSearchOptions = [
  {
    label: "全部",
    value: null

  }, {
    label: "已关闭",
    value: "已关闭"
  }, {
    label: "正在运行",
    value: "正在运行"
  }, {
    label: "已挂起",
    value: "已挂起"
  }, {
    label: "正在挂起",
    value: "正在挂起"
  }, {
    label: "正在关闭",
    value: "正在关闭"
  }, {
    label: "就绪中",
    value: "就绪中"
  },
]

function handleMachineItemPowerClicked(row) {

}


let machines = ref([
  {
    "key": "1",
    "id": "57d7e24a-189d-4a60-9948-94eb18f17b69",
    "type": "物理机",
    "status": "正在运行",
    "group": "/minecraft/全球",
    "safe-group": ["Web 服务", "数据库服务", "登录网关", "运维"],
    "res-pool": "北京东三区",
    "create_time": "2023/02/15 00:12:09",
    "update_time": "2023/02/15 00:12:15"
  },
  {
    "key": "2",
    "id": "2fc24717-48bd-4b8f-aed0-eea712562e66",
    "type": "物理机",
    "status": "正在运行",
    "group": "/minecraft/全球",
    "safe-group": ["Web 服务", "数据库服务", "登录网关", "运维"],
    "res-pool": "北京西一区",
    "create_time": "2023/02/15 00:12:09",
    "update_time": "2023/02/15 00:12:15"
  },
  {
    "key": "3",
    "id": "d38a9f14-37b6-4cd9-9440-3eb82fddd8f1",
    "type": "物理机",
    "status": "正在运行",
    "group": "/minecraft/全球",
    "safe-group": ["Web 服务", "数据库服务", "登录网关", "运维"],
    "res-pool": "北京东一区",
    "create_time": "2023/02/15 00:12:09",
    "update_time": "2023/02/15 00:12:15"
  },
  {
    "key": "4",
    "id": "8caaf420-8655-4361-9b31-9be42eb7a20a",
    "type": "物理机",
    "status": "正在运行",
    "group": "/minecraft/全球",
    "safe-group": ["Web 服务", "数据库服务", "登录网关", "运维"],
    "res-pool": "北京东二区",
    "create_time": "2023/02/15 00:12:09",
    "update_time": "2023/02/15 00:12:15"
  },
  {
    "key": "5",
    "id": "fecdb3dc-2568-4d14-a249-51991d0db49a",
    "type": "物理机",
    "status": "正在运行",
    "group": "/minecraft/全球",
    "safe-group": ["Web 服务", "数据库服务", "登录网关", "运维"],
    "res-pool": "北京西三区",
    "create_time": "2023/02/15 00:12:09",
    "update_time": "2023/02/15 00:12:15"
  },
  {
    "key": "6",
    "id": "2d6e28fc-64c1-4af3-931f-115ba0678677",
    "type": "物理机",
    "status": "正在运行",
    "group": "/minecraft/全球",
    "safe-group": ["Web 服务", "数据库服务", "登录网关", "运维"],
    "res-pool": "北京西二区",
    "create_time": "2023/02/15 00:12:09",
    "update_time": "2023/02/15 00:12:15"
  }, {
    "key": "7",
    "id": "cd37ddc9-761f-4671-bfe4-45cc6a88bc7f",
    "type": "物理机",
    "status": "正在运行",
    "group": "/minecraft/全球",
    "safe-group": ["Web 服务", "数据库服务", "登录网关", "运维"],
    "res-pool": "北京北二区",
    "create_time": "2023/02/15 00:12:09",
    "update_time": "2023/02/15 00:12:15"
  },
  {
    "key": "8",
    "id": "b80943b7-0bf1-423b-8672-739c7eaedd15",
    "type": "物理机",
    "status": "正在运行",
    "group": "/minecraft/全球",
    "safe-group": ["Web 服务", "数据库服务", "登录网关", "运维"],
    "res-pool": "北京南一区",
    "create_time": "2023/02/15 00:12:09",
    "update_time": "2023/02/15 00:12:15"
  }, {
    "key": "9",
    "id": "3288ad07-ddf1-41d1-8c6d-df040945e450",
    "type": "物理机",
    "status": "正在运行",
    "group": "/minecraft/全球",
    "safe-group": ["Web 服务", "数据库服务", "登录网关", "运维"],
    "res-pool": "北京北三区",
    "create_time": "2023/02/15 00:12:09",
    "update_time": "2023/02/15 00:12:15"
  }
]);
const columns = [
  {
    title: "ID",
    key: "id",
    width: 320,
    fixed: "left"
  },
  {
    title: "类型",
    key: "type",
    width: 80,
    fixed: "left"
  },
  {
    title: "群组",
    key: "group",
    width: 150,
    fixed: "left"
  },
  {
    title: "资源池",
    key: "res-pool",
    width: 150,
    fixed: "left"
  },
  {
    title: "安全组",
    key: "safe-group",
    resizable: true,
    render(row) {
      return row["safe-group"].map((tagKey) => {
        return h(
            NTag,
            {
              style: {
                marginRight: "6px",
                marginTop: "2px",

              },
              size: "small",
              bordered: false
            }, {
              default: () => tagKey
            }
        );
      });
    }
  },
  {
    title: "受控时间",
    key: "create_time",
    width: 220
  }, {
    title: "数据上报时间",
    key: "update_time",
    width: 220
  },

  {
    title: "状态",
    key: "status",
    width: 100
  },
  {
    title: "操作",
    key: "op",
    render(row) {
      return h(
          NButton, {
            size: "tiny",
            onClick: () => handleMachineItemPowerClicked(row),
            secondary: true,
          }, {
            default: () => "电源"
          }
      );
    },
    fixed: "right",
    width: 150
  },
];

const pagination = reactive({
  page: 5,
  pageSize: 100,
  showSizePicker: true,
  pageSizes: [10, 50, 100],
  onChange: (page) => {
    pagination.page = page;
  },
  onUpdatePageSize: (pageSize) => {
    pagination.pageSize = pageSize;
    pagination.page = 1;
  }
})

</script>

<style scoped>
.op-area {
  padding-top: 15px;
  padding-bottom: 15px;
  display: flex;
}

.machine-view {
  display: flex;
  flex-direction: column;
  width: 100%;
  height: 100%;
}
</style>
