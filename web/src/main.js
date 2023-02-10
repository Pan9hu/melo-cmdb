import {createApp} from 'vue'
import {createPinia} from 'pinia'
import axios from "axios";


import App from './App.vue'
import router from './router'
import naive from 'naive-ui'

const app = createApp(App)

// app.config.globalProperties.$axios = axios.create({
//     baseURL: "http://localhost:5000"
// })
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

app.use(naive)
app.use(createPinia())
app.use(router)


app.mount('#app')
