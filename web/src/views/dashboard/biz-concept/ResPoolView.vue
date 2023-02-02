<template>
  <div class="res-pool-view">
    <n-page-header>
      <template #header>
        <n-breadcrumb>
          <n-breadcrumb-item>业务概念</n-breadcrumb-item>
          <n-breadcrumb-item>资源池</n-breadcrumb-item>
        </n-breadcrumb>
      </template>
    </n-page-header>
    <div class="op-area">
      <n-input style="width: 300px; margin-right: 10px;" v-model:value="resPoolName" type="text"
               placeholder="请输入名称"/>
      <n-input  v-model:value="resPoolBizDemand" type="text"
               placeholder="请输入名称"/>
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
    <n-data-table striped :columns="columns" :data="resPools" :pagination="pagination"/>
    <div style="width: 100%; min-height: 20px;"> </div>
  </div>
</template>

<script setup>
import {h, reactive, ref} from "vue";
import {NButton, NTag} from "naive-ui";
import {SearchOutlined,CloseOutlined} from "@vicons/antd"

let resPoolName = ref("")
let resPoolBizDemand = ref("")

let resPools = ref([]);
let columns = [{
  type: "selection",
  fixed:"left"
},{
  title:"名称",
  key: "name",
  fixed:"left",
  width: 250
},{
  title:"处理器",
  key: "processor",
  fixed:"left",
  width: 150
},
  {
    title:"内存(GB)",
    key: "memory",
    fixed:"left",
    width: 150
  },

  {
    title:"硬盘容量(GB)",
    key: "disk",
    fixed:"left",
    width: 150
  },
  {
    title:"网络带宽(Gbps)",
    key: "net",
    fixed:"left",
    width: 150
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
.res-pool-view{
  display: flex;
  flex-direction: column;
  width: 100%;
  height: 100%;
}
</style>