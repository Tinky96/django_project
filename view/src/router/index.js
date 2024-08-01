import { createRouter, createWebHistory } from 'vue-router'
// import axios from 'axios';
import index_goods from '@/components/index_goods.vue'
import user_register from '@/components/user_register.vue'
import upon_goods from '@/components/upon_goods.vue'
import buy_goods from '@/components/buy_goods.vue'
import search_goods from '@/components/search_goods.vue'
import self_message from '@/components/self_message.vue'
import goods_cart from '@/components/goods_cart.vue'
import about_us from '@/components/about_us.vue'
// import { create } from 'core-js/core/object'

// 配置组件及路径对应关系
const routes = [
    {
        path: '/',
        component: index_goods
    },
    {
        path: '/index_goods',
        component: index_goods
    },
    {
        path: '/user_register',
        component: user_register
    },
    {
        path: '/upon_goods',
        component: upon_goods
    },
    {
        path: '/buy_goods',
        component: buy_goods
    },
    {
        path: '/search_goods',
        component: search_goods
    },
    {
        path: '/self_message',
        component: self_message,
    },{
        path: '/goods_cart',
        component: goods_cart,
    },{
        path: '/about_us',
        component: about_us,
    },
]
const router = createRouter({
    history: createWebHistory(),
    routes
});

export default router // 导出路由配置