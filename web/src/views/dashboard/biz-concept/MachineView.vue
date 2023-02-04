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
      <n-input type="text" size="small" placeholder="按照 ID 搜索, 与其他条件互斥"
               style="width: 250px; margin-right: 5px"/>
      <n-input type="text" size="small" placeholder="按照群组搜索, 支持全文搜索"
               style="width: 250px; margin-right: 5px"/>
      <n-input type="text" size="small" placeholder="按照资源池搜索, 支持全文搜索"
               style="width: 250px; margin-right: 5px"/>
      <n-select v-model:value="machineTypeSearchOptionValue" size="medium" :options="machineTypeSearchOptions"
                placeholder="选择机器类型" style="width: 150px; margin-right: 5px;"/>
      <n-select v-model:value="machineStatusSearchOptionValue" size="medium" :options="machineStatusSearchOptions"
                placeholder="选择机器状态" style="width: 150px; margin-right: 5px;"/>
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
    <div style="width: 100%; min-height: 20px;">&nbsp</div>
  </div>
</template>

<script setup>
import {h, reactive, ref} from "vue";
import {NButton, NTag} from "naive-ui";
import {SearchOutlined, CloseOutlined} from "@vicons/antd"

let machineTypeSearchOptionValue = ref(null);

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

let machines = ref([
  {
    "key": "1",
    "id": "57d7e24a-189d-4a60-9948-94eb18f17b69",
    "type": "物理机",
    "status": "正在运行",
    "group": "/minecraft/全球",
    "safe-group": ["Web 服务", "数据库服务", "登录网关", "运维"],
    "res-pool": "北京东三区",
    "create-time": "2023/02/15 00:12:09",
    "update-time": "2023/02/15 00:12:15"
  },
  {
    "key": "2",
    "id": "57d7e24a-189d-4a60-9948-94eb18f17b69",
    "type": "物理机",
    "status": "正在运行",
    "group": "/minecraft/全球",
    "safe-group": ["Web 服务", "数据库服务", "登录网关", "运维"],
    "res-pool": "北京东三区",
    "create-time": "2023/02/15 00:12:09",
    "update-time": "2023/02/15 00:12:15"
  },
  {
    "key": "3",
    "id": "57d7e24a-189d-4a60-9948-94eb18f17b69",
    "type": "物理机",
    "status": "正在运行",
    "group": "/minecraft/全球",
    "safe-group": ["Web 服务", "数据库服务", "登录网关", "运维"],
    "res-pool": "北京东三区",
    "create-time": "2023/02/15 00:12:09",
    "update-time": "2023/02/15 00:12:15"
  },
  {
    "key": "4",
    "id": "57d7e24a-189d-4a60-9948-94eb18f17b69",
    "type": "物理机",
    "status": "正在运行",
    "group": "/minecraft/全球",
    "safe-group": ["Web 服务", "数据库服务", "登录网关", "运维"],
    "res-pool": "北京东三区",
    "create-time": "2023/02/15 00:12:09",
    "update-time": "2023/02/15 00:12:15"
  },
  {
    "key": "5",
    "id": "57d7e24a-189d-4a60-9948-94eb18f17b69",
    "type": "物理机",
    "status": "正在运行",
    "group": "/minecraft/全球",
    "safe-group": ["Web 服务", "数据库服务", "登录网关", "运维"],
    "res-pool": "北京东三区",
    "create-time": "2023/02/15 00:12:09",
    "update-time": "2023/02/15 00:12:15"
  },
  {
    "key": "6",
    "id": "57d7e24a-189d-4a60-9948-94eb18f17b69",
    "type": "物理机",
    "status": "正在运行",
    "group": "/minecraft/全球",
    "safe-group": ["Web 服务", "数据库服务", "登录网关", "运维"],
    "res-pool": "北京东三区",
    "create-time": "2023/02/15 00:12:09",
    "update-time": "2023/02/15 00:12:15"
  }, {
    "key": "7",
    "id": "57d7e24a-189d-4a60-9948-94eb18f17b69",
    "type": "物理机",
    "status": "正在运行",
    "group": "/minecraft/全球",
    "safe-group": ["Web 服务", "数据库服务", "登录网关", "运维"],
    "res-pool": "北京东三区",
    "create-time": "2023/02/15 00:12:09",
    "update-time": "2023/02/15 00:12:15"
  },
  {
    "key": "8",
    "id": "57d7e24a-189d-4a60-9948-94eb18f17b69",
    "type": "物理机",
    "status": "正在运行",
    "group": "/minecraft/全球",
    "safe-group": ["Web 服务", "数据库服务", "登录网关", "运维"],
    "res-pool": "北京东三区",
    "create-time": "2023/02/15 00:12:09",
    "update-time": "2023/02/15 00:12:15"
  }, {
    "key": "9",
    "id": "57d7e24a-189d-4a60-9948-94eb18f17b69",
    "type": "物理机",
    "status": "正在运行",
    "group": "/minecraft/全球",
    "safe-group": ["Web 服务", "数据库服务", "登录网关", "运维"],
    "res-pool": "北京东三区",
    "create-time": "2023/02/15 00:12:09",
    "update-time": "2023/02/15 00:12:15"
  }, {
    "key": "10",
    "id": "57d7e24a-189d-4a60-9948-94eb18f17b69",
    "type": "物理机",
    "status": "正在运行",
    "group": "/minecraft/全球",
    "safe-group": ["Web 服务", "数据库服务", "登录网关", "运维"],
    "res-pool": "北京东三区",
    "create-time": "2023/02/15 00:12:09",
    "update-time": "2023/02/15 00:12:15"
  }, {
    "key": "11",
    "id": "57d7e24a-189d-4a60-9948-94eb18f17b69",
    "type": "物理机",
    "status": "正在运行",
    "group": "/minecraft/全球",
    "safe-group": ["Web 服务", "数据库服务", "登录网关", "运维"],
    "res-pool": "北京东三区",
    "create-time": "2023/02/15 00:12:09",
    "update-time": "2023/02/15 00:12:15"
  }
])
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
    key: "create-time",
    width: 220
  }, {
    title: "数据上报时间",
    key: "update-time",
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
