<template>
    <div class="footer-section">
        <div class="container">
            <div class="row">
                <div class="col-lg-3">
                    <div class="footer-widget-title">
                        <h3>销售量</h3>
                    </div>
                    <div class="container">
                        <div class="company-info-desce">
                            <img :src="trendImage" alt="Transaction Trend" class="img-fluid" v-if="trendImage">
                        </div>
                    </div>
                </div>
                <div class="col-lg-3">
                    <div class="footer-widget-title">
                        <h3>最受欢迎</h3>
                    </div>
                    <div class="container">
                        <div class="company-info-desce">
                            <img :src="soldCategoryImage" alt="Sold Product Category Distribution" class="img-fluid" v-if="soldCategoryImage">
                        </div>
                    </div>

                </div>
                <div class="col-lg-3">
                    <div class="footer-widget-title">
                        <h3>正在热卖</h3>
                    </div>
                    <div class="container">
                        <div class="company-info-desce">
                            <img :src="onSaleCategoryImage" alt="On Sale Product Category Distribution" class="img-fluid" v-if="onSaleCategoryImage">
                        </div>
                    </div>

                </div>
                <div class="col-lg-3 col-md-6">
                    <div class="footer-widget-content" data-cues="slideInUp">
                        <div class="footer-widget-title">
                            <h3>Get in Touch</h3>
                        </div>
                        <div class="icon-box">
                            <div class="widget-icon-box">
                                <div class="widget-icon">
                                    <i class="bi bi-envelope-open"></i>
                                </div>
                            </div>
                            <div class="icon-box-content">
                                <p>Email Us</p>
                                <h4>c487836173@163.com</h4>
                            </div>
                        </div>
                        <div class="icon-box">
                            <div class="widget-icon-box">
                                <div class="widget-icon">
                                    <i class="bi bi-telephone"></i>
                                </div>
                            </div>
                            <div class="icon-box-content">
                                <p>Phone Us</p>
                                <h4>+86 17649987250</h4>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="row">
                <div class="col-lg-12">
                    <div class="copyright-description text-center">
                        <p><a>欢迎指正</a></p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>

import axios from "axios";

export default {
    data() {
        return {
            trendImage: null,
            soldCategoryImage: null,
            onSaleCategoryImage: null,
        };
    },
    mounted() {
        this.fetchImages();
    },
    methods: {
        fetchImages() {
            axios
                .get("/api/get_images/")
                .then((response) => {
                    this.trendImage =
                        "data:image/png;base64," + response.data.trend_image;
                    this.soldCategoryImage =
                        "data:image/png;base64," +
                        response.data.sold_category_image;
                    this.onSaleCategoryImage =
                        "data:image/png;base64," +
                        response.data.on_sale_category_image;
                })
                .catch((error) => {
                    console.error("Error fetching images:", error);
                });
        },
    },
};
</script>

<style scoped>
.company-info-desce img {
    max-width: 100%;
    height: auto;
}
</style>

