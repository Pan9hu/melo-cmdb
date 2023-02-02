<template>
  <div class="vcs-view">
    <n-page-header>
      <template #header>
        <n-breadcrumb>
          <n-breadcrumb-item>配置</n-breadcrumb-item>
          <n-breadcrumb-item>版本控制</n-breadcrumb-item>
        </n-breadcrumb>
      </template>
    </n-page-header>
    <n-card >
    <n-steps :current="currentStepIndex" :status="currentStepStatus">
      <n-step
          title="存储库"
          description="选择一个 Git 存储库并设置分支与提交版本。"
      />
      <n-step
          title="目录"
          description="设置一个指定的配置目录来存放远程的配置数据。"
      />
      <n-step
          title="机器或群组"
          description="更新任意数量的机器或者群组的配置数据。"
      />
      <n-step
          disabled
          title="执行"
          description="在这里提交任务, 设置WebHook 通知, 查看进度, 甚至可以置入后台并开始新的同步任务。"
      />
      <n-step
          disabled
          title="完成"
          description="结果页。"
      />
    </n-steps>
    </n-card>
    <router-view @update-step-index="setCurrentStepIndex" @update-step-status="setCurrentStepStatus" style="width: 100%; height: 100%;"/>
    <div style="width: 100%; min-height: 20px;" ></div>
  </div>
</template>

<script setup>

import {ref} from "vue";

let currentStepIndex = ref(1);
let currentStepStatus = ref("process") // 'process' | 'finish' |'error' |'wait'

function setCurrentStepIndex(index){
  currentStepIndex.value = index;
}
function setCurrentStepStatus(status){
  currentStepStatus.value = status;
}


</script>

<style scoped>

.vcs-view {
  display: flex;
  flex-direction: column;
  width: 100%;
  height: 100%;
}
</style>
