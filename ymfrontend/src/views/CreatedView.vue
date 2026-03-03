<template>
    <div class="mt-8 max-w-4xl mx-auto grid grid-cols-4 gap-4">
        <div class="main-center col-span-4">
            <div class="p-12 bg-white border border-gray-200 rounded-3xl">
                <div>
                    <div class="border-l-4 border-blue-500 pl-2">
                        <label class="text-xl font-bold">标题</label>
                    </div>
                    <br>
                    <input type="text" placeholder="请输入文章标题" v-model="form.title"
                        class="w-full py-4 m mb-4 px-6 border border-gray-300 rounded-lg">
                </div>
                <div>
                    <div class="border-l-4 border-blue-500 pl-2">
                        <label class="text-xl font-bold">摘要</label>
                    </div>
                    <br>
                    <input type="text" placeholder="请输入文章摘要" v-model="form.abstract"
                        class="w-full mb-4 py-4 px-6 border border-gray-300 rounded-lg">
                </div>
                <div class="border-l-4 border-blue-500 pl-2">
                    <label class="text-xl font-bold">所属类别</label>
                </div>
                <div class="flex">
                    <!-- 用 v-for 循环生成单选框 -->
                    <label v-for="category in categories" :key="category" class="mr-6 my-4">
                        <div
                            class="bg-blue-100 border border-blue-500 rounded-lg px-4 py-2 cursor-pointer hover:bg-blue-200">
                            <input type="radio" v-model="form.category" :value="category"
                            name="category" class="">
                            {{ category }}
                        </div>
                    </label>
                </div>
                <div class="border-l-4 border-blue-500 pl-2">
                    <label class="text-xl font-bold">标签</label>
                </div>
                <div class="flex mt-4">
                    <input type="text" placeholder="考研" v-model="form.tag1" 
                        class="w-full py-4 m mb-4 px-6 border border-gray-300 rounded-lg mr-4">
                    <input type="text" placeholder="顺利" v-model="form.tag2"
                        class="w-full py-4 m mb-4 px-6 border border-gray-300 rounded-lg mr-4">
                    <input type="text" placeholder="上岸" v-model="form.tag3"
                        class="w-full py-4 m mb-4 px-6 border border-gray-300 rounded-lg">
                </div>
                <div class="mt-4">
                    <div class="border-l-4 border-blue-500 pl-2">
                        <label class="text-xl font-bold">是否VIP专属</label>
                    </div>
                    <div class="flex my-4">
                        <label class="mr-6">
                            <div
                                class="bg-blue-100 border border-blue-500 rounded-lg px-4 py-2 cursor-pointer hover:bg-blue-200">
                                <input type="radio" value="true" v-model="form.is_vip" name="vipExclusive" class="mr-2">
                                是
                            </div>
                        </label>
                        <label>
                            <div
                                class="bg-blue-100 border border-blue-500 rounded-lg px-4 py-2 cursor-pointer hover:bg-blue-200">
                                <input type="radio" value="false"
                                v-model="form.is_vip" name="vipExclusive" class="mr-2">
                                否
                            </div>
                        </label>
                    </div>
                </div>
                <div class="border-l-4 border-blue-500 pl-2">
                    <label class="text-xl font-bold">正文</label>
                </div>
                <div class="mt-4">
                    <textarea placeholder="在这里输入文章内容" v-model="form.content"
                            class="w-full h-64 py-4 px-6 border border-gray-300 rounded-lg"></textarea>
                        
                </div>
               

                <div class="mt-4">
                    <button @click="submitArticle" class="mt-6 py-4 px-8 bg-blue-500 text-white rounded-lg mx-auto block">提交</button>
                </div>
            </div>
        </div>
    </div>
    
</template>

<script>
import axios from 'axios';
import markdownIt from 'markdown-it';
import { ElMessage } from 'element-plus';

export default {
    data() {
        return {
            isLoggedIn: false,
            userInfo: {},
            categories: ['考研资讯', '院校信息', '学习交流', '复试准备', '心灵驿站'], // 单选框的选项
            markdownInput: '', // 输入的 markdown 文本
            markdownOutput: '', // markdown-it 渲染后的效果
            form: {
                title: '',
                abstract: '',
                category: '',
                tag1: '',
                tag2: '',
                tag3: '',
                content: '',
                is_vip:false,
            }
        }
    },
    created() {
        this.checkLoginStatus();
    },
    methods: {
        checkLoginStatus() {
            // 检查 localStorage 或其他适合的方式来确定用户是否已登录
            const userData = localStorage.getItem('user');
            // console.log(userData);
            if (userData) {
                // 如果存在用户数据，则认为用户已登录
                this.isLoggedIn = true;
                this.userInfo = JSON.parse(userData);
                console.log(this.userInfo)
            } else {
                // 否则，用户未登录
                this.isLoggedIn = false;
            }
        },
        //提交文章
        submitArticle() {
            if(!this.isLoggedIn){
                ElMessage.error('请先登录!');
                return;
            }
            if (!this.form.title || !this.form.abstract || !this.form.category || !this.form.content) {
                ElMessage.error('请填写完整信息!');
                return;
            }
            const articleData = {
                title: this.form.title,
                abstract: this.form.abstract,
                category: this.form.category,
                tag1: this.form.tag1,
                tag2: this.form.tag2,
                tag3: this.form.tag3,
                content: this.form.content,
                is_vip: this.form.is_vip,
                author: this.userInfo.id
            };
            if(!articleData.tag1){
                articleData.tag1='考研';
            }
            if(!articleData.tag2){
                articleData.tag2='顺利';
            }
            if(!articleData.tag3){
                articleData.tag3='上岸';
            }
            console.log(articleData);
             // Send article data to the API endpoint
             axios.post('/api_article/article/', articleData)
                .then(response => {
                    // Handle successful response
                    console.log("Article uploaded successfully:", response.data);
                    ElMessage.success('文章发布成功!');
                    this.form= {
                        title: '',
                        abstract: '',
                        category: '',
                        tag1: '',
                        tag2: '',
                        tag3: '',
                        content: '',
                        is_vip:false,
                    };
                })
                .catch(error => {
                    // Handle error response
                    console.error("Error uploading article:", error.response.data);
                    // Display error message to the user
                    ElMessage.error('提交文章发生错误，请稍后重试!');
                });
        },
    },
}
</script>