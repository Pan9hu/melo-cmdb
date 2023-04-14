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
      <div class="image">
        <img src="../assets/image/melo.svg" alt="">
      </div>
      <div class="title">登录 Melo CMDB</div>
      <div class="box">
        <n-input v-model:value="username" type="text" placeholder="请输入用户名"/>
      </div>
      <div class="box">
        <n-input v-model:value="password" type="password" show-password-on="click"
                 @keyup.enter="handleLoginButtonClicked" placeholder="请输入登录密码"/>
      </div>
      <div class="text-box">
        <div class="about-text" @click="handleAboutLinkClicked">关于 Melo CMDB</div>
        <div class="forget-password" @click="handleResetPasswordClicked" >忘记密码? 点击找回</div>
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
import {getCurrentInstance, onMounted, ref} from 'vue';
import {useRouter} from 'vue-router';
import {useMessage} from "naive-ui";

const router = useRouter()
const {proxy} = getCurrentInstance()
const message = useMessage()

let username = ref("");
let password = ref("");
let loginButtonLoadingStatus = ref(false)


onMounted(() => {
  if (localStorage.access_token && localStorage.username){
    router.push({
      path: '/dashboard'
    })
  }
  document.title = "登录 Melo CMDB"
})

function handleLoginButtonClicked() {
  if (!username.value && !password.value) {
    message.error("登录失败, 请输入账号密码!")
  } else if (username.value && !password.value) {
    message.warning("登录失败, 请输入密码!")
  } else if (!username.value && password.value) {
    message.warning("登录失败, 请输入账号!")
  } else {
    proxy.$axios.post("/api/auth/login", {
      username: username.value,
      password: btoa(encodeURIComponent(password.value))
    }).then(r => {
      if (r.status === 200) {
        const content = r.data
        if (content["code"] === "10000") {
          sessionStorage.clear()
          localStorage.clear()
          localStorage.access_token = content.data.access_token
          localStorage.refresh_token = content.data.refresh_token
          localStorage.username = content.data.username
          router.push({
            path: '/dashboard'
          })
        } else if (content["code"] === "20000") {
          message.error("用户不存在, 请重新输入")
        }else {
          message.error("密码错误, 请重新输入")
        }
      }
    })
  }
}

function handleAboutLinkClicked() {
  router.push({
    path: '/about'
  })
}

function handleResetPasswordClicked(){
  router.push({
    path: '/reset-password'
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

.image {
  display: flex;
  width: 20%;
  height: 20%;
  position: absolute;
  left: 0;
  bottom: 0;
}
</style>
