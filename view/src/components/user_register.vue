<template>
    <load_header></load_header>

    <div class="subscribe-section">
        <div class="container">
            <div class="row subscribe">
                <div class="col-lg-12">
                    <div class="section-title-left text-center" data-cues="slideInUp">
                        <div class="section-title-left text-center" data-cues="slideInUp"></div>
                        <h4>少玩游戏</h4>
                        <h1>没有账号?</h1>
                        <h1>newsletter</h1>
                    </div>
                    <form>
                        <div class="enter-text">
                            <input type="text" name="User" placeholder="账号" v-model="username">
                            <input type="text" name="Mail" placeholder="邮箱" v-model="email">
                            <input type="text" name="PassWord" placeholder="密码" v-model="password">
                            <input type="text" name="rePassWord" placeholder="确认密码" v-model="re_password">
                        </div>
                        <div class="Subcribe-button-2">
                            <button @click="register">注册</button>
                        </div>
                    </form>
                </div>
                <div class="subscribe-shape" data-cues="slideInUp">
                    <img src="../assets/picture/subscribe-shape.png" alt="shape">
                </div>
            </div>
        </div>
    </div>

</template>

<script>
import load_header from './load_header.vue'
export default {
    components: {
        load_header
    },
    data() {
        return {
            username: '',
            password: '',
            email: '',
            re_password: '',
        };
    },
    computed: {
        counter() {
            return this.counterValue;
        }
    },
    methods: {
        register() {
            if (this.password == this.re_password) {

                this.$axios.post('/api/register/', { "username": this.username, "password": this.password, "email": this.email })
                    .then(response => {
                        const data = response.data;
                        if (data.status) {
                            localStorage.setItem('userToken', data.token);
                            // 将用户设为已登陆
                            localStorage.setItem('isLoggedIn', true);
                            // 保存用户ID  
                            localStorage.setItem('userId', data.user_id);
                        } else {
                            alert(data.message);
                        }
                    })
                    .catch(error => {
                        // 处理错误响应  
                        alert('请求错误:', error);
                    });
            } else {
                alert("两次密码不一致");
                location.reload();
            }
        }
    },

};
</script>
<style></style>