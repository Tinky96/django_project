<template>

    <load_header></load_header>

    <div class="container header_container">
        <div class="row align-items-center">
            <div class="col-lg-6">
                <div class="slider-content">
                    <h5>多读书 多看报</h5>
                    <h1>少玩游戏</h1>
                    <p>多睡觉</p>

                </div>
            </div>
            <div class="col-lg-6">
                <div class="hero-thumb">
                    <img src="@/assets/picture/index.jpg" alt="thumb">
                </div>
            </div>
        </div>

    </div>

    <div class="blog-section">
        <div class="container">
            <div class="row">
                <div class="col-lg-12">
                    <div class="section-title-left text-center" data-cues="slideInUp">
                        <h5></h5>
                        <h1>游戏列表</h1>
                    </div>
                </div>
            </div>
            <el-form-item label="类型">
                <el-select v-model="value" placeholder="选择类型" class="col-lg-3">
                    <el-option v-for="item in options" :key="item.value" :label="item.label" :value="item.value">
                    </el-option>
                </el-select>
            </el-form-item>

            <div class="container">
                <div class="col-lg-12" v-masonry>
                    <div v-masonry-tile v-for="product in productList" :key="product.Product_id" class="col-lg-4 col-md-6 item">

                        <div class="single-blog-box">
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
        };
    },
    components: {
        load_header,
        load_footer,
    },
    methods: {
        fetchCategories() {
            this.$axios
                .get("/api/categories/")
                .then((response) => {
                    this.options = response.data.map((category) => ({
                        value: category.category_id,
                        label: category.category_name,
                    }));
                })
                .catch((error) => {
                    alert(error);
                });
        },
        get_goods() {
            let url = "/api/get_product";
            if (this.value) {
                url += "?category_id=" + this.value;
            }
            this.$axios
                .get(url)
                .then((response) => {
                    this.productList = response.data;
                    console.log(this.productList);
                })
                .catch((error) => {
                    console.error("get_goods Error", error);
                });
            this.refreshLayout = true;
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
        this.fetchCategories();
    },
    watch: {
        value: {
            handler() {
                this.get_goods();
            },
            immediate: true, // fetch products on initial load
        },
    },
};
</script>

