<template>
    <!-- 这是文章首页 -->
    <div class="max-w-7xl mx-auto grid grid-cols-5 gap-4">
        <div class="mt-4 main-left col-span-1">
            <div class="p-1 bg-white border border-gray-200 text-center rounded-xl flex flex-col space-y-2">
                <div @click="getArticleList('')"
                    class="flex items-center space-x-2 text-gray-500 hover:text-blue-700 p-4 rounded-xl hover:bg-gray-100">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                        stroke="currentColor" class="w-6 h-6 mr-2">
                        <path stroke-linecap="round" stroke-linejoin="round"
                            d="M2.25 12l8.954-8.955c.44-.439 1.152-.439 1.591 0L21.75 12M4.5 9.75v10.125c0 .621.504 1.125 1.125 1.125H9.75v-4.875c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125V21h4.125c.621 0 1.125-.504 1.125-1.125V9.75M8.25 21h8.25" />
                    </svg>综合推荐
                </div>
                <div @click="getArticleList('考研资讯')"
                    class="flex items-center space-x-2 text-gray-500 hover:text-blue-700 p-4 rounded-xl hover:bg-gray-100">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                        stroke="currentColor" class="w-6 h-6 mr-2">
                        <path stroke-linecap="round" stroke-linejoin="round"
                            d="M2.25 12l8.954-8.955c.44-.439 1.152-.439 1.591 0L21.75 12M4.5 9.75v10.125c0 .621.504 1.125 1.125 1.125H9.75v-4.875c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125V21h4.125c.621 0 1.125-.504 1.125-1.125V9.75M8.25 21h8.25" />
                    </svg>考研资讯
                </div>
                <div @click="getArticleList('院校信息')"
                    class="flex items-center space-x-2 text-gray-500 hover:text-blue-700 p-4 rounded-xl hover:bg-gray-100">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                        stroke="currentColor" class="w-6 h-6 mr-2">
                        <path stroke-linecap="round" stroke-linejoin="round"
                            d="M2.25 12l8.954-8.955c.44-.439 1.152-.439 1.591 0L21.75 12M4.5 9.75v10.125c0 .621.504 1.125 1.125 1.125H9.75v-4.875c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125V21h4.125c.621 0 1.125-.504 1.125-1.125V9.75M8.25 21h8.25" />
                    </svg>院校信息
                </div>
                <div @click="getArticleList('学习交流')"
                    class="flex items-center space-x-2 text-gray-500 hover:text-blue-700 p-4 rounded-xl hover:bg-gray-100">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                        stroke="currentColor" class="w-6 h-6 mr-2">
                        <path stroke-linecap="round" stroke-linejoin="round"
                            d="M2.25 12l8.954-8.955c.44-.439 1.152-.439 1.591 0L21.75 12M4.5 9.75v10.125c0 .621.504 1.125 1.125 1.125H9.75v-4.875c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125V21h4.125c.621 0 1.125-.504 1.125-1.125V9.75M8.25 21h8.25" />
                    </svg>学习交流
                </div>
                <div @click="getArticleList('复试准备')"
                    class="flex items-center space-x-2 text-gray-500 hover:text-blue-700 p-4 rounded-xl hover:bg-gray-100">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                        stroke="currentColor" class="w-6 h-6 mr-2">
                        <path stroke-linecap="round" stroke-linejoin="round"
                            d="M2.25 12l8.954-8.955c.44-.439 1.152-.439 1.591 0L21.75 12M4.5 9.75v10.125c0 .621.504 1.125 1.125 1.125H9.75v-4.875c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125V21h4.125c.621 0 1.125-.504 1.125-1.125V9.75M8.25 21h8.25" />
                    </svg>复试准备
                </div>
                <div @click="getArticleList('心灵驿站')"
                    class="flex items-center space-x-2 text-gray-500 hover:text-blue-700 p-4 rounded-xl hover:bg-gray-100">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                        stroke="currentColor" class="w-6 h-6 mr-2">
                        <path stroke-linecap="round" stroke-linejoin="round"
                            d="M2.25 12l8.954-8.955c.44-.439 1.152-.439 1.591 0L21.75 12M4.5 9.75v10.125c0 .621.504 1.125 1.125 1.125H9.75v-4.875c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125V21h4.125c.621 0 1.125-.504 1.125-1.125V9.75M8.25 21h8.25" />
                    </svg>心灵驿站
                </div>
            </div>
        </div>

        <div class="mt-4 main-center col-span-3 space-y-4">
            <div v-if="articles.length === 0"
                class="p-4  bg-white border border-gray-200 rounded-xl flex flex-col items-center">
                <p class="text-gray-500 text-xl mt-8">亲爱的研梦er，这里空空如也~</p>
                <img src="http://127.0.0.1:8000/media/svg/empty.svg" class="w-1/2 mt-4">
            </div>

            <div v-for="(article, index) in articles" :key="index"
                @click="goToArticleDetail(article.id, article.is_vip, article.ViewNum)"
                class="p-4 bg-white border border-gray-200 rounded-xl hover:bg-blue-100">
                <div class="flex items-center space-x-1">
                    <div class="border-2 border-blue-500 h-6 mx-2"></div>
                    <h2 class="text-xl font-bold">{{ article.title }}</h2>
                    <div v-if="article.is_vip"
                        class=" text-xs text-white border bg-orange-400 border-orange-500 rounded-full px-2">VIP专属</div>
                </div>
                <p class="text-sm text-gray-500 mt-3">{{ article.abstract }}</p>
                <div class="flex justify-between items-center mt-5">
                    <div class="flex space-x-2 text-gray-500 text-sm">
                        <span>{{ article.author_name }}</span>
                        <div class="border-2 border-gray-300 h-5 mx-2"></div>
                        <span>浏览量: {{ article.ViewNum }}</span>
                        <div class="border-2 border-gray-300 h-5 mx-2"></div>
                        <span>
                            点赞量: {{ article.LikeNum }}</span>
                    </div>
                    <div class="flex space-x-2 text-gray-500 text-xs">
                        <span v-for="tag in [article.tag1, article.tag2, article.tag3]" :key="tag"
                            class="px-4 py-1 bg-gray-200 rounded-3xl">{{ tag }}</span>
                    </div>
                </div>
            </div>
        </div>

        <div class="mt-4 main-right col-span-1 space-y-4">
            <div v-if="isLoggedIn" class="p-4 bg-white border border-gray-200 text-center rounded-xl">
                <img class="w-20 h-20 rounded-full mx-auto mb-2" :src="userInfo.avatar" alt="User avatar">
                <h2 class="text-xl font-bold">{{ userInfo.name }}</h2>
                <div class="text-xs rounded-full py-1 px-3 mt-2 mb-1 inline-block"
                    :class="{ 'bg-green-400 text-white': userInfo.is_vip, 'bg-blue-400 text-white': !userInfo.is_vip }">
                    {{ userInfo.is_vip ? 'VIP用户' : '普通用户' }}
                </div>
                <div class="text-sm text-gray-500 mt-1">
                    研梦值：{{ userInfo.ymvalue }}
                </div>
                <div class="flex justify-around items-center mt-4">
                    <button @click="goToUserCenter" class="px-8 py-2 bg-blue-500 text-white rounded-3xl">个人中心</button>
                </div>
                <div class="flex justify-around items-center mt-4">
                    <button @click="logOut" class="px-8 py-2 bg-gray-500 text-white rounded-3xl">退出登录</button>
                </div>
            </div>

            <div v-else class="p-4 bg-white border border-gray-200 text-center rounded-xl">

                <div class="flex items-center space-x-1">
                    <div class="border-2 border-blue-500 h-6 mx-2"></div>
                    <h2 class="text-xl font-bold">登录享受更多权益</h2>
                </div>
                <RouterLink to="/login">
                    <div class="flex justify-around items-center mt-4">
                        <button class="px-8 py-2 bg-blue-500 text-white rounded-xl">登录</button>
                    </div>
                </RouterLink>

                <RouterLink to="/signup">
                    <div class="flex justify-around items-center mt-4">
                        <button class="px-8 py-2 bg-gray-500 text-white rounded-xl">注册</button>
                    </div>
                </RouterLink>
            </div>

            <div class="relative">
                <RouterLink to="/offer">
                    <div v-if="showCard" class="p-4 bg-white border border-gray-200 text-center rounded-xl">
                        <div class="">戳这里领取你的专属C9高校录取通知书吧!</div>
                        <div class="text-sm text-gray-400">(此功能仅供娱乐)</div>
                    </div>
                </RouterLink>

                <button v-if="showCard" class="absolute top-0 right-0 mt-2 mr-2 text-gray-500" @click="closeCard">
                    <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12">
                        </path>
                    </svg>
                </button>
            </div>

        </div>
    </div>
</template>

<script>
import axios from 'axios';
import { ElMessage } from 'element-plus';

export default {
    data() {
        return {
            articles: [], // 存储文章数据
            isLoggedIn: false,
            showCard: true,
            userInfo: {},
        };
    },
    created() {
        // 在组件创建时调用 getArticleList 方法，参数为空
        this.getArticleList();
        // 在组件创建时检查用户登录状态
        this.checkLoginStatus();
    },
    methods: {
        // 关闭按钮
        closeCard() {
            this.showCard = false;
        },

        // 检查用户登录状态
        checkLoginStatus() {
            // 检查 localStorage 或其他适合的方式来确定用户是否已登录
            const userData = localStorage.getItem('user');
            console.log(userData);
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

        // 获取分类文章列表
        getArticleList(category) {
            // 发送GET请求
            axios.get('/api_article/getArticlelist/', {
                params: {
                    category: category
                }
            })
                .then(response => {
                    // 更新文章列表数据
                    this.articles = response.data;
                    console.log(this.articles);
                })
                .catch(error => {
                    // 处理错误
                    console.error('Error:', error);
                });
        },

        // 跳转到文章详情页面
        goToArticleDetail(articleId, is_vip, idViewNum) {
            // 文章仅vip用户可见
            if (is_vip) {
                if (!this.isLoggedIn) {
                    ElMessage.warning('当前内容仅限VIP用户查看,请先登录!');
                    return;
                }
                if (this.userInfo.is_vip == false) {
                    ElMessage.warning('当前内容仅限VIP用户查看,请先开通VIP!');
                    return;
                }
            }
            // 更新浏览量
            axios.patch(`/api_article/article/${articleId}/`, {
                ViewNum: idViewNum + 1, // 假设点赞成功后数量加1
            }).then(response => {
                // 更新文章点赞数量成功后，刷新评论列表
                console.log(response.data)
            }).catch(error => {
                console.error('Error updating like count:', error);
            });
            // 使用 Vue Router 导航到文章详情页面，并传递 articleId 作为参数
            this.$router.push({ name: 'article', params: { id: articleId } });
        },
        // 跳转到用户中心
        goToUserCenter() {
            if (!this.isLoggedIn) {
                ElMessage.warning('未检测到您的登录状态,请先登录!');
                return;
            }
            this.$router.push({ name: 'user', params: { id: this.userInfo.id } });
        },
        // 退出登录
        logOut() {
            localStorage.removeItem('user');
            this.isLoggedIn = false;
            this.userInfo = {};
        }


    }
}
</script>