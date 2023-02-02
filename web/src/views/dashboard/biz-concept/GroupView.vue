<template>
  <div class="group-view">
    <n-page-header>
      <template #header>
        <n-breadcrumb>
          <n-breadcrumb-item>业务概念</n-breadcrumb-item>
          <n-breadcrumb-item>群组</n-breadcrumb-item>
        </n-breadcrumb>
      </template>
    </n-page-header>
    <div class="op-area">
      <n-input style="width: 700px; margin-right: 10px;" v-model:value="groupName" type="text"
               placeholder="请输入名称"/>
      <n-select v-model:value="groupLevelSelectOptionValue" size="medium" :options="groupLevelSelectOptions"
                placeholder="请选择层级" style="width: 300px; margin-right: 10px;"/>
      <n-input style="width: 700px; margin-right: 10px;" v-model:value="parentGroup" type="text"
               placeholder="请输入所属群组"/>
      <n-input v-model:value="bizDemand" type="text" placeholder="请输入业务需求, 支持全文检索.." />
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
import {NButton, NTag} from "naive-ui";
import {SearchOutlined, CloseOutlined} from "@vicons/antd"


let groupName = ref("")
let parentGroup = ref("")

let groupLevelSelectOptionValue = ref(null)


let groupLevelSelectOptions = [
  {
    label: "全部",
    value: null
  }, {
    label: "第一层",
    value: "第一层"
  }, {
    label: "第二层",
    value: "第二层"
  }, {
    label: "第三层",
    value: "第三层"
  },
]

let bizDemand = ref("")


let groups = ref([{}]);


function handleDeleteCurrentItemButtonClicked(row) {
}

let columns = [{
  type: "selection",
  fixed: "left"
}, {
  title: "名称",
  key: "name",
  fixed: "left",
  width: 250
}, {
  title: "层级",
  key: "level",
  fixed: "left",
  width: 80
}, {
  title: "所属群组",
  key: "parent",
  width: 250
},
  {
    title: "创建时间",
    key: "create-time",
    width: 200

  }, {
    title: "业务需求",
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

.group-view {
  display: flex;
  flex-direction: column;
  width: 100%;
  height: 100%;
}
</style>
