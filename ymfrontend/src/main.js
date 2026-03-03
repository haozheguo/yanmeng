import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'
import axios from 'axios'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import './assets/main.css'

axios.defaults.baseURL = 'http://127.0.0.1:8000'

const app = createApp(App)

// 本地媒体文件基本路径
app.config.globalProperties.$baseImgUrl = 'http://127.0.0.1:8000/media/'

app.use(createPinia())
app.use(router,axios)
app.use(ElementPlus)

app.mount('#app')
