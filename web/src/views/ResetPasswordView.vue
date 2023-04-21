<template>
  <n-watermark
      content="欢迎使用 Melo CMDB"
      cross
      fullscreen
      :font-size="16"
      :line-height="16"
      :width="384"
      :height="384"
      :x-offset="12"
      :y-offset="60"
      :rotate="-15"
  />
    <n-layout class="reset-password-view" >
      <div
          style="width: 100%;height: 100%;display: flex;flex-direction: column;justify-content: center;align-items: center">
        <div class="title">重置密码</div>
        <n-card style="width: 26%;height: 10%;display: flex;flex-direction: column;">
          <n-steps style="display: flex;width: 100%;height: 100%; justify-content: center" :current="currentStepIndex"
                   :status="currentStepStatus">
            <n-step
                title="身份验证"
                description="账号信息核对"
            />
            <n-step
                title="密码重置"
                description="用户密码重置"
            />
            <n-step
                title="重置完成"
                description="用户密码重置成功"
            />
          </n-steps>
        </n-card>
        <router-view @update-step-index="setCurrentStepIndex" @update-step-status="setCurrentStepStatus"
                     style="width: 100%; height: 100%;"/>
      </div>
    </n-layout>
    <div class="image">
      <img src="../assets/image/melo.svg" alt="">
    </div>
</template>

<script setup>
import {getCurrentInstance, onMounted, ref} from 'vue';
import {useRouter} from "vue-router";
import {useMessage} from "naive-ui";

onMounted(() => {
  document.title = "重置密码"
})
const router = useRouter()
const {proxy} = getCurrentInstance()
const message = useMessage()


let username = ref("");
let password = ref("");
let currentStepIndex = ref(1);
let currentStepStatus = ref("process") // 'process' | 'finish' |'error' |'wait'


function setCurrentStepIndex(index) {
  currentStepIndex.value = index;
}

function setCurrentStepStatus(status) {
  currentStepStatus.value = status;
}

</script>


<style scoped>


.title {
  font-size: 20pt;
  text-align: center;
  margin-bottom: 25px;
  margin-top: 10%;

}

.image {
  display: flex;
  width: 20%;
  height: 20%;
  position: absolute;
  left: 0;
  bottom: 0;
}

.reset-password-view {
  display: flex;
  flex-direction: column;
  justify-content: center;
  width: 100%;
  height: 100%;
}
</style>