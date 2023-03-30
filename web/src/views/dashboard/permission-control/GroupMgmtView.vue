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
                :options="roleSelectOptions" placeholder="选择检索条件(全部)"/>
      <n-input style="margin-right: 10px;" placeholder="按照组名或者用途搜索, 支持全文检索.." type="text"
               v-model:value="searchLineValue" @keyup.enter="handleSearchButtonClicked"/>
      <n-tooltip placement="top" trigger="hover">
        <template #trigger>
          <n-button secondary tertiary circle style="margin-left: 5px" type="info"
                    @click="handleSearchButtonClicked">
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
    <n-data-table striped :columns="columns" :data="groups" :row-key="rowKey" @update-checked-row-keys="handleCheck"
                  :pagination="pagination"/>
    <n-modal v-model:show="isShowAddModal" :mask-closablef="false" preset="card" title="添加组"
             :on-after-leave="onAddModalAfterLeave" :segmented="false" style="width: 45%; min-width: 600px">
      <div style="display: flex;width: 100%; height: 100%; flex-direction: column">
        <div style="width: 100%; ">
          <div style="font-size: 12pt; font-weight: bold;">名称</div>
          <n-input v-model:value="groupNameTextInput" type="text" placeholder="必填, 请输入组名"
                   style="margin-bottom: 10px; max-width: 200px" @keyup.enter="onAddModalOk"/>
          <div style="font-size: 12pt; font-weight: bold;">用途</div>
          <n-input v-model:value="usageTextInput" type="text" placeholder="请输入用途" @keyup.enter="onAddModalOk"/>
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
          <n-input type="text" placeholder="请输入用途" v-model:value="usageTextInputOne" @keyup.enter="onModifyModalOk"/>
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
import {getCurrentInstance, h, onMounted, reactive, ref} from "vue";
import {NButton, useDialog, useMessage} from "naive-ui";
import {CloseOutlined, DeleteOutlined, PlusOutlined, SearchOutlined} from "@vicons/antd"
import TableOperationAreaButtonGroup from "@/components/TableOperationAreaButtonGroup.vue";


const {proxy} = getCurrentInstance()
const dialog = useDialog()
const message = useMessage()

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
            "update_time": item["update_time"],
            "create_time": item["create_time"],
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
    console.error(e);
  })
})


let groups = ref([])
let checkedRowKeysRef = ref([])
let groupNameTextInput = ref("")
let usageTextInput = ref("")
let usageTextInputOne = ref("")
let roleSelectOptionValue = ref()
let searchLineValue = ref("")
let isShowAddModal = ref(false);
let isShowModifyModal = ref(false);
let isShowDeleteModal = ref(false);
let groupName = ref("")
let roleSelectOptions = [
  {
    label: "全部",
    value: null
  }, {
    label: "组名",
    value: "name"
  }, {
    label: "用途",
    value: "usage"
  },
]


function rowKey(row) {
  return row.key
}

function handleCheck(rowKeys) {
  checkedRowKeysRef.value = rowKeys;
}

function setGroupName(name) {
  groupName.value = name
}

function onAddModalAfterLeave() {
}

function onModifyModalAfterLeave() {
}

function onAddModalOk() {
  isShowAddModal.value = true;
  proxy.$axios.post("/api/group/", {
    name: groupNameTextInput.value,
    usage: usageTextInput.value,
  },).then(r => {
    if (r.status === 200) {
      // 获得响应体中的数据
      const content = r.data
      message.success("添加成功")
        if (content["code"] === "10000"){
          // 从响应体数据中获取状态码匹配
          const data = content["data"]
          data.map((item)=>{
            groups.value.push({
              "key": item["name"],
              "name": item["name"],
              "update_time": item["update_time"],
              "create_time": item["create_time"],
              "usage": item["usage"]
            })
          });
        }
    }
    groupNameTextInput.value = "";
    usageTextInput.value = "";
  }).catch(e => {
    console.error(e);
  })
}

function onAddModalFailed() {
  isShowAddModal.value = false;
}

function onModifyModalFailed() {
  isShowModifyModal.value = false;
}

function onModifyModalOk() {
  isShowModifyModal.value = true;
  proxy.$axios.put(`/api/group/${groupName.value}`, {
    usage: usageTextInputOne.value,
  }).then(r => {
    if (r.status === 200) {
      // 获得响应体中的数据
      const content = r.data
      console.log(content)
      if (content["code"] === "10000") {
        // 从响应体数据中获取状态码匹配
        const data = content["data"]
        data.map((item) => {
          groups.value.find(({key}) => key === item["name"]).update_time = item["update_time"]
          groups.value.find(({key}) => key === item["name"]).usage = item["usage"];
        })
      }
      message.success("修改成功")
    }
    usageTextInputOne.value = "";
  }).catch(e => {
    console.error(e);
  })
}


function handleSearchButtonClicked() {
  if (roleSelectOptionValue.value === "name") {
    proxy.$axios.get(`/api/group/${searchLineValue.value}`,).then(r => {
      if (r.status === 200) {
        const content = r.data
        if (content["code"] === "10000") {
          const data = content["data"]
          let result = [];
          data.map((item) => {
            result.push({
              "key": item["name"],
              "name": item["name"],
              "update_time": item["update_time"],
              "create_time": item["create_time"],
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
      console.error(e);
    })
  } else {
    proxy.$axios.get("/api/group/", {
      params: {
        usage: searchLineValue.value,
      }
    }).then(r => {
      if (r.status === 200) {
        const content = r.data
        if (content["code"] === "10000") {
          const data = content["data"]
          let result = [];
          data.map((item) => {
            result.push({
              "key": item["name"],
              "name": item["name"],
              "update_time": item["update_time"],
              "create_time": item["create_time"],
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
      console.error(e);
    })
  }
}

function handleAddButtonClicked() {
  isShowAddModal.value = true;
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
          const name_list = checkedRowKeysRef.value
          proxy.$axios.delete("/api/group/", {
            data: name_list
          }).then(r => {
            if (r.status === 200) {
              const content = r.data
              if (content["code"] === "10000") {
                // 从响应体数据中获取状态码匹配
                const data = content["data"]
                let result = [];
                data.map((item) => {
                  result.push({
                    "key": item["name"],
                    "name": item["name"],
                    "update_time": item["update_time"],
                    "create_time": item["create_time"],
                    "usage": item["usage"]
                  })
                });
                groups.value = result;
              }
              message.success("删除成功")
            }
            checkedRowKeysRef.value = [""];
          })
        }
      })
}

function handleClearSearchContent() {
  searchLineValue.value = ""
  roleSelectOptionValue.value = null
}


let columns = [
  {
    type: "selection",
    fixed: "left",
  }, {
    title: "组名",
    key: "name",
    fixed: "left",
    width: 250
  }, {
    title: "创建时间",
    key: "create_time",
    width: 200

  }, {
    title: "更新时间",
    key: "update_time",
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
              setGroupName(row.name)
            },
            onDeleteButtonClicked: () => {
              isShowDeleteModal.value = true
              dialog.warning({
                title: "执行删除",
                content: "即将删除 " + row.name + " !",
                positiveText: "确定",
                negativeText: "取消",
                onPositiveClick: () => {
                  proxy.$axios.delete(`/api/group/${row.name}`).then(r => {
                    if (r.status === 200) {
                      const content = r.data
                      if (content["code"] === "10000") {
                        // 从响应体数据中获取状态码匹配
                        const data = content["data"]
                        if (data.length === 0 ){
                          groups.value.splice(groups.value.findIndex(({key}) => key === row.name),1)
                        }
                      }
                    }
                    checkedRowKeysRef.value = [""];
                  })
                  message.success("删除成功")
                }
              })
            },
          }
      );
    },
    fixed: "right",
    width: 150
  },
]

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

.group-mgmt-view {
  display: flex;
  flex-direction: column;
  width: 100%;
  height: 100%;
}
</style>