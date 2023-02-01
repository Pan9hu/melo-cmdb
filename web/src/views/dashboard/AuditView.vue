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
      <n-input placeholder="按照 ID 搜索, 与其他条件互斥" style="width: 250px; margin-right: 5px"/>
      <n-input tplaceholder="按照群组搜索, 支持全文搜索" style="width: 250px; margin-right: 5px"/>
      <n-input  placeholder="按照资源池搜索, 支持全文搜索" style="width: 250px; margin-right: 5px"/>
      <n-select v-model:value="auditTypeSearchOptionValue" size="medium" :options="auditStatusOptions"
                placeholder="选择机器类型" style="width: 150px; margin-right: 5px;"/>
      <n-tooltip placement="top" trigger="hover">
        <template #trigger>
          <n-button  secondary tertiary circle style="margin-left: 5px" type="info">
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
        <span>将勾选审计内容下载</span>
      </n-tooltip>
    </div>
    <n-data-table striped :columns="columns" :data="machines" :pagination="pagination"/>
    <div style="width: 100%; min-height: 20px;"></div>
  </div>
</template>

<script setup>
import {h, reactive, ref} from "vue";
import {NButton, NTag} from "naive-ui";
import {SearchOutlined, CloseOutlined,DownloadOutlined} from "@vicons/antd"


let auditTypeSearchOptionValue = ref(null);


let auditStatusOptions= [
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
    label: "容器",
    value: "容器"
  },
]

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


let columns = [
  {
    title: "ID",
    key: "id",
    width: 320
  },{
    title: "员工姓名",
    key: "name",
    width: 320
  }
]

let information = ref(null)

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
