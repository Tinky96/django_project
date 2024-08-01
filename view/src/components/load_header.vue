<template>
    <!-- 加载 -->
    <div v-if="isloading" class="loader-wrapper">
        <div class="loader"></div>
        <div class="loder-section left-section"></div>
        <div class="loder-section right-section"></div>
    </div>
    <!-- 顶栏 -->
    <div :class="{ sticky: isSticky }" class="cyber-security_nav_manu" v-show="showNavbar">
        <div class="container">
            <div class="row up align-items-center">
                <div class="col-lg-2">
                    <div class="header-button">
                        <a href="#" @click="showLoginModal">登录</a>
                    </div>
                </div>
                <div class="col-lg-3">
                    <el-input v-model="message" placeholder="输入" class="input-with-select">

                        <template #append>
                            <el-button icon="Search" @click="search(message)" />
                        </template>
                    </el-input>
                </div>
                <div class="col-lg-7">
                    <nav class="cyber-security_menu">
                        <ul class="nav_scroll">
                            <li><a href="/">主页</a></li>
                            <li><a href="" @click="goToCart(event)">购物车</a></li>
                            <li>
                                <a href="upon_goods" @click="checkLoginAndRedirect">我要上传</a>
                            </li>
                            <li>
                                <a href="" @click="goToUserPage(event)">用户主页</a>
                            </li>
                            <li>

                                <a href="#">关于
                                    <span><i class="bi bi-chevron-down"></i></span></a>
                                <ul class="sub-menu">
                                    <!-- <li><a href="{% url 'user' %}">关于</a></li> -->
                                    <li>
                                        <a href="/about">关于我们</a>
                                    </li>
                                    <li><a href="faq.html">Faq</a></li>
                                </ul>
                            </li>
                        </ul>
                    </nav>
                </div>
            </div>
        </div>
    </div>
    <!-- 登录框 -->
    <div v-if="showModal" class="login-container">
        <span class="close-btn" @click="closeLoginModal">x</span>
        <form>
            <input type="text" placeholder="Username" v-model="username" />
            <input type="password" placeholder="Password" v-model="password" />

            <el-button type="primary" @click="login($event)">登录</el-button>
            <router-link to="/user_register">
                <el-button type="primary">注册</el-button>
            </router-link>

            <!-- <button @click="login($event)">Login</button> -->

        </form>
    </div>
</template>

<script>
export default {
    computed: {
        counter() {
            return this.counterValue;
        },
    },
    created() {
        // 检查用户的登录状态
        const isLoggedIn = localStorage.getItem("isLoggedIn");
        if (isLoggedIn && isLoggedIn === "true") {
            this.is_login = true;
            const userID = localStorage.getItem("userId");
            this.user_name = userID.substring(0, 3);
            // this.handleLoggedIn();
        } else {
            this.is_login = false;
        }
    },
    data() {
        return {
            username: "",
            password: "",
            isSticky: false,
            showNavbar: false,
            isloading: true,
            showModal: false,
            message: "",
        };
    },
    mounted() {
        setTimeout(() => {
            this.isloading = false; // 加载完成后将 isloading 设置为 false
            this.showNavbar = true;
        }, 2000);

        window.addEventListener("scroll", this.handleScroll);
    },
    beforeUnmount() {
        window.removeEventListener("scroll", this.handleScroll);
    },
    methods: {
        // 显示登录框
        search(message) {
            this.$router.push({ path: "/search_goods", query: { message } });
        },
        showLoginModal() {
            this.showModal = true;
        },
        // 关闭登录框
        closeLoginModal() {
            this.showModal = false;
        },
        // 滚动显示顶栏
        handleScroll() {
            const scroll = window.scrollY;
            if (scroll < 100) {
                this.isSticky = false;
            } else {
                this.isSticky = true;
            }
        },
        //登录
        login(event) {
            event.preventDefault();
            this.$axios
                .post("/api/login/", {
                    username: this.username,
                    password: this.password,
                })
                .then((response) => {
                    const data = response.data;
                    alert(data.status);
                    if (data.status) {
                        alert("登陆成功");
                        localStorage.setItem("userToken", data.token);
                        // 将用户设为已登陆
                        localStorage.setItem("isLoggedIn", true);
                        // 保存用户ID
                        localStorage.setItem("userId", data.user_id);
                        // location.reload();
                    } else {
                        alert("登陆失败");
                    }
                })
                .catch((error) => {
                    // 处理错误响应
                    alert("请求错误:", error);
                });
        },
        goToUserPage() {
            const userId = localStorage.getItem("userId");
            this.$router.push({ path: "/self_message", query: { userId } });
        },
        goToCart() {
            const userId = localStorage.getItem("userId");
            this.$router.push({ path: "/goods_cart", query: { userId } });
        },
    },
};
</script>

<style scoped>
@import "@/assets/css/bootstrap.min.css";
@import "@/assets/css/owl.carousel.min.css";
@import "@/assets/css/animate.css";
@import "@/assets/css/animated-text.css";
@import "@/assets/css/all.min.css";
@import "@/assets/css/flaticon.css";
@import "@/assets/css/theme-default.css";
@import "@/assets/css/meanmenu.min.css";
@import "@/assets/css/owl.transitions.css";
@import "@/assets/css/venobox.css";
@import "@/assets/css/bootstrap-icons.css";
@import "@/assets/css/style.css";
@import "@/assets/css/responsive.css";

/* @import '@/assets/css/scrollCue.css';  */
@import "@/assets/css/login.css";
</style>
