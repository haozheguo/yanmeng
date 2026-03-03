<template>
    <div class="max-w-7xl mx-auto grid grid-cols-7 gap-4">
        <div class="mt-8 main-center col-span-5">
            <div class="bg-white border border-gray-200 rounded-xl">
                <div class="p-2 flex space-x-2 items-center">
                    <input type="text" v-model="searchText" class="p-4 flex-grow bg-gray-100 rounded-xl"
                        placeholder="请输入你要搜索的关键词">

                    <button @click="search" class="inline-block py-4 px-8 bg-blue-500 text-white rounded-xl">搜索</button>
                </div>
            </div>

            <div v-if="articles.length === 0 && posts.length === 0"
                class="p-4 mt-4 bg-white border border-gray-200 rounded-xl flex flex-col items-center">
                <p class="text-gray-500 text-xl mt-8">亲爱的研梦er，这里空空如也~</p>
                <img src="http://127.0.0.1:8000/media/svg/empty.svg" class="w-1/2 mt-4">
            </div>

            <div v-for="(article, index) in articles" :key="index"
                @click="goToArticleDetail(article.id, article.is_vip, article.ViewNum)"
                class="p-4 bg-white border border-gray-200 rounded-lg hover:bg-blue-100 mt-4">
                <div class="flex items-center space-x-1">
                    <div class="border-2 border-blue-500 h-6 mx-2"></div>
                    <h2 class="text-xl font-bold">{{ article.title }}</h2>
                    <div v-if="article.is_vip"
                        class="text-xs text-white border bg-orange-400 border-orange-500 rounded-full px-2">VIP专属</div>
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
                            class="px-2 py-1 bg-gray-200 rounded-lg">{{ tag }}</span>
                    </div>
                </div>
            </div>

            <div v-for="(post, index) in posts" :key="index" @click="goToPostDetail(post.id, post.ViewNum)"
                class="p-4 bg-white border border-gray-200 rounded-lg hover:bg-blue-100 mt-4">
                <div class="flex items-center space-x-1">
                    <img :src="post.author.avatar" alt="author's avatar" class="w-10 h-10 rounded-full">
                    <div>
                        <span class="font-bold ml-2">{{ post.author.name }}</span>
                        <span v-if="post.author.is_vip"
                            class="ml-2 text-sm text-white border bg-orange-400 border-orange-500 rounded-full px-1">VIP用户</span>
                    </div>
                </div>
                <p class="ml-8 mt-3">{{ post.content }}</p>
                <div v-if="post.img" class="mt-3">
                    <img :src="post.img" alt="post image" style="max-width: 75%;">
                </div>
                <div class="flex justify-between items-center mt-5">
                    <div class="flex space-x-2  text-sm">
                        <span class="text-blue-500">#{{ post.category }}</span>
                        <div class="border-2 border-gray-300 h-5 mx-2"></div>
                        <span class="text-gray-500">浏览量: {{ post.ViewNum }}</span>
                        <div class="border-2 border-gray-300 h-5 mx-2"></div>
                        <span class="text-gray-500">点赞量: {{ post.LikeNum }}</span>
                    </div>
                    <div class="text-gray-500 text-sm">
                        {{ formatDate(post.created_at) }}
                    </div>
                </div>
            </div>

        </div>

        <div class="mt-8 main-right col-span-2">
            <div class="bg-white rounded-xl p-2">
                <div class="flex items-center space-x-1 mb-2">
                    <div class="border-2 border-blue-500 h-6 ml-4 mr-2"></div>
                    <h2 class="text-xl font-bold">热门文章</h2>
                </div>
                <div v-for="(article, index) in trendArticle" :key="article.id"
                    @click="goToArticleDetail(article.id, article.is_vip, article.ViewNum)"
                    class=" hover:bg-gray-100 p-1 rounded-xl">
                    <div>
                        <span class="font-bold text-blue-500 mx-2">{{ index + 1 }}.</span>
                        <span class="font-bold"> {{ article.title }}</span>
                    </div>
                    <div class="flex justify-between">
                        <div>
                            <span class="text-sm text-blue-400 mx-2">#{{ article.category }}</span>
                            <span class="text-sm text-gray-500">浏览量:{{ article.ViewNum }} </span>
                            <span class="text-sm mx-2 text-gray-500">点赞量:{{ article.LikeNum }} </span>
                        </div>
                    </div>
                </div>

            </div>
            <div class="bg-white rounded-xl p-2 mt-4">
                <div class="flex items-center space-x-1 mb-2">
                    <div class="border-2 border-blue-500 h-6 ml-4 mr-2"></div>
                    <h2 class="text-xl font-bold">热门帖子</h2>
                </div>
                <div v-for="(post, index) in trendPost" :key="post.id" @click="goToPostDetail(post.id, post.ViewNum)"
                    class=" hover:bg-gray-100 p-1 rounded-xl">
                    <div>
                        <span class="font-bold text-blue-500 mx-2">{{ index + 1 }}.</span>
                        <span class="font-bold"> {{ post.content.slice(0, 15) }}...</span>
                    </div>
                    <div class="flex justify-between">
                        <div>
                            <span class="text-sm text-blue-400 mx-2">#{{ post.category }}</span>
                            <span class="text-sm text-gray-500">浏览量:{{ post.ViewNum }} </span>
                            <span class="text-sm mx-2 text-gray-500">点赞量:{{ post.LikeNum }} </span>
                        </div>
                    </div>
                </div>

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
            searchText: '',
            articles: [],
            posts: [],
            trendPost: [],
            trendArticle: [],
            isLoggedIn: false,
            userInfo: {},
        }
    },
    created() {
        this.checkLoginStatus();
        this.getPostTrend();
        this.getArticleTrend();
    },
    methods: {
        // 格式化时间
        formatDate(date) {
            return new Date(date).toLocaleString();
        },
        // 检查用户登录状态
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

        // 获取热门帖子列表
        getPostTrend() {
            axios.get('/api_forum/trendPost/')
                .then(response => {
                    this.trendPost = response.data;
                    console.log(this.trendPost);
                })
                .catch(error => {
                    console.error('Error:', error);
                });
        },

        // 获取热门文章列表
        getArticleTrend() {
            axios.get('/api_article/trendArticle/')
                .then(response => {
                    this.trendArticle = response.data;
                    console.log(this.trendArticle);
                })
                .catch(error => {
                    console.error('Error:', error);
                });
        },

        // 搜索按钮
        search() {
            console.log(this.searchText)
            if (!this.searchText) {
                ElMessage.warning('搜索内容为空，请检查您的输入！');
                return;
            }
            this.searchArticle();
            this.searchPost();
        },

        // 搜索帖子
        searchPost() {
            axios.get('/api_forum/searchPost/', {
                params: {
                    search: this.searchText
                }
            })
                .then(response => {
                    this.posts = response.data;
                    console.log(this.posts);
                })
                .catch(error => {
                    console.error('Error:', error);
                });
        },

        // 搜索文章
        searchArticle() {
            // 发送GET请求
            axios.get('/api_article/searchArticle/', {
                params: {
                    search: this.searchText
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

        goToPostDetail(postId, idViewNum) {
            // 更新浏览量
            axios.patch(`/api_forum/post/${postId}/`, {
                ViewNum: idViewNum + 1, // 假设点赞成功后数量加1
            }).then(response => {
                // 更新文章点赞数量成功后，刷新评论列表
                console.log(response.data)
            }).catch(error => {
                console.error('Error updating like count:', error);
            });
            // 使用 Vue Router 导航到文章详情页面，并传递 postId 作为参数
            this.$router.push({ name: 'post', params: { id: postId } });
        }
    }
}
</script>