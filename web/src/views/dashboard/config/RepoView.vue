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
          <n-button secondary tertiary circle style="margin-left: 5px" type="success" @click="handleAddButtonClicked">
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
    <n-data-table striped :columns="columns" :data="repo" :pagination="pagination"/>
    <n-modal v-model:show="isShowAddModal" :mask-closablef="false" preset="card" title="添加存储库"
             :on-after-leave="onAddModalAfterLeave" :segmented="false" style="width: 45%; min-width: 600px">
      <div style="display: flex;width: 100%; height: 100%; flex-direction: column">
        <div style="width: 100%; ">
          <div style="font-size: 12pt; font-weight: bold;">名称</div>
          <n-input type="text" placeholder="必填, 请输入名称" style="margin-bottom: 10px; max-width: 350px"/>
          <div style="font-size: 12pt; font-weight: bold;">类型</div>
          <n-select type="text" placeholder="必填, 请选择类型" style="margin-bottom: 10px; max-width: 150px"/>
          <div style="font-size: 12pt; font-weight: bold;">地址</div>
          <n-input type="text" placeholder="必填, 请输入地址" style="margin-bottom: 10px; max-width: 500px"/>
          <div style="font-size: 12pt; font-weight: bold;">用途</div>
          <n-input type="text" placeholder="必填, 请输入用途" style="margin-bottom: 10px;"/>
        </div>
        <div style="display: flex; width: 100%; height: 100%; justify-content: flex-end; margin-top: 10px">
          <n-button @click="onAddModalFailed" style="margin-right: 10px;">取&nbsp;消</n-button>
          <n-button @click="onAddModalOk" type="primary">添&nbsp;加</n-button>
        </div>
      </div>
    </n-modal>
    <n-modal v-model:show="isShowDetailModal" :mask-closablef="false" preset="card" title="xxx的详情"
             :on-after-leave="onDetailModalAfterLeave" :segmented="false" style="width: 45%; min-width: 600px">
      <div style="display: flex;width: 100%; height: 100%; flex-direction: column">
        <div style="width: 100%; ">
          <div style="font-size: 12pt; font-weight: bold;">类型</div>
          <n-select type="text" placeholder="必填, 请选择类型" style="margin-bottom: 10px; max-width: 150px" disabled/>
          <div style="font-size: 12pt; font-weight: bold;">地址</div>
          <n-input type="text" placeholder="必填, 请输入地址" style="margin-bottom: 10px; max-width: 500px" disabled/>
          <div style="font-size: 12pt; font-weight: bold;">用途</div>
          <n-input type="text" placeholder="必填, 请输入用途" style="margin-bottom: 10px;" disabled/>
        </div>
        <div style="display: flex; width: 100%; height: 100%; justify-content: flex-end; margin-top: 10px">
          <n-button @click="onDetailModalOk" type="primary">关&nbsp;闭</n-button>
        </div>
      </div>
    </n-modal>
    <n-modal v-model:show="isShowModifyModal" :mask-closablef="false" preset="card" title="修改存储库"
             :on-after-leave="onModifyModalAfterLeave" :segmented="false" style="width: 45%; min-width: 600px">
      <div style="display: flex;width: 100%; height: 100%; flex-direction: column">
        <div style="width: 100%; ">
          <div style="font-size: 12pt; font-weight: bold;">类型</div>
          <n-select type="text" placeholder="必填, 请选择类型" style="margin-bottom: 10px; max-width: 150px"/>
          <div style="font-size: 12pt; font-weight: bold;">地址</div>
          <n-input type="text" placeholder="必填, 请输入地址" style="margin-bottom: 10px; max-width: 500px"/>
          <div style="font-size: 12pt; font-weight: bold;">用途</div>
          <n-input type="text" placeholder="必填, 请输入用途" style="margin-bottom: 10px;"/>
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
import {h, reactive, ref} from "vue";
import {NButton, NTag, useDialog, useMessage} from "naive-ui";
import {SearchOutlined, CloseOutlined, DeleteOutlined, PlusOutlined} from "@vicons/antd"
import TableOperationAreaButtonGroup from "@/components/TableOperationAreaButtonGroup.vue";

const dialog = useDialog()
const message = useMessage()

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
          TableOperationAreaButtonGroup, {
            isShowDetail: true,
            isShowModify: true,
            isShowDelete: true,
            onDetailButtonClicked: () => {
              isShowDetailModal.value = true;
            },
            onModifyButtonClicked: () => {
              isShowModifyModal.value = true;
            },
            onDeleteButtonClicked: () => {
            },
          }
      );
    },
    fixed: "right",
    width: 150
  },
];

let isShowAddModal = ref(false);
let isShowModifyModal = ref(false);
let isShowDetailModal = ref(false);

function onAddModalAfterLeave() {

}

function onModifyModalAfterLeave() {

}

function onDetailModalAfterLeave() {

}

function onAddModalOk() {
  isShowAddModal.value = false;
}

function onAddModalFailed() {
  isShowAddModal.value = false;
}

function onDetailModalOk() {
  isShowDetailModal.value = false;
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
      message.success("删除成功!")
    },
  })
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