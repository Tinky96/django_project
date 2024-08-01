<template>
    <div>
        <h1>Transaction Trend</h1>
        <img :src="trendImage" alt="Transaction Trend" v-if="trendImage">

        <h1>Sold Product Category Distribution</h1>
        <img :src="soldCategoryImage" alt="Sold Product Category Distribution" v-if="soldCategoryImage">

        <h1>On Sale Product Category Distribution</h1>
        <img :src="onSaleCategoryImage" alt="On Sale Product Category Distribution" v-if="onSaleCategoryImage">
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
img {
    max-width: 100%;
    height: auto;
}
</style>
  