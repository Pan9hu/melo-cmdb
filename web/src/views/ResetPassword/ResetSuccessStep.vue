<template>
  <div class="reset-success-step-view">
    <div
        style="width: 100%;height: 100%;display: flex;flex-direction: column;align-items: center">
      <n-card style="width: 26%;height: 29%;display: flex;flex-direction: column;">
        <div class="step-form-content">
          <div style="margin-bottom: 25px;">
            <div class="step-form-content">
              <n-alert title="处理中" type="info" :bordered="false" v-if="gitRepoCheckStatus === 'doing'">
                正在检验新密码是否可用。
              </n-alert>
              <n-alert title="成功！" type="success" :bordered="false" v-if="gitRepoCheckStatus === 'ok'">
                新登录密码重置成功, 请重新登录。
              </n-alert>
              <n-alert title="" type="error" :bordered="false" v-if="gitRepoCheckStatus === 'false'">
                遗憾, 新密码不可用请重新设置。
              </n-alert>
            </div>

          </div>
        </div>
        <div class="step-op-area">
          <n-button strong style="margin-right: 10px;" @click="handleToAuthSteButtonClicked"
                    :loading="ButtonLoading">重&nbsp;设&nbsp;密&nbsp;码&nbsp;
          </n-button>
          <n-button strong type="primary" @click="handleToLoginViewButtonClicked">重&nbsp;新&nbsp;登&nbsp;录</n-button>

        </div>
      </n-card>
    </div>
  </div>
</template>

<script setup>

import {useRouter} from "vue-router";
import {onMounted, ref} from "vue";
import {useMessage} from 'naive-ui'

const message = useMessage()
const router = useRouter()
const numberAnimationInstRef = ref(null)
const emit = defineEmits(["update-step-index", "update-step-status"])

let gitRepoCheckStatus = ref('ok');
let ButtonLoading = ref(false)

function handleToLoginViewButtonClicked() {
  router.push({
    path: '/Login'
  });
}


function handleToAuthSteButtonClicked() {
  router.push({
    path: '/reset-password/authentication-step'
  });
}

onMounted(() => {
  emit('update-step-index', 3)
  numberAnimationInstRef.value?.play()
})


</script>

<style scoped>
.reset-success-step-view {
  display: flex;
  flex-direction: column;
  width: 100%;
  height: 100%;
}

.step-form-content {
  flex: 1;
  display: flex;
  flex-direction: column;

}

.step-op-area {
  display: flex;
  justify-content: center;
}
</style>