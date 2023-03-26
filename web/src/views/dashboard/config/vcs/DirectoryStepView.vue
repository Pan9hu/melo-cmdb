<template>
  <div class="directory-step-view">
    <n-card style="width: 100%; height: 100%;">
      <div style="width: 100%; height: 100%; display: flex; flex-direction: column; justify-content: flex-end;">
        <div class="step-form-content">
          <div style="margin-bottom: 25px;">
            <div style="font-size: 15pt; margin-bottom: 10px;">同步到:</div>
            <n-input style="width: 100%;" type="text"
                     placeholder="请输入一个目录, 如果目标机器或群组不存在此目录, 那么 Melo CMDB 将会自动创建"/>
          </div>
          <div style="margin-bottom: 25px;">
            <div style="font-size: 15pt;">同步后脚本:</div>
            <div style="font-size: 8pt; margin-bottom: 10px; color: gray ">在每个机器 (或者群组中的机器)
              同步完成执行下面的脚本。
            </div>
            <n-input v-model:value="postSyncScriptContent"
                     style="width: 100%; font-family: 'Source Code Pro',serif;" type="textarea"
                     placeholder="请输入脚本内容" row="20"/>
          </div>
        </div>
        <div class="step-op-area">
          <n-button strong style="margin-right: 10px;">取&nbsp;消</n-button>
          <n-button strong type="primary" @click="handleStepNextButtonClicked">下&nbsp;一&nbsp;步</n-button>
        </div>
      </div>
    </n-card>
  </div>
</template>

<script setup>

import {useRouter} from "vue-router";
import {onMounted, ref} from "vue";

const router = useRouter()

const emit = defineEmits(["update-step-index", "update-step-status"])

let postSyncScriptContent = ref("#!/usr/bin/env bash\n")

function handleStepNextButtonClicked() {
  router.push({
    path: '/dashboard/config/vcs/target-step'
  });
}

onMounted(() => {
  emit('update-step-index', 2)
})


</script>

<style scoped>
.directory-step-view {
  display: flex;
  flex-direction: column;
  width: 100%;
  height: 100%;
  padding-top: 25px;
}

.step-form-content {
  flex: 1;
}

.step-op-area {
  display: flex;
  justify-content: flex-end;
}
</style>