/* eslint-disable */
<template>
    <load_header></load_header>

    <div class="container header_container">
        <div class="row subscribe">
            <div class="col-lg-6">
                <el-upload ref="uploader" v-loading="loading" action="upload" :style="style" :auto-upload="false" list-type="picture-card" :name="uploadId" accept="image/*" :multiple="true" :file-list="fileList" :before-upload="handleBeforeUpload" :http-request="httpRequest" :on-change="handleChange" :on-remove="handleRemove">
                    <el-icon>
                        <Plus />
                    </el-icon>
                </el-upload>
            </div>
            <div class="col-lg-6">
                <el-form :model="form" label-width="auto" style="max-width: 600px">
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
    <load_footer></load_footer>
</template>

<script>
import { ref } from "vue";
import load_header from "./load_header.vue";
import load_footer from "./load_footer.vue";
// import { Delete, Download, Plus, ZoomIn } from '@element-plus/icons-vue'

export default {
    data() {
        return {
            options: [],
            value: "",
            fileList: [],
            product_name: "",
            product_number: "",
            product_key: "",
            product_discription: "",
            product_price: "",
        };
    },
    components: {
        load_header,
        load_footer,
    },
    methods: {
        handleRemove(file, fileList) {
            // 更新fileList数组
            this.fileList = fileList;
        },
        handlePictureCardPreview(file) {
            this.dialogImageUrl = file.url;
            this.dialogVisible = true;
        },
        handleDownload(file) {
            console.log(file);
        },
        handleChange(file, fileList) {
            // 更新fileList数组
            this.fileList = fileList;
        },
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
        submit() {
            alert(this.value);
            const formData = new FormData();
            formData.append("user_id", localStorage.getItem("userId"));
            formData.append("product_name", this.product_name);
            formData.append("product_number", this.product_number);
            formData.append("product_key", this.product_key);
            formData.append("product_description", this.product_discription);
            formData.append("product_price", this.product_price);
            formData.append("category_id", this.value);

            this.fileList.forEach((file) => {
                formData.append("images", file.raw, file.name);
            });
            const headers = {
                Authorization: `Token ${localStorage.getItem("userToken")}`,
            };
            this.$axios
                .post("/api/create_product/", formData, { headers })
                .then((response) => {
                    console.log(response.data);
                    // 处理成功响应
                })
                .catch((error) => {
                    console.error(error);
                    // 处理错误响应
                });
        },
    },
    created() {
        this.fetchCategories();
    },
    setup() {
        const dialogImageUrl = ref("");
        const dialogVisible = ref(false);
        const disabled = ref(false);

        return {
            dialogImageUrl,
            dialogVisible,
            disabled,
        };
    },
};
</script>

<style scoped>
::v-deep .el-form-item__label {
    color: white !important;
}
.el-upload__icon {
    /* 假设图标是通过颜色填充的 */
    fill: rgba(0, 0, 0, 0.5); /* 设置为半透明黑色 */
    /* 或者如果图标是通过背景色设置的 */
    background-color: rgba(0, 0, 0, 0.5); /* 设置为半透明黑色背景 */
}

/* 如果图标是一个字体图标，你可能需要修改它的颜色 */
.el-upload__icon-font {
    color: rgba(0, 0, 0, 0.5); /* 设置为半透明黑色字体颜色 */
}
</style>