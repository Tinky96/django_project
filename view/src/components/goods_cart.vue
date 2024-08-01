<template>
    <load_header></load_header>
    <div class="container header_container">
        <div class="row align-items-center">
            <div class="col-lg-6">
                <div class="slider-content">
                    <h1>{{ this.$route.query.userId  }}</h1>
                    <h5>&</h5>
                    <p>购物车</p>
                </div>
            </div>
        </div>

    </div>
    <div class="container">
        <div class="row">
            <div class="col-lg-8 ">
                <div v-for="product in productList" :key="product.Product_id">
                    <el-card shadow="hover" class="product-card" style="margin-top:20px">
                        <div class="container" style="align-items: center">
                            <div class="row">
                                <!-- 勾选部分 -->
                                <div class="col-lg-1">
                                    <el-checkbox v-model="product.selected" size="large" @change="updatePrice(product)" />
                                </div>

                                <!-- 显示图片部分 -->
                                <div class="col-lg-4">
                                    <el-image style="width: auto; height: 100%" :src="getImageUrl(product.product_image)" :zoom-rate="1.2" :max-scale="7" :min-scale="0.2" :preview-src-list="srcList" :initial-index="4" fit="cover" />
                                </div>

                                <!-- 显示其他信息部分（例如更新日期） -->

                                <!-- 显示商品名称部分 -->
                                <div class="col-lg-4">
                                    <div class="blog-meta-icon">
                                        <h6>
                                            <i aria-hidden="true" class="far fa-calendar-alt"></i>
                                            <span>{{ product.update }}</span>
                                        </h6>

                                    </div>
                                    <p>用户: {{ product.product_upper }}</p>
                                    <p>种类: {{ product.category }}</p>
                                    <p>价格: {{ product.Product_price }} ¥</p>
                                    <div class="col-lg-2">
                                    </div>
                                </div>
                                <div class="col-lg-3">
                                    <p>
                                        name: {{ product.Product_name }}
                                    </p>
                                    <el-button type="primary" @click="rm_from_cart(product)">
                                        <el-icon>
                                            <Remove />
                                        </el-icon>
                                        移除</el-button>
                                </div>
                            </div>
                        </div>
                    </el-card>
                </div>
            </div>
            <div class="col-lg-4">
                <div class="subscribe-section text-center">
                    <div class="container">
                        <div class="row subscribe">
                            <div class="col-lg-12">
                                <div class="section-title-left">
                                    <h1>已选择</h1>
                                    <h4>{{ selectProcuct.length }}个</h4>
                                    <h4>价格为: </h4>
                                    <h1>{{ totalPrice }}¥</h1>
                                </div>
                                <div class="change-button"> <!-- 确保按钮容器居中显示 -->
                                    <el-button-group>
                                        <el-button type="primary" @click="buy_all">结算!</el-button>
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
            value: "",
            options: [],
            refreshLayout: false,
            totalPrice: 0,
            selectProcuct: [],
        };
    },
    components: {
        load_header,
        load_footer,
    },
    methods: {
        get_goods() {
            const message = this.$route.query.userId;
            const headers = {
                Authorization: `Token ${localStorage.getItem("userToken")}`,
            };
            this.$axios
                .get(`/api/get_carts/?user=${message}`, { headers })
                .then((response) => {
                    this.productList = response.data;
                    console.log(this.productList);
                })
                .catch((error) => {
                    console.error("get_goods Error", error);
                });
        },
        getImageUrl(imagePath) {
            // 拼接基本URL和图片路径
            return this.$axios.defaults.baseURL + imagePath;
        },
        updatePrice(product) {
            if (product.selected) {
                this.selectProcuct.push(product); // 将产品添加到选中列表中
            } else {
                const index = this.selectProcuct.indexOf(product);
                if (index !== -1) {
                    this.selectProcuct.splice(index, 1); // 从选中列表中移除产品
                }
            }

            // 计算总价
            this.totalPrice = this.selectProcuct.reduce(
                (total, product) => total + parseFloat(product.Product_price),
                0
            );
        },
        rm_from_cart(product) {
            const userId = this.$route.query.userId;
            const productId = product.Product_id;
            const headers = {
                Authorization: `Token ${localStorage.getItem("userToken")}`,
            };
            this.$axios
                .delete(`/api/remove_from_cart`, {
                    data: { user_id: userId, product_id: productId },
                    headers,
                })
                .then((response) => {
                    // 成功从购物车中移除商品后，重新获取购物车商品列表
                    alert(response);
                    this.get_goods();
                })
                .catch((error) => {
                    console.error("Error removing product from cart:", error);
                });
        },
        buy_all() {
            if (this.selectProcuct.length === 0) {
                // 如果没有选中的产品，则提示用户至少选择一个产品
                alert("请至少选择一个产品进行结算！");
                return;
            }

            // 构造订单数据
            const orderData = {
                buyer: this.$route.query.userId,
                productList: this.selectProcuct.map(
                    (product) => product.Product_id
                ),
            };

            // 发送 POST 请求创建订单
            const headers = {
                Authorization: `Token ${localStorage.getItem("userToken")}`,
            };
            this.$axios
                .post("/api/make_orders/", orderData, { headers })
                .then((response) => {
                    // 订单创建成功
                    alert(response + "订单创建成功！");
                    // 清空购物车中已选中的产品
                    this.selectProcuct = [];
                    this.totalPrice = 0;
                    // 重新获取购物车商品列表
                    this.get_goods();
                })
                .catch((error) => {
                    // 订单创建失败
                    console.error("Error creating order:", error);
                    alert("订单创建失败，请稍后重试！");
                });
        },
    },
    mounted() {
        this.get_goods();
    },
};
</script>
