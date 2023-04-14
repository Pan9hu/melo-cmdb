<template>
  <div class="Reset-step-view">
    <div
        style="width: 100%;height: 100%;display: flex;flex-direction: column;align-items: center">
      <n-card style="width: 26%;height: 44%;display: flex;flex-direction: column;">
        <div class="step-form-content">
          <div style="margin-bottom: 25px;">
            <div style="font-size: 13pt; margin-bottom: 10px;">新密码:</div>
            <n-input  type="password" show-password-on="click" placeholder="请输入新密码">
              <template #prefix>
                <n-icon :component="Password"/>
              </template>
            </n-input>
          </div>
          <div style="margin-bottom: 25px;">
            <div style="font-size: 13pt; margin-bottom: 10px;">再次输入:</div>
            <n-input  type="password" show-password-on="click" placeholder="请再次输入新密码">
              <template #prefix>
                <n-icon :component="Password"/>
              </template>
            </n-input>
          </div>
        </div>
        <div class="step-op-area">
          <n-button strong style="margin-right: 10px;">清&nbsp;空</n-button>
          <n-button strong type="primary" @click="handleStepNextButtonClicked" :loading="nextButtonLoading">下&nbsp;一&nbsp;步</n-button>
        </div>
      </n-card>
    </div>
  </div>
</template>

<script setup>

import {useRouter} from "vue-router";
import {onMounted, ref} from "vue";
import {Password} from "@vicons/carbon";

const router = useRouter()

const emit = defineEmits(["update-step-index", "update-step-status"])

let postSyncScriptContent = ref("#!/usr/bin/env bash\n")
let nextButtonLoading = ref(false)

function handleStepNextButtonClicked() {
  router.push({
    path: '/reset-password/reset-success-step'
  });
}

onMounted(() => {
  emit('update-step-index', 2)
})


</script>

<style scoped>
.Reset-step-view {
  display: flex;
  flex-direction: column;
  width: 100%;
  height: 100%;
}

.step-form-content {
  flex: 1;
}

.step-op-area {
  display: flex;
  justify-content: center;
}
</style>