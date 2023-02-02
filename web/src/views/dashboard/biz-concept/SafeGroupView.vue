<template>
  <div class="safe-group-view">
    <n-page-header>
      <template #header>
        <n-breadcrumb>
          <n-breadcrumb-item>业务概念</n-breadcrumb-item>
          <n-breadcrumb-item>安全组</n-breadcrumb-item>
        </n-breadcrumb>
      </template>
    </n-page-header>
    <div class="op-area">
      <n-input style="width: 300px; margin-right: 10px;" v-model:value="safeGroupName" type="text"
               placeholder="请输入名称"/>
      <n-input  v-model:value="safeGroupBizDemand" type="text"
               placeholder="请输入业务需求, 支持全文检索.."/>
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
    <n-data-table striped :columns="columns" :data="safeGroups" :pagination="pagination"/>
    <div style="width: 100%; min-height: 20px;"> </div>
  </div>
</template>

<script setup>
import {h, reactive, ref} from "vue";
import {NButton, NTag} from "naive-ui";
import {SearchOutlined,CloseOutlined} from "@vicons/antd"

let safeGroupName = ref("")
let safeGroupBizDemand = ref("")


let safeGroups = ref([{
  "key": "0",
  "name": "常规",
  "role": ["IN:TCP:80", "IN:TCP:443","ALL:TCP:22","ALL:TCP:3389"],
  "create-time": "2023/02/15 00:12:09",
  "usage": "常规的静态 Web 服务和远程管理端口"
}]);
let columns = [{
  type: "selection",
  fixed:"left"
},{
  title:"名称",
  key: "name",
  fixed:"left",
  width: 250
},{
  title: "放行端口",
  key: "ports",
  resizable: true,
  render(row) {
    return row["role"].map((tagKey) => {
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
    title:"创建时间",
    key: "create-time",
    width: 200

  },{
    title:"业务需求",
    key: "usage",
    resizable: true,
  },{
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
  },];

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
.safe-group-view{
  display: flex;
  flex-direction: column;
  width: 100%;
  height: 100%;
}
</style>