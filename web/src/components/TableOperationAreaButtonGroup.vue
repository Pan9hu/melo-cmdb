<template>
  <div class="table-operation-area-button-group">
    <n-button strong secondary size="tiny" style="margin-right: 5px" v-if="props.isShowDetail"
              @click="onDetailButtonClicked" type="info">详情
    </n-button>
    <n-button strong secondary size="tiny" style="margin-right: 5px" v-if="props.isShowModify"
              @click="onModifyButtonClicked" type="warning">修改
    </n-button>
    <n-button strong secondary size="tiny" style="margin-right: 5px" v-if="props.isShowDelete"
              @click="onDeleteButtonClicked" type="error" >删除
    </n-button>
  </div>
</template>

<script setup>
const props = defineProps({
  isShowDetail: Boolean,
  isShowModify: Boolean,
  isShowDelete: Boolean,
  onDetailButtonClicked: Function,
  onModifyButtonClicked: Function,
  onDeleteButtonClicked: Function,

})

</script>

<style scoped>
.table-operation-area-button-group {
  height: 100%;
  width: 100%;
  display: flex;
  justify-content: left;
}
</style>
