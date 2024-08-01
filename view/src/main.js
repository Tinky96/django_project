import { createApp } from 'vue'  
import App from './App.vue'  
import ElementPlus from 'element-plus'  
import 'element-plus/theme-chalk/index.css'  
import axios from 'axios'  
import router from './router/index.js'  
import 'bootstrap/dist/css/bootstrap.css'  
import animated from "animate.css"  
import * as ElIcon from '@element-plus/icons-vue'  
import {VueMasonryPlugin} from 'vue-masonry'; 

const app = createApp(App)  
app.use(ElementPlus)  
app.use(router)  
app.use(animated)  
app.use(VueMasonryPlugin)  
  
axios.defaults.baseURL = "http://localhost:8000"  
axios.interceptors.request.use(  
  config => {  
    const token = localStorage.getItem('userToken')  
    if (token) {  
      config.headers = config.headers || {}  
      config.headers.common = config.headers.common || {}  
      config.headers.common['Authorization'] = `Bearer ${token}`  
    }  
    return config  
  },  
  error => {  
    return Promise.reject(error)  
  }  
)  


app.config.globalProperties.$axios = axios  
  
Object.keys(ElIcon).forEach((key) => {  
  app.component(key, ElIcon[key])  
})  
  
app.mount('#app');  
