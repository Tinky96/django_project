<template>
    <load_header></load_header>
    <!-- 搜索框 -->

    <div class="blog-section">
        <div class="container">
            <div class="row">
                <el-form-item label="类型">
                    <el-select v-model="value" placeholder="选择类型" class="col-lg-3">
                        <el-option v-for="item in options" :key="item.value" :label="item.label" :value="item.value">
                        </el-option>
                    </el-select>
                </el-form-item>
                <div class="col-lg-12">
                    <div v-masonry="containerId" transition-duration="0.3s" item-selector=".item">
                        <div v-masonry-tile v-for="product in productList" :key="product.Product_id" class="col-lg-4 col-md-6 item">
                            <div class="single-blog-box" data-cues="slideInUp">
                                <div class="blog-thumb">
                                    <img :src="
                                            getImageUrl(product.product_image)
                                        " alt="thumb" />
                                </div>
                                <div class="blog-content">
                                    <div class="blog-meta-icon">
                                        <h6>
                                            <i aria-hidden="true" class="far fa-calendar-alt"></i>
                                            <span>{{ product.update }}</span>
                                        </h6>
                                    </div>
                                    <div class="blog-meta-comment-icon">
                                        <h6>
                                            <i class="bi bi-chat-dots"></i>
                                            <span>Comment (5)</span>
                                        </h6>
                                    </div>
                                    <h3>
                                        <a href="#" @click="
                                                goToBuyGoods(product.Product_id)
                                            ">{{ product.Product_name }}</a>
                                    </h3>
                                    <p>{{ product.product_upper }}</p>
                                    <div class="blog-button">
                                        <a href="#" @click="
                                                goToBuyGoods(product.Product_id)
                                            ">Read More
                                            <i class="bi bi-chevron-double-right"></i></a>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <div class="counter-section">
        <div class="container">
            <div class="row">
                <div class="col-lg-3 col-md-6">
                    <div class="single-counter-box" data-cues="slideInUp">
                        <div class="counter-icon">
                            <img src="@/assets/picture/counter-icon.png" alt="" />
                        </div>
                        <div class="counter-title">
                            <div class="counter-text">
                                <h1 class="counter">200</h1>
                                <span>+</span>
                                <p>Clients Protection</p>
                            </div>
                        </div>
                        client
                    </div>
                </div>
                <div class="col-lg-3 col-md-6">
                    <div class="single-counter-box" data-cues="slideInUp">
                        <div class="counter-icon">
                            <img src="@/assets/picture/counter-icon1.png" alt="" />
                        </div>
                        <div class="counter-title">
                            <div class="counter-text">
                                <h1 class="counter">250</h1>
                                <span>+</span>
                                <p>Smart Home Protection</p>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col-lg-3 col-md-6">
                    <div class="single-counter-box" data-cues="slideInUp">
                        <div class="counter-icon">
                            <img src="@/assets/picture/counter-icon2.png" alt="" />
                        </div>
                        <div class="counter-title">
                            <div class="counter-text">
                                <h1 class="counter">280</h1>
                                <span>+</span>
                                <p>Website Protection</p>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col-lg-3 col-md-6">
                    <div class="single-counter-box" data-cues="slideInUp">
                        <div class="counter-icon">
                            <img src="@/assets/picture/counter-icon3.png" alt="" />
                        </div>
                        <div class="counter-title">
                            <div class="counter-text">
                                <h1 class="counter">320</h1>
                                <span>+</span>
                                <p>Programmers Team</p>
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
import load_footer from './load_footer.vue';
import load_header from "./load_header.vue";

export default {
    data() {
        return {
            message: "",
            productList: [],
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
        },
    },
    methods: {
        get_goods() {
            const message = this.$route.query.message;
            const headers = {
                Authorization: `Token ${localStorage.getItem("userToken")}`,
            };
            this.$axios
                .get(`/api/get_product/?q=${message}`, { headers })
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
        goToBuyGoods(product_id) {
            this.$router.push({ path: "/buy_goods", query: { product_id } });
        },
        search(message) {
            this.$router.push({ path: "/search_goods", query: { message } });
        },
    },
    mounted() {
        this.get_goods();
    },
};
</script>
