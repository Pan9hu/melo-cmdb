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
      <n-select style="width: 250px; margin-right: 10px;" size="medium" v-model:value="roleSelectOptionValue"
                :options="roleSelectOptions" placeholder="选择检索条件"/>
      <n-input style="margin-right: 10px;" placeholder="按照组名或者用途搜索, 支持全文检索.." type="text"/>
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
          <n-button secondary tertiary circle style="margin-left: 5px" type="success"
                    @click="handleAddButtonClicked">
            <template #icon>
              <n-icon>
                <plus-outlined/>
              </n-icon>
            </template>
          </n-button>
        </template>
        <span>添加</span>
      </n-tooltip>
      <n-tooltip placement="top" trigger="hover">
        <template #trigger>
          <n-button secondary tertiary circle style="margin-left: 5px" type="warning"
                    @click="handleBatchDeleteButtonClicked">
            <template #icon>
              <n-icon>
                <delete-outlined/>
              </n-icon>
            </template>
          </n-button>
        </template>
        <span>删除选中的条目</span>
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
    <n-modal v-model:show="isShowAddModal" :mask-closablef="false" preset="card" title="添加组"
             :on-after-leave="onAddModalAfterLeave" :segmented="false" style="width: 45%; min-width: 600px">
      <div style="display: flex;width: 100%; height: 100%; flex-direction: column">
        <div style="width: 100%; ">
          <div style="font-size: 12pt; font-weight: bold;">名称</div>
          <n-input type="text" placeholder="必填, 请输入名称" style="margin-bottom: 10px; max-width: 200px"/>
          <div style="font-size: 12pt; font-weight: bold;">用途</div>
          <n-input type="text" placeholder="请输入用途"/>
        </div>
        <div style="display: flex; width: 100%; height: 100%; justify-content: flex-end; margin-top: 10px">
          <n-button @click="onAddModalFailed" style="margin-right: 10px;">取&nbsp;消</n-button>
          <n-button @click="onAddModalOk" type="primary">添&nbsp;加</n-button>
        </div>
      </div>
    </n-modal>
    <n-modal v-model:show="isShowModifyModal" :mask-closablef="false" preset="card" title="修改组"
             :on-after-leave="onModifyModalAfterLeave" :segmented="false" style="width: 45%; min-width: 600px">
      <div style="display: flex;width: 100%; height: 100%; flex-direction: column">
        <div style="width: 100%; ">
          <div style="font-size: 12pt; font-weight: bold;">用途</div>
          <n-input type="text" placeholder="请输入用途"/>
        </div>
        <div style="display: flex; width: 100%; height: 100%; justify-content: flex-end; margin-top: 10px">
          <n-button @click="onModifyModalFailed" style="margin-right: 10px;">取&nbsp;消</n-button>
          <n-button @click="onModifyModalOk" type="primary">修&nbsp;改</n-button>
        </div>
      </div>
    </n-modal>
    <div style="width: 100%; min-height: 20px;"></div>
  </div>
</template>

<script setup>
import {h, reactive, ref, getCurrentInstance, onMounted} from "vue";
import {NButton, useDialog, useMessage} from "naive-ui";
import {SearchOutlined, CloseOutlined, DeleteOutlined, PlusOutlined} from "@vicons/antd"
import TableOperationAreaButtonGroup from "@/components/TableOperationAreaButtonGroup.vue";

const {proxy} = getCurrentInstance()

onMounted(() => {
  proxy.$axios.get("/api/group/", {}).then(r => {
    if (r.status === 200) {
      const content = r.data
      if (content["code"] === "10000") {
        const data = content["data"]
        let result = [];

        data.map((item) => {
          result.push({
            "key": item["name"],
            "name": item["name"],
            "create-time": item["create_time"],
            "usage": item["usage"]
          })
        });

        groups.value = result;
      } else {
      }
    } else {
      console.error(r.status)
    }
  }).catch(e => {
  })
})


const dialog = useDialog()
const message = useMessage()


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

let isShowAddModal = ref(false);
let isShowModifyModal = ref(false);

function onAddModalAfterLeave() {
}

function onModifyModalAfterLeave() {
}

function onAddModalOk() {
  isShowAddModal.value = false;
}

function onAddModalFailed() {
  isShowAddModal.value = false;
}

function onModifyModalFailed() {
  isShowModifyModal.value = false;
}

function onModifyModalOk() {
  isShowModifyModal.value = false;
}

function handleAddButtonClicked() {
  isShowAddModal.value = true;
}

function handleBatchDeleteButtonClicked() {
  dialog.warning({
    title: "批量删除",
    content: "即将删除 24 个条目, 是否继续?",
    positiveText: "确定",
    negativeText: "取消",
    onPositiveClick: () => {
      message.success("删除成功")
    },
  })
}


let groups = ref([])

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
    title: "用途",
    key: "usage",
    resizable: true,
  }, {
    title: "操作",
    key: "op",
    render(row) {
      return h(
          TableOperationAreaButtonGroup, {
            isShowDetail: false,
            isShowModify: true,
            isShowDelete: true,
            onDetailButtonClicked: () => {
            },
            onModifyButtonClicked: () => {
              isShowModifyModal.value = true
            },
            onDeleteButtonClicked: () => {
            },
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