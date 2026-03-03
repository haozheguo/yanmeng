<template>
    <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
        <div class="mt-8 main-center col-span-3 ">
            <div class="bg-white p-6 rounded-2xl shadow-md">
                <div class="flex items-center ">
                    <div class="border-2 border-blue-500 h-8 mx-2"></div>
                    <div class="text-2xl font-bold">{{ article.title }}</div>
                </div>
                <div class="text-gray-600 mt-2">
                    <span>{{ formatDate(article.create_time) }}</span>
                    <span class="mx-2">•</span>
                    <span>浏览量: {{ article.ViewNum }}</span>
                    <span class="mx-2">•</span>
                    <span>点赞量: {{ article.LikeNum }}</span>
                </div>
                <div class="flex justify-between mt-4 ">
                    <div>
                        <span class="font-bold text-xl text-blue-500">#{{ article.category }}</span>
                    </div>
                    <div class="flex">
                        <div class="mx-2">
                            <div class="inline-block bg-blue-100 text-blue-500 rounded-xl border border-blue-500 px-4">
                                {{
                        article.tag1 }}</div>
                        </div>
                        <div class="mx-2">
                            <div class="inline-block bg-blue-100 text-blue-500 rounded-xl border border-blue-500 px-4">
                                {{
                        article.tag2 }}</div>
                        </div>
                        <div class="mx-2">
                            <div class="inline-block bg-blue-100 text-blue-500 rounded-xl border border-blue-500 px-4">
                                {{
                        article.tag3 }}</div>
                        </div>
                    </div>
                </div>
                <div class="border-t border-blue-300 border-double border-2 mt-4"></div>

                <div class="mt-6 markdown-body" v-html="parseMarkdown(String(article.content))"></div>
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
                    <img :src="comment.user.avatar" alt="User Avatar" class="w-10 h-10 rounded-full">
                    <div class="flex-1">
                        <div class="flex justify-between">
                            <div>
                                <span class="font-bold">{{ comment.user.name }}</span>
                                <span v-if="comment.user.is_vip"
                                    class="ml-2 text-sm text-white border bg-orange-400 border-orange-500 rounded-full px-1">VIP用户</span>
                            </div>
                            <div class="text-sm text-gray-500">{{ formatDate(comment.comment_time) }}</div>
                        </div>
                        <p class="mt-2">{{ comment.content }}</p>
                    </div>
                </div>
            </div>
        </div>

        <div class="mt-8 main-right col-span-1">
            <div class="flex flex-col items-center justify-center bg-white p-4 rounded-xl shadow-md">

                <img v-if="authorInfo.avatar" :src="authorInfo.avatar" alt="Author Avatar"
                    class="w-16 h-16 rounded-full">

                <div class="mt-2 text-xl font-bold">{{ authorInfo.name }}</div>

                <div class="flex items-center mt-1">
                    <span class="text-gray-500 mr-1">研梦值:</span>
                    <span>{{ authorInfo.ymvalue }}</span>
                </div>

                <div class="text-xs rounded-full py-1 px-3 mt-2 mb-1 inline-block"
                    :class="{ 'bg-orange-400 text-white': authorInfo.is_vip, 'bg-blue-400 text-white': !authorInfo.is_vip }">
                    {{ authorInfo.is_vip ? 'VIP用户' : '普通用户' }}
                </div>
            </div>

            <div class="flex flex-col mt-4 justify-center bg-white p-4 rounded-xl shadow-md">
                <div class="flex items-center space-x-1">
                    <div class="border-2 border-blue-500 h-6 mx-2"></div>
                    <h2 class="text-xl font-bold">词云图</h2>
                </div>
                <div id="wordCloud" style="width: 100%; height: 300px;"></div>
            </div>

            <div v-if="isLoggedIn" class="p-4 mt-4 bg-white border border-gray-200 text-center rounded-xl">
                <div>
                    <button @click="submitLike"
                        class="bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded-full my-2">👍点赞</button>
                </div>
                <div>
                    <button @click="collectArticle"
                        class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full my-2">⭐收藏</button>
                </div>
            </div>

            <div v-else class="p-4 mt-4 bg-white border border-gray-200 text-center rounded-xl">

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
import MarkdownIt from 'markdown-it';
import mdHighlight from 'markdown-it-highlightjs';
import markdownItKatex from 'markdown-it-katex';
import MarkdownMath from 'markdown-it-math';
import { ElMessage } from 'element-plus';
import * as echarts from 'echarts';
import 'echarts-wordcloud';

export default {
    name: 'ArticleView',
    data() {
        return {
            article: {},
            authorInfo: {},
            comments: [],
            commentContent: '',
            // 检查用户登录状态
            isLoggedIn: false,
            userInfo: {},
            wordCloudData: [],
            // wordCloudData: [
            //     { name: '考研', value: 100 },
            //     { name: '经验分享', value: 80 },
            //     { name: '复试准备', value: 70 },
            //     { name: '上岸', value: 60 },
            //     { name: '考研人数', value: 50 },
            //     { name: '心路历程', value: 40 },
            //     { name: '院校选择', value: 30 },
            //     { name: '报录比', value: 20 },
            //     { name: '解压', value: 10 },
            //     { name: '2025年', value: 100 },
            //     { name: '官方', value: 80 },
            //     { name: '教育话题', value: 70 },
            //     { name: '缓解焦虑', value: 60 },
            //     { name: '备考策略', value: 50 },
            //     { name: '鸡汤', value: 10 },
            // ],

            myChart: null, // 初始化 myChart
        }
    },
    created() {
        this.checkLoginStatus();
        this.getKeywords();
        this.getArticle();
        this.getComments();
    },
    // vue路由守卫，用来销毁 ECharts 实例
    beforeRouteLeave(to, from, next) {
        // 调用方法销毁 ECharts 实例
        this.destroyWordCloud();
        next();
    },
    methods: {
        // 格式化时间
        formatDate(date) {
            return new Date(date).toLocaleString();
        },

        // markdown解析
        parseMarkdown(content) {
            const md = new MarkdownIt();
            // 如果需要的话，可以在这里添加插件
            md.use(mdHighlight);
            md.use(markdownItKatex);
            md.use(MarkdownMath);
            return md.render(content);
        },

        // 获取文章内容
        getArticle() {
            axios
                .get('/api_article/article/' + this.$route.params.id + '/')
                .then(response => {
                    this.article = response.data;
                    // console.log(this.article);
                    this.getAuthorInfo();
                })
                .catch(error => {
                    console.error('Error fetching article:', error);
                });
        },

        // 获取文章作者信息
        getAuthorInfo() {
            axios
                .get('/api_user/author/' + this.article.author + '/').then(response => {
                    this.authorInfo = response.data;
                    // console.log(this.authorInfo);
                })
        },
        // 文章收藏
        collectArticle() {
            if (!this.isLoggedIn) {
                ElMessage.warning('请先登录！');
                return;
            }
            console.log('Collect article:', this.$route.params.id, this.userInfo.id)
            axios.get('/api_article/collectArticle/', {
                params: {
                    user_id: this.userInfo.id,
                    article_id: this.$route.params.id
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

        // 生成词云图
        generateWordCloud() {
            console.log('你好这是词云表',this.wordCloudData)
            const myChart = echarts.init(document.getElementById('wordCloud'));
            const option = {
                series: [{
                    type: 'wordCloud',
                    shape: 'circle',
                    keepAspect: false,
                    // maskImage: maskImage,
                    left: 'center',
                    top: 'center',
                    width: '100%',
                    height: '90%',
                    right: null,
                    bottom: null,
                    sizeRange: [12, 60],
                    rotationRange: [-90, 90],
                    rotationStep: 45,
                    gridSize: 8, // 调整间距
                    sizeRange: [10, 50], // 调整大小范围
                    drawOutOfBound: false,
                    layoutAnimation: true,
                    textStyle: {
                        fontFamily: 'sans-serif',
                        fontWeight: 'bold',
                        color: function () {
                            return 'rgb(' + [
                                Math.round(Math.random() * 160),
                                Math.round(Math.random() * 160),
                                Math.round(Math.random() * 160)
                            ].join(',') + ')';
                        }
                    },
                    emphasis: {
                        // focus: 'self',
                        textStyle: {
                            textShadowBlur: 1,
                            textShadowColor: '#333'
                        }
                    },
                    data: this.wordCloudData,
                }]
            };
            option && myChart.setOption(option);
            //随着屏幕大小调节图表
            window.addEventListener("resize", () => {
                myChart.resize();
            });
            // 将 myChart 存储在组件的数据中，以便在销毁时使用
            this.myChart = myChart;
            console.log('词云图创建了');
        },


        // 销毁词云图
        destroyWordCloud() {
            if (this.myChart) {
                this.myChart.dispose();
                console.log('词云图销毁了')
            }
        },


        // 获取评论列表
        getComments() {
            const articleId = this.$route.params.id;
            // console.log(articleId)
            // 发送GET请求
            axios.get('/api_article/comments/' + articleId)
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

        // 获取文章关键词
        getKeywords() {
            const articleId = this.$route.params.id;
            axios.get('/api_article/articleKeywords/'+articleId).then(response => {
                // console.log(response.data);
                this.wordCloudData = response.data;
                console.log('关键词获取了',this.wordCloudData);
                this.generateWordCloud();
            })
            .catch(error => {
                console.error('Error:', error);
            })
        },

        // 点赞文章
        submitLike() {
            if (!this.isLoggedIn) {
                ElMessage.warning('请先登录再点赞！');
                return;
            }

            axios.post('/api_article/likearticle/', {
                user: this.userInfo.id,
                article: this.article.id,
            }).then(response => {
                // 成功发送点赞记录后，更新文章点赞数量
                this.updateLikeCount();
            }).catch(error => {
                console.error('Error submitting like:', error);
            });
        },

        // 更新文章点赞数量
        updateLikeCount() {
            axios.patch(`/api_article/article/${this.article.id}/`, {
                LikeNum: this.article.LikeNum + 1, // 假设点赞成功后数量加1
            }).then(response => {
                // 更新文章点赞数量成功后，刷新评论列表
                this.getArticle();
                ElMessage.success('点赞成功！');
            }).catch(error => {
                console.error('Error updating like count:', error);
            });
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
                console.log(this.userInfo);
            } else {
                // 否则，用户未登录
                this.isLoggedIn = false;
            }
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
            axios.post('/api_article/commentarticle/', {
                content: this.commentContent,
                user: this.userInfo.id,
                article: this.article.id,
            }).then(response => {
                ElMessage.success('成功发表评论！');
                this.commentContent = '';
                this.getComments();
            }).catch(error => {
                console.error('Error submitting comment:', error);
            });
        },

    },
}
</script>