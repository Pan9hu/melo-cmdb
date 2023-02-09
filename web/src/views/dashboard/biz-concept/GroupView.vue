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
               placeholder="请输入名称, 与其他条件互斥"/>
      <n-select v-model:value="groupLevelSelectOptionValue" size="medium" :options="groupLevelSelectOptions"
                placeholder="请选择层级" style="width: 300px; margin-right: 10px;"/>
      <n-input style="width: 700px; margin-right: 10px;" v-model:value="parentGroup" type="text"
               placeholder="请输入所属群组"/>
      <n-input style="margin-right: 10px;" v-model:value="bizDemand" type="text" placeholder="请输入业务需求, 支持全文检索.." />
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
          <n-button secondary tertiary circle style="margin-left: 5px" type="warning"  @click="handleBatchDeleteButtonClicked">
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
    <n-modal v-model:show="isShowAddModal" :mask-closablef="false" preset="card" title="添加群组"
              :on-after-leave="onAddModalAfterLeave" :segmented="false" style="width: 45%; min-width: 600px">
      <div style="display: flex;width: 100%; height: 100%; flex-direction: column">
        <div style="width: 100%; ">
          <div style="font-size: 12pt; font-weight: bold;">名称</div>
          <n-input type="text" placeholder="必填, 请输入名称" style="margin-bottom: 10px; max-width: 150px"/>

          <div style="font-size: 12pt; font-weight: bold;">层级</div>
          <n-select placeholder="必填, 请选择层级" style="margin-bottom: 10px; max-width: 200px"/>
          <div style="font-size: 12pt; font-weight: bold;">所属群组</div>
          <n-select placeholder="必填, 请选择所属群组" style="margin-bottom: 10px; max-width: 200px"/>
          <div style="font-size: 12pt; font-weight: bold;">业务需求</div>
          <n-input type="text" placeholder="必填, 请输入业务需求" style="margin-bottom: 10px;"/>
        </div>
        <div style="display: flex; width: 100%; height: 100%; justify-content: flex-end; margin-top: 10px">
          <n-button @click="onAddModalFailed" style="margin-right: 10px;">取&nbsp;消</n-button>
          <n-button @click="onAddModalOk" type="primary">添&nbsp;加</n-button>
        </div>
      </div>
    </n-modal>
    <n-modal v-model:show="isShowModifyModal" :mask-closablef="false" preset="card" title="修改群组"
             :on-after-leave="onAddModalAfterLeave" :segmented="false" style="width: 45%; min-width: 600px">
      <div style="display: flex;width: 100%; height: 100%; flex-direction: column">
        <div style="width: 100%; ">
          <div style="font-size: 12pt; font-weight: bold;">名称</div>
          <n-input type="text" placeholder="必填, 请输入名称" style="margin-bottom: 10px; max-width: 150px"/>

          <div style="font-size: 12pt; font-weight: bold;">层级</div>
          <n-select placeholder="必填, 请选择层级" style="margin-bottom: 10px; max-width: 200px"/>
          <div style="font-size: 12pt; font-weight: bold;">所属群组</div>
          <n-select placeholder="必填, 请选择所属群组" style="margin-bottom: 10px; max-width: 200px"/>
          <div style="font-size: 12pt; font-weight: bold;">业务需求</div>
          <n-input type="text" placeholder="必填, 请输入业务需求" style="margin-bottom: 10px;"/>
<!--          TODO 应该有地方向安全组中添加机器和安全组-->
<!--          <div style="font-size: 12pt; font-weight: bold;">安全组</div>-->
<!--          <n-input type="textarea" row="10" placeholder="选填, 请输入安全组名称, 使用英文半角小写逗号分隔" style="margin-bottom: 10px;"/>-->
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
import {SearchOutlined, CloseOutlined,PlusOutlined,DeleteOutlined} from "@vicons/antd"
import TableOperationAreaButtonGroup from "@/components/TableOperationAreaButtonGroup.vue";
const dialog = useDialog()
const message = useMessage()

let isShowModifyModal = ref(false);
let isShowAddModal = ref(false);

function onAddModalAfterLeave(){

}

function onAddModalOk(){
  isShowAddModal.value =false;
}

function onAddModalFailed(){
  isShowAddModal.value =false;
}

function onModifyModalFailed() {
  isShowModifyModal.value = false;
}

function onModifyModalOk() {
  isShowModifyModal.value = false;
}

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


let groups = ref([{
  "key" : "0",
  "name" : "1",
  "level" : "1",
  "parent" : "1",
  "create-time" : "2023/2/7 18:32:30",
  "usage" : "1",
  // M 表示当前群组下面的机器所用的安全组
  // G 表示当前群组下面次级群组所用的安全组
  // 只能修改当前群组下面机器的安全组，会影响当前层级群组下面全部机器的安全组
  // 若要修改机器的安全组配置, 那么可以通过搜索指定的机器进行修改，在机器页面
  "safe-group-list" : ["M:Web 业务", "M:数据库服务","G:网关服务"]

}]);



function handleAddButtonClicked(){
  isShowAddModal.value = true;
}

function handleBatchDeleteButtonClicked(){
  dialog.warning({
    title: "批量删除",
    content:"即将删除 24 个条目, 是否继续?",
    positiveText: "确定",
    negativeText: "取消",
    onPositiveClick:()=>{
      message.success("删除成功!")
    },
  })
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
    title: "安全组",
    key: "safe-group-list",
    resizable: true,
    render(row) {
      return row["safe-group-list"].map((tagKey) => {
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
          TableOperationAreaButtonGroup, {
            isShowDetail: false,
            isShowModify: true,
            isShowDelete: true,
            onDetailButtonClicked: () => {
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
