<template>
    <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
        <div class="mt-8 main-center col-span-3 ">
            <div class="p-4 bg-white border border-gray-200 rounded-lg">
                <div v-if="post.author" class="flex items-center space-x-1">
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
            <div class="mt-4 bg-white p-6 rounded-2xl shadow-md">
                <div class="flex items-center space-x-1">
                    <div class="border-2 border-blue-500 h-6 mx-2"></div>
                    <h2 class="text-xl font-bold">发表评论</h2>
                </div>

                <form @submit.prevent="submitComment" class="mt-2">
                    <textarea v-model="commentContent" class="w-full p-2 border rounded-md" rows="4"
                        placeholder="欢迎你加入研梦大家庭，记得友善发言哦！"></textarea>
                    <button type="submit"
                        class="mt-4 bg-blue-500 hover:bg-blue-300 text-white font-bold py-2 px-4 rounded">
                        发布
                    </button>
                </form>
            </div>

            <div v-for="comment in comments" :key="comment.id" class="my-4 bg-white p-6 rounded-2xl shadow-md">
                <div class="flex items-start space-x-4">
                    <img v-if="comment.author.avatar" :src="comment.author.avatar" alt="User Avatar"
                        class="w-10 h-10 rounded-full">
                    <div class="flex-1">
                        <div class="flex justify-between">
                            <div>
                                <span class="font-bold">{{ comment.author.name }}</span>
                                <span v-if="comment.author.is_vip"
                                    class="ml-2 text-sm text-white border bg-orange-400 border-orange-500 rounded-full px-1">VIP用户</span>
                            </div>
                            <div class="text-sm text-gray-500">{{ formatDate(comment.created_at) }}</div>
                        </div>
                        <p class="mt-2">{{ comment.content }}</p>
                    </div>
                </div>
            </div>
        </div>

        <div class="mt-8 main-right col-span-1">
            <div v-if="isLoggedIn" class="p-4 bg-white border border-gray-200 text-center rounded-lg">
                <img class="w-20 h-20 rounded-full mx-auto mb-2" :src="userInfo.avatar" alt="User avatar">
                <h2 class="text-xl font-bold">{{ userInfo.name }}</h2>
                <div class="text-xs rounded-full py-1 px-3 mt-2 mb-1 inline-block"
                    :class="{ 'bg-green-400 text-white': userInfo.is_vip, 'bg-blue-400 text-white': !userInfo.is_vip }">
                    {{ userInfo.is_vip ? 'VIP用户' : '普通用户' }}
                </div>
                <div class="text-sm text-gray-500 mt-1">
                    研梦值：{{ userInfo.ymvalue }}
                </div>
                <div>
                    <button @click="submitLike"
                        class="bg-green-500 hover:bg-green-700 text-white font-bold py-1 px-4 rounded-full mt-4">👍点赞</button>
                </div>
                <div>
                    <button @click="collectPost"
                        class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-1 px-4 rounded-full mt-4">⭐收藏</button>
                </div>

            </div>

            <div v-else class="p-4 bg-white border border-gray-200 text-center rounded-lg">

                <div class="flex items-center space-x-1">
                    <div class="border-2 border-blue-500 h-6 mx-2"></div>
                    <h2 class="text-xl font-bold">登录享受更多权益</h2>
                </div>
                <RouterLink to="/login">
                    <div class="flex justify-around items-center mt-4">
                        <button class="px-8 py-2 bg-blue-500 text-white rounded-lg">登录</button>
                    </div>
                </RouterLink>

                <RouterLink to="/signup">
                    <div class="flex justify-around items-center mt-4">
                        <button class="px-8 py-2 bg-gray-500 text-white rounded-lg">注册</button>
                    </div>
                </RouterLink>
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
            isLoggedIn: false,
            userInfo: {},
            post: {},
            commentContent: '',
            comments: [],
        }
    },
    created() {
        this.getPost();
        this.getComments();
        this.checkLoginStatus();
    },
    methods: {
        // 格式化时间
        formatDate(date) {
            return new Date(date).toLocaleString();
        },

        // 获取帖子内容
        getPost() {
            axios.get('/api_forum/getPostlist/', {
                params: {
                    id: this.$route.params.id
                }
            })
                .then(response => {
                    // 更新文章列表数据
                    this.post = response.data;
                })
                .catch(error => {
                    // 处理错误
                    console.error('Error:', error);
                });
        },

        // 收藏帖子
        collectPost(){
            if(!this.isLoggedIn) {
                ElMessage.warning('请先登录再执行收藏动作！');
                return;
            }
            console.log(this.userInfo.id, this.$route.params.id,this.post.id)
            axios.get('/api_forum/collectPost/', {
                params: {
                    author_id: this.userInfo.id,
                    post_id: this.post.id
                }
            })
                .then(response => {
                    console.log('Response data:', response.data);
                    const { type } = response.data;
                    if (type === true) {
                        // 新的收藏记录已创建
                        ElMessage.success('帖子已成功收藏！');
                    } else {
                        // 收藏记录已存在，收藏时间已更新
                        ElMessage.warning('您已经收藏过该帖子！');
                    }
                })
                .catch(error => {
                    console.error('There was a problem with the request:', error);
                });
        },
        // 文章收藏
        collectArticle() {
            if (!this.isLoggedIn) {
                ElMessage.warning('请先登录！');
                return;
            }
            const id = this.post.id;
            console.log(id)
            console.log('Collect article:', this.$route.params.id, this.userInfo.id,this.post.id)
            axios.get('/api_article/collectArticle/', {
                params: {
                    author_id: Number(this.userInfo.id),
        post_id: Number(this.$route.params.id)
                }
            })
                .then(response => {
                    console.log('Response data:', response.data);
                    const { type } = response.data;
                    if (type === true) {
                        // 新的收藏记录已创建
                        ElMessage.success('文章已成功收藏！');
                    } else {
                        // 收藏记录已存在，收藏时间已更新
                        ElMessage.warning('您已经收藏过该文章！');
                    }
                })
                .catch(error => {
                    console.error('There was a problem with the request:', error);
                });
        },
        // 检查登录状态
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

        // 获取评论列表
        getComments() {
            const postId = this.$route.params.id;
            // 发送GET请求
            axios.get('/api_forum/comments/' + postId)
                .then(response => {
                    // 更新文章列表数据
                    this.comments = response.data;
                    console.log(this.comments);
                })
                .catch(error => {
                    // 处理错误
                    console.error('Error:', error);
                });
        },
        // 点赞帖子
        submitLike() {
            if (!this.isLoggedIn) {
                ElMessage.warning('请先登录再点赞！');
                return;
            }

            axios.post('/api_forum/like/', {
                author: this.userInfo.id,
                post: this.post.id,
            }).then(response => {
                // 成功发送点赞记录后，更新文章点赞数量
                this.updateLikeCount();
            }).catch(error => {
                console.error('Error submitting like:', error);
            });
        },

        // 更新帖子点赞数量
        updateLikeCount() {
            axios.patch(`/api_forum/post/${this.post.id}/`, {
                LikeNum: this.post.LikeNum + 1, // 假设点赞成功后数量加1
            }).then(response => {
                // 更新帖子点赞数量成功后，刷新文章
                this.getPost();
                ElMessage.success('点赞成功！');
            }).catch(error => {
                console.error('Error updating like count:', error);
            });
        },

        // 发表评论
        submitComment() {
            if (!this.isLoggedIn) {
                ElMessage.warning('请先登录再发表评论！');
                return;
            }
            if (!this.commentContent) {
                ElMessage.warning('评论内容不能为空！');
                return;
            }
            axios.post('/api_forum/comment/', {
                content: this.commentContent,
                author: this.userInfo.id,
                post: this.post.id,
            }).then(response => {
                ElMessage.success('成功发表评论！');
                this.commentContent = '';
                this.getComments();
            }).catch(error => {
                console.error('Error submitting comment:', error);
            });
        },
    }
}
</script>