<template>
  <div class="member-mgmt-view">
    <n-page-header>
      <template #header>
        <n-breadcrumb>
          <n-breadcrumb-item>权限控制</n-breadcrumb-item>
          <n-breadcrumb-item>成员</n-breadcrumb-item>
        </n-breadcrumb>
      </template>
    </n-page-header>
    <div class="op-area">
      <n-input style="width: 350px; margin-right: 10px;" v-model:value="memberName" type="text"
               placeholder="请输入姓名"/>
      <n-input style="width: 600px; margin-right: 10px;" v-model:value="memberNo" type="text" placeholder="请输入工号, 与其他条件互斥"/>
      <n-input style="width: 350px; margin-right: 10px;" v-model:value="memberGroup" type="text"
               placeholder="请输入组"/>
      <n-input style="width: 400px; margin-right: 10px;" v-model:value="memberPhone" type="text"
               placeholder="请输入手机号码"/>
      <n-input style="width: 400px; margin-right: 10px;" v-model:value="memberEmail" type="text"
               placeholder="请输入工作邮箱"/>
      <n-select style="width: 350px; margin-right: 10px;" v-model:value="memberSexSelectOptionValue"
                :options="memberSexSelectOptions" placeholder="请选择性别"/>
      <n-input style="margin-right: 10px;" v-model:value="memberArchGroup" type="text"
               placeholder="请输入组织架构, 支持全文检索.."/>
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
    <n-data-table striped :columns="columns" :data="members" :pagination="pagination"/>
    <n-modal v-model:show="isShowAddModal" :mask-closablef="false" preset="card" title="添加成员"
             :on-after-leave="onAddModalAfterLeave" :segmented="false" style="width: 45%; min-width: 600px">
      <div style="display: flex;width: 100%; height: 100%; flex-direction: column">
        <div style="width: 100%; ">
          <div style="font-size: 12pt; font-weight: bold;">姓名</div>
          <n-input type="text" placeholder="必填, 请输入姓名" style="margin-bottom: 10px; max-width: 200px"/>
          <div style="font-size: 12pt; font-weight: bold;">工号</div>
          <n-input type="text" placeholder="必填, 请输入工号" style="margin-bottom: 10px; max-width: 250px"/>
          <div style="font-size: 12pt; font-weight: bold;">组</div>
          <n-select placeholder="必填, 请选择组" style="margin-bottom: 10px; max-width: 200px"/>
          <div style="font-size: 12pt; font-weight: bold;">性别</div>
          <n-select placeholder="必填, 请选择性别" style="margin-bottom: 10px; max-width: 150px"/>
          <div style="font-size: 12pt; font-weight: bold;">手机号码</div>
          <n-input type="text" placeholder="必填, 请输入手机号码" style="margin-bottom: 10px; max-width: 220px"/>
          <div style="font-size: 12pt; font-weight: bold;">工作邮箱</div>
          <n-input type="text" placeholder="必填, 请输入工作邮箱" style="margin-bottom: 10px; max-width: 300px"/>
          <div style="font-size: 12pt; font-weight: bold;">组织架构</div>
          <n-input type="text" placeholder="必填, 请输入组织架构" style="margin-bottom: 10px;"/>
        </div>
        <div style="display: flex; width: 100%; height: 100%; justify-content: flex-end; margin-top: 10px">
          <n-button @click="onAddModalFailed" style="margin-right: 10px;">取&nbsp;消</n-button>
          <n-button @click="onAddModalOk" type="primary">添&nbsp;加</n-button>
        </div>
      </div>
    </n-modal>
    <n-modal v-model:show="isShowDetailModal" :mask-closablef="false" preset="card" title="Z12831839 的详细信息"
             :on-after-leave="onDetailModalAfterLeave" :segmented="false" style="width: 45%; min-width: 600px">
      <div style="display: flex;width: 100%; height: 100%; flex-direction: column">
        <div style="width: 100%; ">
          <div style="font-size: 12pt; font-weight: bold;">姓名</div>
          <n-input type="text" placeholder="必填, 请输入姓名" style="margin-bottom: 10px; max-width: 200px" disabled/>
          <div style="font-size: 12pt; font-weight: bold;">组</div>
          <n-select placeholder="必填, 请选择组" style="margin-bottom: 10px; max-width: 200px" disabled/>
          <div style="font-size: 12pt; font-weight: bold;">性别</div>
          <n-select placeholder="必填, 请选择性别" style="margin-bottom: 10px; max-width: 150px" disabled/>
          <div style="font-size: 12pt; font-weight: bold;">手机号码</div>
          <n-input type="text" placeholder="必填, 请输入手机号码" style="margin-bottom: 10px; max-width: 220px"
                   disabled/>
          <div style="font-size: 12pt; font-weight: bold;">工作邮箱</div>
          <n-input type="text" placeholder="必填, 请输入工作邮箱" style="margin-bottom: 10px; max-width: 300px"
                   disabled/>
          <div style="font-size: 12pt; font-weight: bold;">组织架构</div>
          <n-input type="text" placeholder="必填, 请输入组织架构" style="margin-bottom: 10px;" disabled/>
          <div style="font-size: 12pt; font-weight: bold;">创建时间</div>
          <n-date-picker type="datetime" clearable disabled placeholder="创建时间" style="max-width: 300px;"/>
          <div style="font-size: 12pt; font-weight: bold;">最后一次修改时间</div>
          <n-date-picker type="datetime" clearable disabled placeholder="最后一次修改时间" style="max-width: 300px;"/>
        </div>
        <div style="display: flex; width: 100%; height: 100%; justify-content: flex-end; margin-top: 10px">
          <n-button @click="onDetailModalOk" type="primary">关&nbsp;闭</n-button>
        </div>
      </div>
    </n-modal>
    <n-modal v-model:show="isShowModifyModal" :mask-closablef="false" preset="card" title="修改成员"
             :on-after-leave="onModifyModalAfterLeave" :segmented="false" style="width: 45%; min-width: 600px">
      <div style="display: flex;width: 100%; height: 100%; flex-direction: column">
        <div style="width: 100%; ">
          <div style="font-size: 12pt; font-weight: bold;">姓名</div>
          <n-input type="text" placeholder="必填, 请输入姓名" style="margin-bottom: 10px; max-width: 200px"/>
          <div style="font-size: 12pt; font-weight: bold;">组</div>
          <n-select placeholder="必填, 请选择组" style="margin-bottom: 10px; max-width: 200px"/>
          <div style="font-size: 12pt; font-weight: bold;">性别</div>
          <n-select placeholder="必填, 请选择性别" style="margin-bottom: 10px; max-width: 150px"/>
          <div style="font-size: 12pt; font-weight: bold;">手机号码</div>
          <n-input type="text" placeholder="必填, 请输入手机号码" style="margin-bottom: 10px; max-width: 220px"/>
          <div style="font-size: 12pt; font-weight: bold;">工作邮箱</div>
          <n-input type="text" placeholder="必填, 请输入工作邮箱" style="margin-bottom: 10px; max-width: 300px"/>
          <div style="font-size: 12pt; font-weight: bold;">组织架构</div>
          <n-input type="text" placeholder="必填, 请输入组织架构" style="margin-bottom: 10px;"/>
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
import {NButton, useDialog, useMessage} from "naive-ui";
import {SearchOutlined, CloseOutlined, PlusOutlined, DeleteOutlined} from "@vicons/antd"
import TableOperationAreaButtonGroup from "@/components/TableOperationAreaButtonGroup.vue";

const dialog = useDialog()
const message = useMessage()

let memberName = ref("");
let memberNo = ref("");
let memberGroup = ref("");
let memberPhone = ref("");
let memberEmail = ref("");
let memberSexSelectOptionValue = ref(null)
let memberArchGroup = ref("");
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
  isShowAddModal.value =false;
}

function onAddModalFailed() {
  isShowAddModal.value =false;
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

const memberSexSelectOptions = [
  {
    label: "全部",
    value: null
  }, {
    label: "男",
    value: "男"
  }, {
    label: "女",
    value: "女"
  }, {
    label: "其他",
    value: "其他"
  },
]


let members = ref([{
  "key": "0",
  "name": "小王",
  "no": "Z12831839",
  "group": "运维一组",
  "arch-group": "/xxxx/xxxx/xxxx",
  "phone": "1829317193",
  "email": "xxxxxxxxxx@gmail.com",
  "sex": "男",
  "create-time": "2023/12/09 09:09:01",
  "update-time": "2023/12/09 09:09:02",
}]);

let columns = [{
  type: "selection",
  fixed: "left"
}, {
  title: "姓名",
  key: "name",
  fixed: "left",
  width: 100
}, {
  title: "工号",
  key: "no",
  width: 150
}, {
  title: "组",
  key: "group",
  width: 200,
  fixed: "left"
},
  {
    title: "手机号码",
    key: "phone",
    width: 150
  }, {
    title: "工作邮箱",
    key: "email",
    width: 220
  },
  {
    title: "性别",
    key: "sex",
    width: 100
  },
  {
    title: "组织架构",
    key: "arch-group",
    resizable: true,
  },

  {
    title: "创建时间",
    key: "create-time",
    width: 200
  }, {
    title: "最后一次修改时间",
    key: "update-time",
    width: 200
  }, {
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

.member-mgmt-view {
  display: flex;
  flex-direction: column;
  width: 100%;
  height: 100%;
}
</style>