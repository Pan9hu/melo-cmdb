<template>
  <div class="group-mgmt-view">
    <n-page-header>
      <template #header>
        <n-breadcrumb>
          <n-breadcrumb-item>权限控制</n-breadcrumb-item>
          <n-breadcrumb-item>组</n-breadcrumb-item>
        </n-breadcrumb>
      </template>
    </n-page-header>
    <div class="op-area">
      <n-select style="width: 250px; margin-right: 10px;" size="medium"  v-model:value="roleSelectOptionValue"
                :options="roleSelectOptions" placeholder="选择检索条件"/>
      <n-input placeholder="按照组名或者用途搜索, 支持全文搜索.." type="text"/>
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
    <n-data-table striped :columns="columns" :data="groups" :pagination="pagination"/>
    <div style="width: 100%; min-height: 20px;"></div>
  </div>
</template>

<script setup>
import {h, reactive, ref} from "vue";
import {NButton} from "naive-ui";
import {SearchOutlined, CloseOutlined} from "@vicons/antd"


let roleSelectOptionValue = ref(null)

let roleSelectOptions = [
  {
    label: "全部",
    value: null
  }, {
    label: "名称",
    value: "名称"
  }, {
    label: "用途",
    value: "用途"
  },
]

function handleDeleteCurrentItemButtonClicked(row) {
}

let groups = ref([{
  "key": "0",
  "name": "运维一组",
  "create-time": "2023/12/09 09:09:01",
  "usage": "用户处理日常运维工作"
}])

let columns = [
  {
    type: "selection",
    fixed: "left"
  }, {
    title: "组名",
    key: "name",
    fixed: "left",
    width: 250
  }, {
    title: "创建时间",
    key: "create-time",
    width: 200

  }, {
    title: "备注",
    key: "usage",
    resizable: true,
  }, {
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


</script>

<style scoped>
.op-area {
  padding-top: 15px;
  padding-bottom: 15px;
  display: flex;
}

.group-mgmt-view {
  display: flex;
  flex-direction: column;
  width: 100%;
  height: 100%;
}
</style>