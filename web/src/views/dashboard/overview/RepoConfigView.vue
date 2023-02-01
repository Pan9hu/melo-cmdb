<template>
  <div class="repo-config-view">
    <n-page-header>
      <template #header>
        <n-breadcrumb>
          <n-breadcrumb-item>概览</n-breadcrumb-item>
          <n-breadcrumb-item>存储库与配置</n-breadcrumb-item>
        </n-breadcrumb>
      </template>
    </n-page-header>
    <n-data-table striped :columns="columns" :data="members" :pagination="pagination"/>
    <div style="width: 100%; min-height: 20px;"> </div>
  </div>
</template>

<script setup>
import {h, reactive, ref} from "vue";
import {NButton, NTag} from "naive-ui";
import {SearchOutlined,CloseOutlined} from "@vicons/antd"

let members = ref([]);
let columns = [];

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
.repo-config-view{
  display: flex;
  flex-direction: column;
  width: 100%;
  height: 100%;
}
</style>
