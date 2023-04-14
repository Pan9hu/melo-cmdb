<template>
  <div class="authentication-step-view">
    <div
        style="width: 100%;height: 100%;display: flex;flex-direction: column;align-items: center">
      <n-card style="width: 26%;height: 60%;display: flex;flex-direction: column;">
        <div class="step-form-content">
          <div style="margin-bottom: 25px;">
            <div style="font-size: 13pt; margin-bottom: 10px;">账号:</div>
            <n-input style="width: 500px;" type="text" placeholder="请输入你要重置密码的账号"/>
          </div>
          <div style="margin-bottom: 25px;">
            <div style="font-size: 13pt; margin-bottom: 10px;">验证方式:</div>
            <n-select v-model:value="AuthenticationOptionValue" :options="AuthenticationOptions"
                      placeholder="请选择电子邮箱或手机号的方式验证"/>
          </div>
          <div style="margin-bottom: 25px;">
            <div style="font-size: 13pt; margin-bottom: 10px;">验证码:</div>
            <n-input style="width: 500px;" type="text" placeholder="请输入你获取的验证码"/>
          </div>
        </div>
        <div class="step-op-area">
          <n-button strong style="margin-right: 10px;">返&nbsp;回&nbsp;登&nbsp;录</n-button>
          <n-button strong type="primary" @click="handleStepNextButtonClicked" :loading="nextButtonLoading">下&nbsp;一&nbsp;步</n-button>
        </div>
      </n-card>
    </div>
  </div>
</template>

<script setup>

import {useRouter} from "vue-router";
import {onMounted, ref} from "vue";

const router = useRouter()

const emit = defineEmits(["update-step-index", "update-step-status"])

const AuthenticationOptions = [
  {
    label: "电子邮箱",
    value: "email"
  }, {
    label: "手机号",
    value: "phone"
  }
]

let AuthenticationOptionValue = ref();
let nextButtonLoading = ref(false)

function handleStepNextButtonClicked() {
  router.push({
    path: '/reset-password/reset-step'
  });
}

onMounted(() => {
  emit('update-step-index', 1)
})

</script>

<style scoped>
.authentication-step-view {
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
