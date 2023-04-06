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
               placeholder="请输入姓名" @keyup.enter="handleSearchButtonClicked"/>
      <n-input style="width: 600px; margin-right: 10px;" v-model:value="memberUid" type="text"
               placeholder="请输入工号, 与其他条件互斥" @keyup.enter="handleSearchButtonClicked"/>
      <n-input style="width: 350px; margin-right: 10px;" v-model:value="memberGroup" type="text"
               placeholder="请输入组" @keyup.enter="handleSearchButtonClicked"/>
      <n-input style="width: 400px; margin-right: 10px;" v-model:value="memberPhone" type="text"
               placeholder="请输入手机号码" @keyup.enter="handleSearchButtonClicked"/>
      <n-input style="width: 400px; margin-right: 10px;" v-model:value="memberEmail" type="text"
               placeholder="请输入工作邮箱" @keyup.enter="handleSearchButtonClicked"/>
      <n-select style="width: 350px; margin-right: 10px;" v-model:value="memberSexSelectOptionValue"
                :options="memberSexSelectOptions" placeholder="请选择性别"/>
      <n-input style="margin-right: 10px;" v-model:value="memberArchGroup" type="text"
               placeholder="请输入组织架构, 支持全文检索.." @keyup.enter="handleSearchButtonClicked"/>
      <n-tooltip placement="top" trigger="hover">
        <template #trigger>
          <n-button secondary tertiary circle style="margin-left: 5px" type="info" @click="handleSearchButtonClicked">
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
        <span>添加成员</span>
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
          <n-button secondary tertiary circle style="margin-left: 5px" type="error"
                    @click="handleClearSearchContent">
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
    <n-data-table striped :columns="columns" :data="members" @update-checked-row-keys="handleCheck"
                  :pagination="pagination"/>
    <n-modal v-model:show="isShowAddModal" :mask-closablef="false" preset="card" title="添加成员"
             :on-after-leave="onAddModalAfterLeave" :segmented="false" style="width: 45%; min-width: 600px">
      <div style="display: flex;width: 100%; height: 100%; flex-direction: column">
        <div style="width: 100%; ">
          <div style="font-size: 12pt; font-weight: bold;">姓名</div>
          <n-input type="text" placeholder="必填, 请输入姓名" style="margin-bottom: 10px; max-width: 200px"
                   v-model:value="addMemberName"/>
          <div style="font-size: 12pt; font-weight: bold;">工号</div>
          <n-input type="text" placeholder="必填, 请输入工号" style="margin-bottom: 10px; max-width: 250px"
                   v-model:value="addMemberUid"/>
          <div style="font-size: 12pt; font-weight: bold;">组</div>
          <n-select placeholder="必填, 请选择组" style="margin-bottom: 10px; max-width: 200px"
                    v-model:value="addMemberGroupSelectOptionValue" :options="memberGroupSelectOptions"/>
          <div style="font-size: 12pt; font-weight: bold;">性别</div>
          <n-select placeholder="必填, 请选择性别" style="margin-bottom: 10px; max-width: 150px"
                    v-model:value="addMemberSexSelectOptionValue" :options="sexSelectOptions"/>
          <div style="font-size: 12pt; font-weight: bold;">手机号码</div>
          <n-input type="text" placeholder="必填, 请输入手机号码" style="margin-bottom: 10px; max-width: 220px"
                   v-model:value="addMemberPhone"/>
          <div style="font-size: 12pt; font-weight: bold;">工作邮箱</div>
          <n-input type="text" placeholder="必填, 请输入工作邮箱" style="margin-bottom: 10px; max-width: 300px"
                   v-model:value="addMemberEmail"/>
          <div style="font-size: 12pt; font-weight: bold;">组织架构</div>
          <n-input type="text" placeholder="必填, 请输入组织架构" style="margin-bottom: 10px;"
                   v-model:value="addMemberArchGroup"/>
        </div>
        <div style="display: flex; width: 100%; height: 100%; justify-content: flex-end; margin-top: 10px">
          <n-button @click="onAddModalFailed" style="margin-right: 10px;">取&nbsp;消</n-button>
          <n-button @click="onAddModalOk" type="primary">添&nbsp;加</n-button>
        </div>
      </div>
    </n-modal>
    <n-modal v-model:show="isShowDetailModal" :mask-closablef="false" preset="card" :title="detailTitleValue"
             :on-after-leave="onDetailModalAfterLeave" :segmented="false" style="width: 45%; min-width: 600px">
      <div style="display: flex;width: 100%; height: 100%; flex-direction: column">
        <div style="width: 100%; ">
          <div style="font-size: 12pt; font-weight: bold;">姓名</div>
          <n-input type="text" placeholder="必填, 请输入姓名" v-model:value="detailNameValue"
                   style="margin-bottom: 10px; max-width: 200px" disabled/>
          <div style="font-size: 12pt; font-weight: bold;">组</div>
          <n-select placeholder="必填, 请选择组" v-model:value="detailGroupValue"
                    style="margin-bottom: 10px; max-width: 200px" disabled/>
          <div style="font-size: 12pt; font-weight: bold;">性别</div>
          <n-select placeholder="必填, 请选择性别" v-model:value="detailSexValue"
                    style="margin-bottom: 10px; max-width: 150px" disabled/>
          <div style="font-size: 12pt; font-weight: bold;">手机号码</div>
          <n-input type="text" placeholder="必填, 请输入手机号码" v-model:value="detailPhoneValue"
                   style="margin-bottom: 10px; max-width: 220px"
                   disabled/>
          <div style="font-size: 12pt; font-weight: bold;">工作邮箱</div>
          <n-input type="text" placeholder="必填, 请输入工作邮箱" v-model:value="detailEmailValue"
                   style="margin-bottom: 10px; max-width: 300px"
                   disabled/>
          <div style="font-size: 12pt; font-weight: bold;">组织架构</div>
          <n-input type="text" placeholder="必填, 请输入组织架构" v-model:value="detailArchGroupValue"
                   style="margin-bottom: 10px;" disabled/>
          <div style="font-size: 12pt; font-weight: bold;">创建时间</div>
          <n-input type="text" disabled clearable placeholder="创建时间"
                   v-model:value="detailCreateTime" style="max-width: 300px;"/>
          <div style="font-size: 12pt; font-weight: bold;">最后一次修改时间</div>
          <n-input type="text" disabled clearable placeholder="最后一次修改时间"
                   v-model:value="detailUpdateTime" style="max-width: 300px;"/>
        </div>
        <div style="display: flex; width: 100%; height: 100%; justify-content: flex-end; margin-top: 10px">
          <n-button @click="onDetailModalOk" type="primary">关&nbsp;闭</n-button>
        </div>
      </div>
    </n-modal>
    <n-modal v-model:show="isShowModifyModal" :mask-closablef="false" preset="card" :title="modifyTitleValue"
             :on-after-leave="onModifyModalAfterLeave" :segmented="false" style="width: 45%; min-width: 600px">
      <div style="display: flex;width: 100%; height: 100%; flex-direction: column">
        <div style="width: 100%; ">
          <div style="font-size: 12pt; font-weight: bold;">姓名</div>
          <n-input type="text" placeholder="必填, 请输入姓名" style="margin-bottom: 10px; max-width: 200px"
                   v-model:value="modifyNameValue"/>
          <div style="font-size: 12pt; font-weight: bold;">组</div>
          <n-select placeholder="必填, 请选择组" style="margin-bottom: 10px; max-width: 200px"
                    v-model:value="modifyGroupValue" :options="memberGroupSelectOptions"/>
          <div style="font-size: 12pt; font-weight: bold;">性别</div>
          <n-select placeholder="必填, 请选择性别" style="margin-bottom: 10px; max-width: 150px"
                    v-model:value="modifySexValue" :options="sexSelectOptions"/>
          <div style="font-size: 12pt; font-weight: bold;">手机号码</div>
          <n-input type="text" placeholder="必填, 请输入手机号码" style="margin-bottom: 10px; max-width: 220px"
                   v-model:value="modifyPhoneValue"/>
          <div style="font-size: 12pt; font-weight: bold;">工作邮箱</div>
          <n-input type="text" placeholder="必填, 请输入工作邮箱" style="margin-bottom: 10px; max-width: 300px"
                   v-model:value="modifyEmailValue"/>
          <div style="font-size: 12pt; font-weight: bold;">组织架构</div>
          <n-input type="text" placeholder="必填, 请输入组织架构" style="margin-bottom: 10px;"
                   v-model:value="modifyArchGroupValue"/>
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
import {getCurrentInstance, h, onMounted, reactive, ref, watch} from "vue";
import {NButton, useDialog, useMessage} from "naive-ui";
import {SearchOutlined, CloseOutlined, PlusOutlined, DeleteOutlined} from "@vicons/antd"
import TableOperationAreaButtonGroup from "@/components/TableOperationAreaButtonGroup.vue";

const {proxy} = getCurrentInstance()
const dialog = useDialog()
const message = useMessage()


onMounted(() => {
  proxy.$axios.get("/api/account/", {}).then(r => {
    if (r.status === 200) {
      const content = r.data
      if (content["code"] === "10000") {
        const data = content["data"]
        let result = [];
        data.map((item) => {
          result.push({
            "key": item["username"],
            "name": item["name"],
            "username": item["username"],
            "group": item["group"],
            "arch_group": item["arch_group"],
            "phone": item["phone"],
            "email": item["email"],
            "sex": item["sex"],
            "create_time": item["create_time"],
            "update_time": item["update_time"]
          })
        });
        members.value = result;
      }
    } else {
      console.error(r.status)
    }
  }).catch(e => {
    console.error(e);
  })
})

let memberName = ref("");
let memberUid = ref(null);
let memberGroup = ref("");
let memberPhone = ref("");
let memberEmail = ref("");
let addMemberName = ref();
let addMemberUid = ref();
let addMemberPhone = ref();
let addMemberEmail = ref();
let addMemberArchGroup = ref();
let memberSexSelectOptionValue = ref()
let addMemberSexSelectOptionValue = ref()
let addMemberGroupSelectOptionValue = ref()
let memberGroupSelectOptions = ref([])
let memberArchGroup = ref("");
let isShowAddModal = ref(false);
let isShowModifyModal = ref(false);
let isShowDetailModal = ref(false);
let isShowDeleteModal = ref(false);
let checkedRowKeysRef = ref([])
let detailTitleValue = ref()
let detailNameValue = ref()
let detailGroupValue = ref()
let detailSexValue = ref()
let detailPhoneValue = ref()
let detailEmailValue = ref()
let detailArchGroupValue = ref()
let detailCreateTime = ref()
let detailUpdateTime = ref()
let modifyTitleValue = ref()
let modifyNameValue = ref()
let modifyGroupValue = ref()
let modifySexValue = ref()
let modifyPhoneValue = ref()
let modifyEmailValue = ref()
let modifyArchGroupValue = ref()
let modifyUidValue = ref(null)

function setUidValue(uid) {
  modifyUidValue.value = uid
}

function getGroups() {
  proxy.$axios.get("/api/group/", {}).then(r => {
    if (r.status === 200) {
      const content = r.data
      if (content["code"] === "10000") {
        const data = content["data"]
        let result = [];
        data.map((item) => {
          result.push({
            "label": item["name"],
            "value": item["name"],
          })
        });
        memberGroupSelectOptions.value = result;
      } else {
      }
    } else {
      console.error(r.status)
    }
  }).catch(e => {
    console.error(e);
  })
}

function handleCheck(rowKeys) {
  checkedRowKeysRef.value = rowKeys;
}

function onAddModalAfterLeave() {
  addMemberName.value = ""
  addMemberUid.value = ""
  addMemberSexSelectOptionValue.value = null
  addMemberGroupSelectOptionValue.value = null
  addMemberPhone.value = ""
  addMemberEmail.value = ""
  addMemberArchGroup.value = ""
}

function onModifyModalAfterLeave() {
  modifyNameValue.value = ""
  modifyGroupValue.value = null
  modifySexValue.value = null
  modifyPhoneValue.value = ""
  modifyEmailValue.value = ""
  modifyArchGroupValue.value = ""
}

function onDetailModalAfterLeave() {

}

function onAddModalOk() {
  isShowAddModal.value = true;
  if (addMemberName.value && addMemberUid.value && addMemberGroupSelectOptionValue.value &&
      addMemberSexSelectOptionValue.value && addMemberPhone.value && addMemberEmail.value &&
      addMemberArchGroup.value) {
    proxy.$axios.post("/api/account/", {
      name: addMemberName.value,
      uid: addMemberUid.value,
      group: addMemberGroupSelectOptionValue.value,
      sex: addMemberSexSelectOptionValue.value,
      phone: addMemberPhone.value,
      email: addMemberEmail.value,
      arch_group: addMemberArchGroup.value
    }).then(r => {
      if (r.status === 200) {
        const content = r.data
        if (content["code"] === "10000") {
          const data = content["data"]
          data.map((item) => {
            members.value.push({
              "key": item["username"],
              "name": item["name"],
              "username": item["username"],
              "group": item["group"],
              "arch_group": item["arch_group"],
              "phone": item["phone"],
              "email": item["email"],
              "sex": item["sex"],
              "create_time": item["create_time"],
              "update_time": item["update_time"]
            })
          });
        }
        message.success("添加成功")
      } else {
        console.error(r.status)
      }
      addMemberName.value = ""
      addMemberUid.value = ""
      addMemberSexSelectOptionValue.value = null
      addMemberGroupSelectOptionValue.value = null
      addMemberPhone.value = ""
      addMemberEmail.value = ""
      addMemberArchGroup.value = ""
    }).catch(e => {
      console.error(e);
    })
  } else {
    message.error("添加失败, 请填入相关信息")
  }
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
  isShowModifyModal.value = true;
  if (modifyUidValue.value === null) {
    message.error("获取工号失败")
  } else if (!modifyNameValue.value && !modifyGroupValue.value && !modifySexValue.value &&
      !modifyPhoneValue.value && !modifyEmailValue.value && !modifyArchGroupValue.value) {
    message.error("修改失败, 请填入相关信息")
  } else {
    proxy.$axios.put(`/api/account/${modifyUidValue.value}`, {
      name: modifyNameValue.value,
      group: modifyGroupValue.value,
      sex: modifySexValue.value,
      phone: modifyPhoneValue.value,
      email: modifyEmailValue.value,
      arch_group: modifyArchGroupValue.value,
    }).then(r => {
      if (r.status === 200) {
        // 获得响应体中的数据
        const content = r.data
        if (content["code"] === "10000") {
          // 从响应体数据中获取状态码匹配
          const data = content["data"]
          data.map((item) => {
            members.value.find(({key}) => key === item["username"]).update_time = item["update_time"]
            members.value.find(({key}) => key === item["username"]).name = item["name"];
            members.value.find(({key}) => key === item["username"]).group = item["group"];
            members.value.find(({key}) => key === item["username"]).sex = item["sex"];
            members.value.find(({key}) => key === item["username"]).phone = item["phone"];
            members.value.find(({key}) => key === item["username"]).email = item["email"];
            members.value.find(({key}) => key === item["username"]).arch_group = item["arch_group"];
          })
        }
        message.success("修改成功")
      } else {
        message.error("修改失败")
      }
      modifyNameValue.value = ""
      modifyGroupValue.value = null
      modifySexValue.value = null
      modifyPhoneValue.value = ""
      modifyEmailValue.value = ""
      modifyArchGroupValue.value = ""
    }).catch(e => {
      console.error(e);
    })
  }
}


function handleSearchButtonClicked() {
  if (memberUid.value !== null) {
    proxy.$axios.get(`/api/account/${memberUid.value}`).then(r => {
      if (r.status === 200) {
        const content = r.data
        if (content["code"] === "10000") {
          const data = content["data"]
          let result = [];
          data.map((item) => {
            result.push({
              "key": item["username"],
              "name": item["name"],
              "username": item["username"],
              "group": item["group"],
              "arch_group": item["arch_group"],
              "phone": item["phone"],
              "email": item["email"],
              "sex": item["sex"],
              "create_time": item["create_time"],
              "update_time": item["update_time"]
            })
          });
          members.value = result;
        }
      } else {
        message.error("检索失败，工号对象不存在，请重新搜索")
        console.error(r.status)
      }
    }).catch(e => {
      console.error(e);
    })
  } else {
    proxy.$axios.get("/api/account/", {
      params: {
        name: memberName.value,
        group: memberGroup.value,
        phone: memberPhone.value,
        email: memberEmail.value,
        sex: memberSexSelectOptionValue.value,
        arch_group: memberArchGroup.value
      }
    }).then(r => {
      if (r.status === 200) {
        const content = r.data
        if (content["code"] === "10000") {
          const data = content["data"]
          let result = [];
          data.map((item) => {
            result.push({
              "key": item["username"],
              "name": item["name"],
              "username": item["username"],
              "group": item["group"],
              "arch_group": item["arch_group"],
              "phone": item["phone"],
              "email": item["email"],
              "sex": item["sex"],
              "create_time": item["create_time"],
              "update_time": item["update_time"]
            })
          });
          members.value = result;
        }
      } else {
        console.error(r.status)
      }
    }).catch(e => {
      console.error(e);
    })
  }
}

function handleAddButtonClicked() {
  isShowAddModal.value = true;
  addMemberSexSelectOptionValue.value = []
  addMemberGroupSelectOptionValue.value = []
  getGroups()
}

function handleBatchDeleteButtonClicked() {
  const deleteContent = "即将删除 " + checkedRowKeysRef.value.length + " 个条目"
  const emptyContent = "请选中条目后再进行删除"
  checkedRowKeysRef.value.length === 0 ?
      dialog.warning({
        title: "批量删除",
        content: emptyContent,
        negativeText: "取消",
      }) :
      dialog.warning({
        title: "批量删除",
        content: deleteContent,
        positiveText: "确定",
        negativeText: "取消",
        onPositiveClick: () => {
          proxy.$axios.delete("/api/account/", {
            data: checkedRowKeysRef.value
          }).then(r => {
            if (r.status === 200) {
              const content = r.data
              if (content["code"] === "10000") {
                // 从响应体数据中获取状态码匹配
                const data = content["data"]
                let result = [];
                data.map((item) => {
                  result.push({
                    "key": item["username"],
                    "name": item["name"],
                    "username": item["username"],
                    "group": item["group"],
                    "arch_group": item["arch_group"],
                    "phone": item["phone"],
                    "email": item["email"],
                    "sex": item["sex"],
                    "create_time": item["create_time"],
                    "update_time": item["update_time"]
                  })
                });
                members.value = result;
              }
              message.success("删除成功")
            } else {
              message.error("删除失败")
            }
            checkedRowKeysRef.value = [];
          })
        }
      })
}

function handleClearSearchContent() {
  memberUid.value = ""
  memberName.value = ""
  memberGroup.value = ""
  memberPhone.value = ""
  memberEmail.value = ""
  memberSexSelectOptionValue.value = null
  memberArchGroup.value = ""
}


const sexSelectOptions = [
  {
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


let members = ref([]);

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
  key: "username",
  width: 150
}, {
  title: "组",
  key: "group",
  width: 200,
  fixed: "left"
}, {
  title: "手机号码",
  key: "phone",
  width: 150
}, {
  title: "工作邮箱",
  key: "email",
  width: 220
}, {
  title: "性别",
  key: "sex",
  width: 100
}, {
  title: "组织架构",
  key: "arch_group",
  resizable: true,
}, {
  title: "创建时间",
  key: "create_time",
  width: 200
}, {
  title: "最后一次修改时间",
  key: "update_time",
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
            detailTitleValue.value = row.username + " 的详细信息"
            detailNameValue.value = row.name
            detailGroupValue.value = row.group
            detailSexValue.value = row.sex
            detailPhoneValue.value = row.phone
            detailEmailValue.value = row.email
            detailArchGroupValue.value = row.arch_group
            detailCreateTime.value = row.create_time
            detailUpdateTime.value = row.update_time
          },
          onModifyButtonClicked: () => {
            isShowModifyModal.value = true;
            getGroups()
            setUidValue(row.key)
            modifyTitleValue.value = "修改 " + row.username + " 成员"
          },
          onDeleteButtonClicked: () => {
            isShowDeleteModal.value = true
            dialog.warning({
              title: "执行删除",
              content: "即将删除 " + row.key + " 成员!",
              positiveText: "确定",
              negativeText: "取消",
              onPositiveClick: () => {
                proxy.$axios.delete(`/api/account/${row.key}`).then(r => {
                  if (r.status === 200) {
                    const content = r.data
                    if (content["code"] === "10000") {
                      // 从响应体数据中获取状态码匹配
                      const data = content["data"]
                      if (data.length === 0) {
                        members.value.splice(members.value.findIndex(({key}) => key === row.key), 1)
                      }
                    }
                    message.success("删除成功")
                  } else {
                    message.error("删除失败")
                  }
                  checkedRowKeysRef.value = [];
                })
              }
            })
          },
        }
    );
  },
  fixed: "right",
  width: 150
},
];

const pagination = reactive({
  page: 1,
  pageSize: 10,
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