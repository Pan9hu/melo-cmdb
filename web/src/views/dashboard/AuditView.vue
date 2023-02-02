<template>
  <div class="audit-view">
    <n-page-header>
      <template #header>
        <n-breadcrumb>
          <n-breadcrumb-item>审计</n-breadcrumb-item>
        </n-breadcrumb>
      </template>
    </n-page-header>
    <div class="op-area">
      <n-select style="width: 250px; margin-right: 10px;" v-model:value="levelSearchOptionValue"
                :options="levelSearchOptions" placeholder="选择等级"/>
      <n-select style="width: 250px; margin-right: 10px;" v-model:value="resultSearchOptionValue"
                :options="resultSearchOptions" placeholder="选择结果"/>
      <n-input placeholder="请输入成员ID" type="text" style="width: 250px; margin-right: 10px"/>
      <n-input placeholder="请输入成员姓名" type="text" style="width: 250px; margin-right: 10px"/>
      <n-input placeholder="请输入时间, 支持全文搜索.." type="text"/>
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
      <n-tooltip placement="top" trigger="hover">
        <template #trigger>
          <n-button secondary tertiary circle style="margin-left: 5px" type="warning">
            <template #icon>
              <n-icon>
                <download-outlined/>
              </n-icon>
            </template>
          </n-button>
        </template>
        <span>下载当前表格中的内容</span>
      </n-tooltip>
    </div>
    <n-data-table striped :columns="columns" :data="items" :pagination="pagination"/>
    <div style="width: 100%; min-height: 20px;"></div>
  </div>
</template>

<script setup>
import {reactive, ref} from "vue";
import {NButton} from "naive-ui";
import {SearchOutlined, CloseOutlined, DownloadOutlined} from "@vicons/antd"


let levelSearchOptionValue = ref(null);


let levelSearchOptions = [
  {
    label: "全部",
    value: null

  },
  {
    label: "写入",
    value: "写入"

  }, {
    label: "已关闭",
    value: "已关闭"
  }, {
    label: "读取",
    value: "读取"
  }, {
    label: "读取",
    value: "读取"
  }
]
let resultSearchOptionValue = ref(null);


let resultSearchOptions = [
  {
    label: "成功",
    value: "成功"

  }, {
    label: "失败",
    value: "失败"
  }
]


let columns = [
  {
    type: "selection",
    fixed: "left"
  },
  {
    title: "登记",
    key: "level",
    width: 320
  }, {
    title: "成员ID",
    key: "uid",
    width: 320
  }, {
    title: "成员姓名",
    key: "name",
    width: 320
  }, {
    title: "执行结果",
    key: "result",
    width: 320
  }, {
    title: "时间点",
    key: "create-time",
    width: 320
  }, {
    title: "事件",
    key: "event",
    width: 320
  },
]

let items = ref([{
  "key": "0",
  "level": "写入",
  "uid": "Z1231SS",
  "name": "小林",
  "result": "成功",
  "create": "2023/2/2 12:31:32",
  "event": "在 /权限控制/成员 中, 添加了 小周 / Z123SA",
}])


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

.audit-view {
  display: flex;
  flex-direction: column;
  width: 100%;
  height: 100%;
}
</style>
