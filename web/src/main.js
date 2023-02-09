import {createApp} from 'vue'
import {createPinia} from 'pinia'
import axios from "axios";


import App from './App.vue'
import router from './router'

import naive from 'naive-ui'

const app = createApp(App)

// TODO 自动判断生成环境和开发环境

app.config.globalProperties.$axios = axios.create({
    baseURL: "http://localhost:5000"
})

app.use(naive)
app.use(createPinia())
app.use(router)


app.mount('#app')
