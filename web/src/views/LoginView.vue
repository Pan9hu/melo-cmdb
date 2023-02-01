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
  <n-layout class="login-view">
    <div
        style="width: 100%;height: 100%;display: flex;flex-direction: column;justify-content: center;align-items: center">
      <div class="title">登录 Melo CMDB</div>
      <div class="box">
        <n-input v-model:value="username" type="text" placeholder="请输入用户名"/>
      </div>
      <div class="box">
        <n-input v-model:value="password" type="text" placeholder="请输入登录密码"/>
      </div>
      <div class="text-box">
        <div class="about-text" @click="handleAboutLinkClicked">关于 Melo CMDB</div>
        <div class="forget-password">忘记密码? 点击找回</div>
      </div>
      <div class="box">
        <n-button @click="handleLoginButtonClicked" type="primary" strong secondary style="width: 100%;"
                  :loading="loginButtonLoadingStatus">进&nbsp;入&nbsp;系&nbsp;统
        </n-button>
      </div>
    </div>
  </n-layout>
</template>

<script setup>
import {onMounted, ref} from 'vue';
import {useRouter} from 'vue-router';

const router = useRouter()


let username = ref("");
let password = ref("");
let loginButtonLoadingStatus = ref(false)


onMounted(() => {
  document.title = "登录 Melo CMDB"
})


function handleLoginButtonClicked() {
  router.push({
    path: '/dashboard'
  })
}

function handleAboutLinkClicked() {
  router.push({
    path: '/about'
  })

}

</script>


<style scoped>
.login-view {
  width: 100%;
  height: 100%;
}

.title {
  font-size: 20pt;
  text-align: center;
  margin-bottom: 25px;
}

.box {
  width: 350px;
  margin-top: 10px;
}

.text-box {
  font-size: 9pt;
  text-align: right;
  margin-top: 35px;
  width: 350px;
  display: flex;
  justify-content: space-between;
}


.forget-password:hover {
  text-decoration-line: underline;
  cursor: pointer;
}

.about-text:hover {
  text-decoration-line: underline;
  cursor: pointer;
}

</style>
