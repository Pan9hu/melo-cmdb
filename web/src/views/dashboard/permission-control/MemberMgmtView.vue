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
      <n-input style="width: 350px; margin-right: 10px;" v-model:value="memberName" type="text" placeholder="请输入姓名"/>
      <n-input style="width: 350px; margin-right: 10px;" v-model:value="memberNo" type="text" placeholder="请输入工号"/>
      <n-input style="width: 350px; margin-right: 10px;" v-model:value="memberGroup" type="text" placeholder="请输入组"/>
      <n-input style="width: 400px; margin-right: 10px;" v-model:value="memberPhone" type="text" placeholder="请输入手机号码"/>
      <n-input style="width: 400px; margin-right: 10px;" v-model:value="memberEmail" type="text" placeholder="请输入工作邮箱"/>
      <n-select style="width: 300px; margin-right: 10px;" v-model:value="memberSexSelectOptionValue"
                :options="memberSexSelectOptions" placeholder="请选择性别"/>
      <n-input style="margin-right: 10px;" v-model:value="memberArchGroup" type="text" placeholder="请输入组织架构, 支持全文检索.."/>
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
    <n-data-table striped :columns="columns" :data="members" :pagination="pagination"/>
    <div style="width: 100%; min-height: 20px;"></div>
  </div>
</template>

<script setup>
import {h, reactive, ref} from "vue";
import {NButton, NTag} from "naive-ui";
import {SearchOutlined, CloseOutlined} from "@vicons/antd"


let memberName = ref("");
let memberNo = ref("");
let memberGroup = ref("");
let memberPhone = ref("");
let memberEmail = ref("");
let memberSexSelectOptionValue = ref(null)
let memberArchGroup = ref("");

const memberSexSelectOptions = [
  {
    label: "全部",
    value: null
  }, {
    label: "男",
    value: "男"
  },{
    label: "女",
    value: "女"
  },{
    label: "其他",
    value: "其他"
  },
]


function handleDeleteCurrentItemButtonClicked(row){

}

let members = ref([{
  "key": "0",
  "name":"小王",
  "no": "Z12831839",
  "group": "运维一组",
  "arch-group" : "/xxxx/xxxx/xxxx",
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