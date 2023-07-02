import {createApp,} from 'vue'
import {createPinia} from 'pinia'
import axios from "axios";
import App from './App.vue'
import router from './router'
import naive from 'naive-ui'

const app = createApp(App)


// app.config.globalProperties.$axios = axios.create({
//     baseURL: "http://localhost:5000"
// })
//判断环境选择模式
if (import.meta.env.MODE === "development") {
    app.config.globalProperties.$axios = axios.create({
        timeout: 3000

    })
} else {
    app.config.globalProperties.$axios = axios.create({
        baseURL: import.meta.env.VITE_API,
        timeout: 3000
    })
}

app.config.globalProperties.$axios.interceptors.request.use(function (config) {
    if (!localStorage.getItem("access_token") &&
        !localStorage.getItem("refresh_token") &&
        !localStorage.getItem("username")) {
        return config
    } else {
        config.headers["X-Auth-Token"] = JSON.stringify({
            "access": localStorage.getItem("access_token"),
            "refresh": localStorage.getItem("refresh_token"),
            "username": localStorage.getItem("username")
        })
    }
    return config
})


app.use(naive)
app.use(createPinia())
app.use(router)
app.mount('#app')
