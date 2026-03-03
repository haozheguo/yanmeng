<template>
    <div class="max-w-7xl mx-auto grid grid-cols-7 gap-4">
        <div class="mt-8 main-left col-span-2">
            <div v-if="isLoggedIn" class="p-4 bg-white border border-gray-200 text-center rounded-xl">
                <img class="w-20 h-20 rounded-full mx-auto mb-2" :src="userInfo.avatar" alt="User avatar">
                <h2 class="text-xl font-bold">{{ userInfo.name }}</h2>
                <div class="text-xs rounded-full py-1 px-3 mt-2 mb-1 inline-block"
                    :class="{ 'bg-green-400 text-white': userInfo.is_vip, 'bg-blue-400 text-white': userInfo.is_vip === false }">
                    {{ userInfo.is_vip ? 'VIP用户' : '普通用户' }}
                </div>
                <div class="text-sm text-gray-500 mt-1">
                    研梦值：{{ userInfo.ymvalue }}
                </div>
                <div class="flex justify-around items-center mt-4">
                        <input type="file" @change="uploadAvatarImg" style="display: none" ref="uploader">
                        <button @click="$refs.uploader.click()" class="py-2 px-8 bg-green-500 text-white rounded-3xl block">
                        修改头像
                        </button>
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
        </div>

        <div class="mt-8 main-center col-span-5">
            <ul class="flex border-b">
                <li v-for="(tab, index) in tabs" :key="index" class="mr-1">
                    <button class="bg-white inline-block py-2 px-4 rounded-xl hover:text-blue-500"
                        :class="{ 'ext-blue-5t00 bg-gray-200 border-b-2 border-blue-500': activeTab === tab }"
                        @click="tabBar(tab)">
                        {{ tab }}
                    </button>
                </li>
            </ul>
            <div v-if="activeTab === '文章收藏'">
                <div v-if="collectArticles.length === 0"
                    class="mt-4 p-4 bg-white border border-gray-200 rounded-xl flex flex-col items-center">
                    <p class="text-gray-500 text-xl mt-8">亲爱的研梦er，这里空空如也~</p>
                    <img src="http://127.0.0.1:8000/media/svg/empty.svg" class="w-1/2 mt-4">
                </div>

                <div v-for="(article, index) in collectArticles" :key="index"
                    @click="goToArticleDetail(article.id, article.is_vip, article.ViewNum)"
                    class="mt-4 p-4 bg-white border border-gray-200 rounded-xl hover:bg-blue-100">
                    <div class="flex items-center space-x-1">
                        <div class="border-2 border-blue-500 h-6 mx-2"></div>
                        <h2 class="text-xl font-bold">{{ article.title }}</h2>
                        <div v-if="article.is_vip"
                            class=" text-xs text-white border bg-orange-400 border-orange-500 rounded-full px-2">VIP专属
                        </div>
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

            <div v-if="activeTab === '帖子收藏'">
                <div v-if="collectPosts.length === 0" class="mt-4 p-4 bg-white border border-gray-200 rounded-xl flex flex-col items-center">
                    <p class="text-gray-500 text-xl mt-8">亲爱的研梦er，这里空空如也~</p>
                    <img src="http://127.0.0.1:8000/media/svg/empty.svg" class="w-1/2 mt-4">
                </div>
                <div v-for="(post, index) in collectPosts" :key="index" @click="goToPostDetail(post.id, post.ViewNum)"
                class="p-4 mt-4 bg-white border border-gray-200 rounded-xl hover:bg-blue-100">
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

            <!-- 添加更多的 div 来显示其他 tab 的内容 -->
            <div v-if="activeTab === '我的文章'">
                <div v-if="myArticles.length === 0"
                    class="mt-4 p-4 bg-white border border-gray-200 rounded-xl flex flex-col items-center">
                    <p class="text-gray-500 text-xl mt-8">亲爱的研梦er，这里空空如也~</p>
                    <img src="http://127.0.0.1:8000/media/svg/empty.svg" class="w-1/2 mt-4">
                </div>

                <div v-for="(article, index) in myArticles" :key="index"
                    class="mt-4 p-4 bg-white border border-gray-200 rounded-xl hover:bg-blue-100">
                    <div class="flex justify-between items-center">
                        <div class="flex items-center space-x-1">
                            <div class="border-2 border-blue-500 h-6 mx-2"></div>
                            <h2 class="text-xl font-bold">{{ article.title }}</h2>
                            <div v-if="article.is_vip" class="text-xs text-white border bg-orange-400 border-orange-500 rounded-full px-2">
                                VIP专属
                            </div>
                        </div>
                        <div class="flex justify-around items-center">
                            <button @click="deleteArticle(article.id)" class="px-4 py-1 bg-red-500 text-white text-sm rounded-full">删除</button>
                        </div>
                        
                    </div>
                    <div @click="goToArticleDetail(article.id, article.is_vip, article.ViewNum)">
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
            </div>

            <div v-if="activeTab === '我的帖子'">
                <div v-if="myPosts.length === 0"
                    class="mt-4 p-4 bg-white border border-gray-200 rounded-xl flex flex-col items-center">
                    <p class="text-gray-500 text-xl mt-8">亲爱的研梦er，这里空空如也~</p>
                    <img src="http://127.0.0.1:8000/media/svg/empty.svg" class="w-1/2 mt-4">
                </div>

                <div v-for="(post, index) in myPosts" :key="index"
                class="p-4 mt-4 bg-white border border-gray-200 rounded-xl hover:bg-blue-100">
                    <div class="flex justify-between items-center">
                        <div class="flex items-center space-x-1">
                            <img :src="post.author.avatar" alt="author's avatar" class="w-10 h-10 rounded-full">
                            <div>
                                <span class="font-bold ml-2">{{ post.author.name }}</span>
                                <span v-if="post.author.is_vip"
                                class="ml-2 text-sm text-white border bg-orange-400 border-orange-500 rounded-full px-1">VIP用户</span>
                            </div>
                        </div>
                        <div class="flex justify-around items-center">
                            <button @click="deletePost(post.id)" class="px-4 py-1 bg-red-500 text-white text-sm rounded-full">删除</button>
                        </div>
                    </div>
                    
                    <div @click="goToPostDetail(post.id, post.ViewNum)">
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
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import { ElMessage, ElMessageBox } from 'element-plus';

export default {
    data() {
        return {
            isLoggedIn: false,
            userInfo: {},
            img: '',
            myArticles: [],
            myPosts: [],
            collectArticles: [],
            collectPosts:[],
            activeTab: '我的文章',
            tabs: ['我的文章', '我的帖子', '文章收藏', '帖子收藏',], // 添加更多的 tab 名称
        };
    },
    created() {
        // 在组件创建时检查用户登录状态
        this.checkLoginStatus();
        this.getMyArticles();
    },
    methods: {
        // 格式化时间
        formatDate(date) {
            return new Date(date).toLocaleString();
        },
        
        // 上传图片
        async uploadAvatarImg(event) {
            const file = event.target.files[0]
            if (!file) return

            try {
                const formData = new FormData()
                formData.append('file', file)
                formData.append('folder', 'avator')
                const uploadRes = await axios.post('/api_user/upload/', formData, {
                    headers: { 'Content-Type': 'multipart/form-data' }
                })
                this.img = uploadRes.data.url
                // console.log(this.img)
                axios.patch(`/api_user/users/${this.userInfo.id}/`, { avatar:this.img })
                .then(response => {
                    // 删除成功后，刷新文章列表
                    this.userInfo.avatar = this.img;
                    localStorage.setItem('user', JSON.stringify(this.userInfo));
                    ElMessage.success('头像上传成功');
                })
                .catch(error => {
                    // 处理错误
                    console.error('Error deleting article:', error);
                });
            } catch (err) {
                console.error(err)
            }
        },

        // 检查用户登录状态
        checkLoginStatus() {
            // 检查 localStorage 或其他适合的方式来确定用户是否已
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
        // 退出登录
        logOut() {
            localStorage.removeItem('user');
            this.isLoggedIn = false;
            this.userInfo = {};
        },

        // 跳转功能实现
        tabBar(tab) {
            this.activeTab = tab;
            if (tab == '我的文章') {
                // console.log('我的文章')
                this.getMyArticles();
            }
            if (tab == '我的帖子') {
                // console.log('我的帖子')
                this.getMyPosts();
            }
            if(tab == '文章收藏') {
                this.getArticleCollection();
            }
            if(tab == '帖子收藏') {
                console.log('帖子收藏')
                this.getPostCollection();
            }
        },
        // 获取自己发布的文章列表
        getMyArticles() {
            // 发送GET请求
            axios.get('/api_article/getWriteArticlelist/', {
                params: {
                    user_id: this.userInfo.id
                }
            })
                .then(response => {
                    // 更新文章列表数据
                    this.myArticles = response.data;
                    console.log(this.myArticles);
                })
                .catch(error => {
                    // 处理错误
                    console.error('Error:', error);
                });
        },
        // 获取收藏文章列表
        getArticleCollection() {
            // 发送GET请求
            axios.get('/api_article/getCollectArticlelist/', {
                params: {
                    user_id: this.userInfo.id
                }
            })
                .then(response => {
                    // 更新文章列表数据
                    this.collectArticles = response.data;
                    console.log(this.collectArticles);
                })
                .catch(error => {
                    // 处理错误
                    console.error('Error:', error);
                });
        },
        // 删除指定文章
        deleteArticle(articleId) {
            ElMessageBox.confirm('您确定要删除该文章吗？', '提示', {
                confirmButtonText: '确定',
                cancelButtonText: '取消',
                type: 'warning'
            }).then(() => {
            // 发送 DELETE 请求
            axios.patch(`/api_article/article/${articleId}/`, { is_delete: true })
            .then(response => {
                // 删除成功后，刷新文章列表
                this.getMyArticles();
                ElMessage.success('您已成功删除该文章');
            })
            .catch(error => {
                // 处理错误
                console.error('Error deleting article:', error);
            });
            }).catch(() => {
                // 用户点击取消按钮后的操作，这里可以不做任何处理
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
        // 获取发布帖子列表
        getMyPosts(){
            axios.get('/api_forum/getWritePostlist/',{
                params:{
                    author_id:this.userInfo.id
                }
            }).then(response => {
                    // 更新文章列表数据
                    this.myPosts = response.data;
                    console.log(this.myPosts);
                })
                .catch(error => {
                    // 处理错误
                    console.error('Error:', error);
                });
        },
        // 删除指定文章
        deletePost(postId) {
            ElMessageBox.confirm('您确定要删除该帖子吗？', '提示', {
                confirmButtonText: '确定',
                cancelButtonText: '取消',
                type: 'warning'
            }).then(() => {
            // 发送 DELETE 请求
            axios.patch(`/api_forum/post/${postId}/`, { is_delete: true })
            .then(response => {
                // 删除成功后，刷新文章列表
                this.getMyPosts();
                ElMessage.success('您已成功删除该帖子！');
            })
            .catch(error => {
                // 处理错误
                console.error('Error deleting article:', error);
            });
            }).catch(() => {
                // 用户点击取消按钮后的操作，这里可以不做任何处理
            });
        },
        // 获取收藏帖子列表
        getPostCollection(){
            axios.get('/api_forum/getCollectedPost/',{
                params:{
                    author_id:this.userInfo.id
                }
            }).then(response => {
                    // 更新文章列表数据
                    this.collectPosts = response.data;
                    console.log(this.collectPosts);
                })
                .catch(error => {
                    // 处理错误
                    console.error('Error:', error);
                });
        },

        // 跳转到帖子详情页面
        goToPostDetail(postId, idViewNum) {
            // 更新浏览量
            axios.patch(`/api_forum/post/${postId}/`, {
                ViewNum: idViewNum + 1, // 假设点赞成功后数量加1
            }).then(response => {
            // 更新文章点赞数量成功后，刷新评论列表
            // console.log(response.data)
            }).catch(error => {
                console.error('Error updating like count:', error);
            });
            // 使用 Vue Router 导航到文章详情页面，并传递 postId 作为参数
            this.$router.push({ name: 'post', params: { id: postId } });
        },

    },
}
</script>
