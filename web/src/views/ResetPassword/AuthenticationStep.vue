<template>
  <div class="authentication-step-view">
    <div
        style="width: 100%;height: 100%;display: flex;flex-direction: column;align-items: center">
      <n-card style="width: 26%;height: 60%;display: flex;flex-direction: column;">
        <div class="step-form-content">
          <div style="margin-bottom: 25px;">
            <div style="font-size: 13pt; margin-bottom: 10px;">账号:</div>
            <n-input v-model:value="username" type="text" placeholder="请输入你要重置密码的账号">
              <template #prefix>
                <n-icon :component="UserOutlined"/>
              </template>
            </n-input>
          </div>
          <div style="margin-bottom: 25px;">
            <div style="font-size: 13pt; margin-bottom: 10px;">验证方式:</div>
            <n-select v-model:value="AuthenticationOptionValue" :options="AuthenticationOptions"
                      placeholder="请选择电子邮箱或手机号的方式验证"/>
          </div>
          <div style="margin-bottom: 25px;">
            <div style="font-size: 13pt; margin-bottom: 10px;">验证码:</div>
            <div class="container" style="position: relative">
              <n-input type="text" placeholder="请输入你获取的验证码">
                <template #prefix>
                  <n-icon :component="Email"/>
                </template>
              </n-input>
              <n-button size="small" style="position: absolute;top: 9%;right: 1%;border: none;outline: none;"
                        @click="handleSendSecurityCodeButtonClicked" >获取验证码
              </n-button>
            </div>
          </div>
        </div>
        <div class="step-op-area">
          <n-button strong style="margin-right: 10px;" @click="handleToLoginViewButtonClicked">
            返&nbsp;回&nbsp;登&nbsp;录
          </n-button>
          <n-button strong type="primary" @click="handleStepNextButtonClicked" :loading="nextButtonLoading">下&nbsp;一&nbsp;步</n-button>
        </div>
      </n-card>
    </div>
  </div>
</template>

<script setup>

import {useRouter} from "vue-router";
import {getCurrentInstance, onMounted, ref} from "vue";
import {UserOutlined} from "@vicons/antd";
import {Email} from "@vicons/carbon";

const {proxy} = getCurrentInstance()
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
let username = ref("")

function handleToLoginViewButtonClicked() {
  router.push({
    path: '/Login'
  });
}

function handleStepNextButtonClicked() {
  router.push({
    path: '/reset-password/reset-step'
  });
}

function handleSendSecurityCodeButtonClicked() {
  proxy.$axios.post("/api/auth/security-code",{
    username: username.value,
    auth_method: AuthenticationOptionValue.value
  })
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
