<template>
    <load_header></load_header>
    <div class="container header_container">
        <div class="row align-items-center">
            <div class="col-lg-6">
                <div class="slider-content">

                    <a href = "#" @click="goToUserPage">upper: {{ product.product_upper }}</a>

                </div>

            </div>
        </div>
        <div class="col-lg-6">

        </div>
    </div>

    <div class="subscribe-section">
        <div class="container">
            <div class="row subscribe flex-center">
                <div class="col-lg-6">
                    <el-carousel indicator-position="outside">
                        <el-carousel-item v-for="image in productImages" :key="image">
                            <div style="display: flex; justify-content: center; align-items: center; height: 300px;">
                                <img :src="getImageUrl(image)" alt="product image" style="max-height: 100%; max-width: 100%; object-fit: contain;">
                            </div>
                        </el-carousel-item>
                    </el-carousel>

                </div>
                <div class="col-lg-6 flex-center">
                    <el-card style="width: 480px">
                        <template #header>
                            <div class="card-header">
                                <span>商品名称 {{ product.Product_name }}</span>
                            </div>
                        </template>
                        <p>上传者: {{ product.product_upper }}</p>
                        <p>上传日期: {{ product.update }}</p>
                        <p>类型: {{ product.category }}</p>
                        <p>描述: {{ product.description }}</p>
                        <template #footer>价格: {{ product.Product_price }}</template>
                    </el-card>
                </div>
                <div class="col-lg-12">
                    <div class="change-button flex-center">
                        <el-button-group>
                            <el-button type="primary" @click="add_to_Cart">+
                                <el-icon>
                                    <ShoppingCartFull />
                                </el-icon>
                            </el-button>
                            <el-button type="primary" @click="buy_it">Buy!</el-button>

                        </el-button-group>
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
    components: {
        load_header,
        load_footer,
    },
    data() {
        return {
            product: {},
            productImages: [],
        };
    },
    methods: {
        getProductInfo() {
            const product_id = this.$route.query.product_id;
            const headers = {
                Authorization: `Token ${localStorage.getItem("userToken")}`,
            };
            this.$axios
                .get(`/api/get_one_product/?product_id=${product_id}`, {
                    headers,
                })
                .then((response) => {
                    this.product = response.data[0];
                    this.productImages = this.product.images;
                })
                .catch((error) => {
                    console.log(error);
                });
        },
        getImageUrl(image) {
            return this.$axios.defaults.baseURL + image;
        },
        buy_it() {
            this.$axios
                .post("/api/make_order/", {
                    upper: this.product.upper,
                    buyer: localStorage.getItem("userId"),
                    product_id: this.product.product_id,
                })
                .then((response) => {
                    alert(response);
                });
        },
        add_to_Cart() {
            const cartData = {
                user_id: localStorage.getItem("userId"),
                product_id: this.product.product_id,
            };

            const headers = {
                Authorization: `Token ${localStorage.getItem("userToken")}`,
            };

            this.$axios
                .post("/api/add_to_cart/", cartData, { headers })
                .then((response) => {
                    alert(response + "商品已添加到购物车！");
                })
                .catch((error) => {
                    console.log(error);
                });
        },
    },
    mounted() {
        this.getProductInfo();
    },
};
</script>