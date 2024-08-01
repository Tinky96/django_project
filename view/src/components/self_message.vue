
<template>
    <load_header></load_header>
    <div class="container header_container">
        <div class="row align-items-center">
            <div class="col-lg-6">
                <div class="slider-content">
                    <h1>{{ this.$route.query.userId  }}</h1>
                    <h5>&</h5>
                    <p>用户主页</p>

                </div>
            </div>
            <div class="col-lg-6">
                <div class="slider-content">
                    <p>已上传:{{userMessage.uploadedQuantity }}</p>
                    <p>已购买:{{userMessage.purchasedQuantity }}</p>
                    <p>已售出:{{userMessage.soldQuantity }}</p>
                </div>
            </div>
        </div>

    </div>

    <div class="container">
        <div class="row">
            <div class="col-lg-12">
                <div class="section-title-left text-center" data-cues="slideInUp">
                    <h5></h5>
                    <h1>商品信息</h1>
                </div>
            </div>
        </div>
        <div class="row">
            <div class="col-lg-8">
                <el-tabs tab-position="left">
                    <el-tab-pane label="售卖的商品">
                        <div class="demo-collapse">
                            <el-collapse v-model="activeNames" @change="handleChange">
                                <el-collapse-item v-for="(product, index) in productList" :key="index" :title="product.Product_name" :name="index" :class="product.isSaled ? 'dark' : ''" shadow="hover">
                                    <p>价格: {{ product.Product_price }}</p>
                                    <p>种类：{{ product.category }}</p>
                                    <p>描述：{{ product.description }}</p>
                                    <p>上传日期：{{ product.update }}</p>
                                    <el-button-group class="ml-4" v-if="!product.isSaled">
                                        <el-button type="primary" icon="edit" @click="showEdit()"></el-button>
                                        <el-button type="primary" icon="delete"></el-button>
                                    </el-button-group>
                                </el-collapse-item>
                            </el-collapse>
                        </div>
                    </el-tab-pane>
                    <el-tab-pane label="购买的商品" lazy="false">
                        <div class="demo-collapse">
                            <el-collapse v-model="activeNames" @change="handleChange">
                                <el-collapse-item v-for="(product, index) in buyList" :key="index" :title="product.Product_name" :name="index">
                                    <p>价格: {{ product.Product_price }}</p>
                                    <p>种类：{{ product.category }}</p>
                                    <p>描述：{{ product.description }}</p>
                                    <p>账号：{{ product.product_number }}</p>
                                    <p>密码: {{ product.product_key }}</p>
                                </el-collapse-item>
                            </el-collapse>
                        </div>
                    </el-tab-pane>
                    <el-tab-pane label="提现订单" lazy="false">
                        <div class="demo-collapse">
                            <el-collapse v-model="activeNames" @change="handleChange">
                                <el-collapse-item v-for="(rwOrder, index) in rwOrders" :key="index" :title="rwOrder.RW_Order_id" :name="index">
                                    <p>提现状态: {{ rwOrder.is_paid }}</p>
                                    <p>提现金额：{{ rwOrder.amount }}</p>
                                    <p>提现账户：{{ rwOrder.user_account}}</p>
                                </el-collapse-item>
                            </el-collapse>
                        </div>
                    </el-tab-pane>
                </el-tabs>

            </div>
            <div class="col-lg-4">
                <div class="subscribe-section text-center">
                    <div class="container">
                        <div class="row subscribe">
                            <div class="col-lg-12">
                                <div class="section-title-left">
                                    <h4>余额为: </h4>
                                    <h1>{{ userMessage.totalPrice }}¥</h1>
                                </div>
                                <div class="change-button"> <!-- 确保按钮容器居中显示 -->
                                    <el-button-group>
                                        <el-button type="primary" @click="showrecharge">充值</el-button>
                                        <el-button type="primary" @click="showwithdraw">提现</el-button>
                                    </el-button-group>
                                </div>
                            </div>
                            <div class="subscribe-shape" data-cues="slideInUp">
                                <img src="@/assets/picture/subscribe-shape.png" alt="shape">
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- 修改 -->
    <div v-if="showfrom" class="Edit-container">
        <span class="close-btn" @click="closeEdit">x</span>

        <div class="container col-lg-12">
            <div class="row">
                <div class="col-lg-6">
                    <el-upload ref="uploader" v-loading="loading" action="upload" :style="style" :auto-upload="false" list-type="picture-card" :name="uploadId" accept="image/*" :multiple="true" :file-list="fileList" :before-upload="handleBeforeUpload" :http-request="httpRequest" :on-change="handleChange" :on-remove="handleRemove">
                        <i class="el-icon-plus" />
                    </el-upload>
                </div>
                <div class="col-lg-6">
                    <el-form :model="form" label-width="auto" style="max-width: 80%">
                        <el-form-item label="商品名字">
                            <el-input v-model="product_name" />
                        </el-form-item>
                        <el-form-item label="账号">
                            <el-input v-model="product_number" />
                        </el-form-item>
                        <el-form-item label="密码">
                            <el-input v-model="product_key" />
                        </el-form-item>
                        <el-form-item label="类型">
                            <el-select v-model="value" placeholder="选择类型">
                                <el-option v-for="item in options" :key="item.value" :label="item.label" :value="item.value">
                                </el-option>
                            </el-select>
                        </el-form-item>
                        <el-form-item label="描述">
                            <el-input v-model="product_discription" type="textarea" />
                        </el-form-item>
                        <el-form-item label="价格">
                            <el-input v-model="product_price" />
                        </el-form-item>
                        <el-form-item>
                            <el-button type="primary" @click="submit">提交</el-button>
                            <el-button>Cancel</el-button>
                        </el-form-item>
                    </el-form>
                </div>
            </div>
        </div>
    </div>

    <!-- 提现 -->
    <div class="RW-container" v-if="withdraw">
        <span class="close-btn" @click="closeWithdraw">x</span>

        <div class="container col-lg-8">
            <div class="slider-demo-block text-center" style=" margin-bottom:10px;">
                <span class="demonstration">选择你需要提现的金额</span>
                <el-slider v-model="value" />
            </div>
            金额<el-input v-model="value" style="width: 240px; margin-bottom:20px;" placeholder="Please input" />
            账户<el-input v-model="auth_account" style="width: 240px; margin-bottom:20px;" placeholder="Please input" />
        </div>
        <el-button type="primary" @click="withdrawAction">提交</el-button>
    </div>

    <!-- 充值 -->
    <div class="RW-container" v-if="recharge">
        <span class="close-btn" @click="closerecharge">x</span>

        <div class="container col-lg-8">
            <div class="slider-demo-block text-center" style=" margin-bottom:10px;">
                <span class="demonstration">选择你需要充值的金额</span>
                <el-slider v-model="value" />
            </div>
            <el-input v-model="value" style="width: 240px; margin-bottom:20px;" placeholder="Please input" />
        </div>
        <el-button type="primary" @click="rechargeAction">提交</el-button>
    </div>
    <load_footer></load_footer>
</template>

<script>
import load_header from "./load_header.vue";
import load_footer from "./load_footer.vue";
export default {
    data() {
        return {
            message: "",
            productList: [],
            buyList: [],
            showfrom: false,
            userMessage: {
                totalPrice: "",
                uploadedQuantity: "",
                purchasedQuantity: "",
                soldQuantity: "",
            },
            value: 0,
            recharge: false,
            withdraw: false,
            auth_account: "",
            rwOrders:[],
        };
    },
    components: {
        load_header,
        load_footer,
    },
    watch: {
        // 监视路由的变化，如果查询参数发生变化，重新获取商品信息
        "$route.query.message"() {
            this.get_goods();
            this.get_buygoods();
        },
    },
    methods: {
        get_goods() {
            const headers = {
                Authorization: `Token ${localStorage.getItem("userToken")}`,
            };
            this.$axios
                .get(
                    `/api/self_products/?user=${localStorage.getItem(
                        "userId"
                    )}`,
                    {
                        headers,
                    }
                )
                .then((response) => {
                    this.productList = response.data;
                    this.productList.sort((a, b) => {
                        if (a.isSaled && !b.isSaled) {
                            return 1;
                        } else if (!a.isSaled && b.isSaled) {
                            return -1;
                        } else {
                            return 0;
                        }
                    });
                    console.log(this.productList);
                })
                .catch((error) => {
                    console.error("get_goods Error", error);
                });
        },
        get_buygoods() {
            const headers = {
                Authorization: `Token ${localStorage.getItem("userToken")}`,
            };
            this.$axios
                .get(
                    `/api/buy_products/?user=${localStorage.getItem("userId")}`,
                    {
                        headers,
                    }
                )
                .then((response) => {
                    this.buyList = response.data;
                    console.log(this.buyList);
                })
                .catch((error) => {
                    console.error("get_goods Error", error);
                });
        },
        getImageUrl(imagePath) {
            // 拼接基本URL和图片路径
            return this.$axios.defaults.baseURL + imagePath;
        },
        goToBuyGoods(product_id) {
            this.$router.push({ path: "/buy_goods", query: { product_id } });
        },
        search(message) {
            this.$router.push({ path: "/search_goods", query: { message } });
        },
        showEdit() {
            this.showfrom = true;
        },
        // 关闭
        closeEdit() {
            this.showfrom = false;
        },
        Editgoods() {},
        delete() {},
        get_message() {
            const headers = {
                Authorization: `Token ${localStorage.getItem("userToken")}`,
            };
            this.$axios
                .get(`/api/self_message/`, { headers })
                .then((response) => {
                    const userData = response.data;
                    this.userMessage.totalPrice = userData.account_balance; // 用户余额
                    this.userMessage.uploadedQuantity =
                        userData.uploaded_quantity; // 上传数量
                    this.userMessage.purchasedQuantity =
                        userData.purchased_quantity; // 购买数量
                    this.userMessage.soldQuantity = userData.sold_quantity; // 已售商品数量
                })
                .catch((error) => {
                    console.error("get_message Error", error);
                });
        },
        showrecharge() {
            this.recharge = true;
        },
        showwithdraw() {
            this.withdraw = true;
        },
        closerecharge() {
            this.recharge = false;
        },
        closeWithdraw() {
            this.withdraw = false;
        },
        // 提现操作
        withdrawAction() {
            const headers = {
                Authorization: `Token ${localStorage.getItem("userToken")}`,
            };
            const withdrawAmount = this.value; // 提现金额
            const authAccount = this.auth_account; // 提现账户

            // 检查提现账户是否为空
            if (!authAccount) {
                console.error("提现账户不能为空");
                return;
            }

            // 向后端发送提现请求
            this.$axios
                .post(
                    `/api/withdraw/`,
                    { amount: withdrawAmount, auth_account: authAccount },
                    { headers }
                )
                .then((response) => {
                    this.get_message();
                    console(response);
                    this.withdraw = false;
                })
                .catch((error) => {
                    console.error("Withdraw Error", error);
                });
        },
        getRWOrders() {
            // 发起 GET 请求获取后端订单数据
            const headers = {
                Authorization: `Token ${localStorage.getItem("userToken")}`,
            };
            this.$axios
                .get(`/api/get_rw_orders/`,{ headers })
                .then((response) => {
                    // 成功获取后端订单数据
                    this.rwOrders = response.data;
                    console.log("获取到的订单数据：", this.rwOrders);
                })
                .catch((error) => {
                    // 获取订单数据失败
                    console.error("获取订单数据失败：", error);
                });
        },

        // 充值操作
        rechargeAction() {
            const headers = {
                Authorization: `Token ${localStorage.getItem("userToken")}`,
            };
            const rechargeAmount = this.value; // 充值金额
            // 向后端发送充值请求
            this.$axios
                .post(`/api/recharge/`, { amount: rechargeAmount }, { headers })
                .then((response) => {
                    // 充值成功，更新用户信息
                    // this.get_message();
                    const payUrl = response.data.pay_url;
                    window.open(payUrl, "_blank");
                    // 关闭充值框
                    this.recharge = false;
                })
                .catch((error) => {
                    console.error("recharge Error", error);
                });
        },
    },
    // 滚动显示顶栏
    mounted() {
        this.get_goods();
        this.get_buygoods();
        this.get_message();
        this.getRWOrders();
    },
};
</script>
<style scoped>
</style>
