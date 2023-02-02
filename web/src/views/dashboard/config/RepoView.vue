<template>
  <div class="repo-view">
    <n-page-header>
      <template #header>
        <n-breadcrumb>
          <n-breadcrumb-item>配置</n-breadcrumb-item>
          <n-breadcrumb-item>存储库</n-breadcrumb-item>
        </n-breadcrumb>
      </template>
    </n-page-header>
    <div class="op-area">
      <n-input v-model:value="repoName" style="width: 200px; margin-right: 10px; " type="text"
               placeholder="请输入名称"/>
      <n-select v-model:value="repoConnectTypeSelectOptionValue" :options="repoConnectTypeSelectOptions"
                style="width: 200px; margin-right: 10px;" placeholder="请选择类型"/>
      <n-input v-model:value="repoUsage" style="margin-right: 10px; " type="text"
               placeholder="请输入用途, 支持全文检索.."/>
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
    <n-data-table striped :columns="columns" :data="repo" :pagination="pagination"/>
    <div style="width: 100%; min-height: 20px;"></div>
  </div>
</template>

<script setup>
import {h, reactive, ref} from "vue";
import {NButton, NTag} from "naive-ui";
import {SearchOutlined, CloseOutlined} from "@vicons/antd"

let repoName = ref("")
let repoConnectTypeSelectOptionValue = ref(null)
let repoConnectTypeSelectOptions = [
  {
    label: "全部",
    value: null
  },
  {
    label: "SSH",
    value: "SSH",
  },
  {
    label: "HTTP/HTPPS",
    value: "HTTP/HTTPS",
  },
]
let repoUsage = ref("")


let repo = ref([{
  "key": "0",
  "name": "Pan9hu/melo-cmdb",
  "connect-type": "SSH",
  "location": "git@github.com:Pan9hu/melo-cmdb.git",
  "create-time": "2023/2/1 12:32:03",
  "usage": "用于测试环境的 Web 集群负载均衡配置。",
}]);

let columns = [{
  type: "selection",
  fixed: "left"
}, {
  title: "名称",
  key: "name",
  fixed: "left",
}, {
  title: "类型",
  key: "connect-type",
  width: 100
}, {
  title: "地址",
  key: "location",
  width: 500
}, {
  title: "添加时间",
  key: "create-time",
  width: 220
}, {
  title: "用途",
  key: "usage",
  resizable: true
},

  {
    title: "操作",
    key: "op",
    render(row) {
      return h(
          NButton, {
            size: "tiny",
            onClick: () => handleDeleteCurrentItemButtonClicked(row),
            secondary: true,
          }, {
            default: () => "删除"
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

function handleDeleteCurrentItemButtonClicked(row) {

}

</script>

<style scoped>
.op-area {
  padding-top: 15px;
  padding-bottom: 15px;
  display: flex;
}

.repo-view {
  display: flex;
  flex-direction: column;
  width: 100%;
  height: 100%;
}
</style>