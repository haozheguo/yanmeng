<template>
    <div class="max-w-7xl mx-auto mt-4 grid grid-cols-4 gap-4">
        <div class="bg-white p-4 rounded-xl">
            <div class="flex items-center space-x-1">
                <div class="border-2 border-blue-500 h-6 mx-2"></div>
                <div class="font-bold text-xl">入库文章总数</div>
            </div>
            <div class="mt-2 text-5xl text-center text-blue-500 font-bold">{{ allNum }}</div>
        </div>
        <div class="bg-white p-4 rounded-xl">
            <div class="flex items-center space-x-1">
                <div class="border-2 border-blue-500 h-6 mx-2"></div>
                <div class="font-bold text-xl">
                    <span class="text-blue-500">
                        "研招网"</span>来源文章数
                </div>
            </div>
            <div class="mt-2 text-5xl text-center text-blue-500 font-bold">{{ yanzhaoNum }}</div>
        </div>
        <div class="bg-white p-4 rounded-xl">
            <div class="flex items-center space-x-1">
                <div class="border-2 border-blue-500 h-6 mx-2"></div>
                <div class="font-bold text-xl"><span class="text-blue-500">
                        "微信"</span>来源文章数</div>
            </div>
            <div class="mt-2 text-5xl text-center text-blue-500 font-bold">{{ wechatNum }}</div>
        </div>
        <div class="bg-white p-4 rounded-xl">
            <div class="flex items-center space-x-1">
                <div class="border-2 border-blue-500 h-6 mx-2"></div>
                <div class="font-bold text-xl"><span class="text-blue-500">
                        "百度"</span>来源文章数</div>
            </div>
            <div class="mt-2 text-5xl text-center text-blue-500 font-bold">{{ baiduNum }}</div>
        </div>
    </div>
    <div class="max-w-7xl mx-auto mt-4 grid grid-cols-3 gap-4">
        <div class="bg-white rounded-xl p-4">
            <div class="flex items-center space-x-1">
                <div class="border-2 border-blue-500 h-6 mx-2"></div>
                <div class="font-bold text-xl"><span class="text-blue-500">
                        "研招网"</span>最新文章</div>
            </div>
            <div v-for="(article, index) in yanzhaoList" :key="index" class="hover:bg-gray-100 mt-2 rounded-xl">
                <a :href="article.url" target="_blank" class="font-mono hover:font-sans">
                    <div>
                        <span class="font-bold text-blue-500 ml-8 mr-2">{{ index + 1 }}.</span>
                        {{ article.title.substring(0, 18) }}
                    </div>
                    <div class="flex justify-between">
                        <div>
                            <span class="text-sm text-gray-400 ml-8 mr-2">{{ formatDate(article.created_time) }}</span>
                            <span class="text-sm text-blue-500">{{ article.emotion }}</span>
                        </div>
                    </div>
                </a>
            </div>

        </div>
        <div class="bg-white rounded-xl p-4">
            <div class="flex items-center space-x-1">
                <div class="border-2 border-blue-500 h-6 mx-2"></div>
                <div class="font-bold text-xl"><span class="text-blue-500">
                        "微信"</span>最新文章</div>
            </div>
            <div v-for="(article, index) in wechatList" :key="index" class="hover:bg-gray-100 mt-2 rounded-xl">
                <a :href="article.url" target="_blank" class="font-mono hover:font-sans">
                    <div>
                        <span class="font-bold text-blue-500 ml-8 mr-2">{{ index + 1 }}.</span>
                        {{ article.title.substring(0, 18) }}
                    </div>
                    <div class="flex justify-between">
                        <div>
                            <span class="text-sm text-gray-400 ml-8 mr-2">{{ formatDate(article.created_time) }}</span>
                            <span class="text-sm text-blue-500">{{ article.emotion }}</span>
                        </div>
                    </div>
                </a>
            </div>

        </div>
        <div class="bg-white rounded-xl p-4">
            <div class="flex items-center space-x-1">
                <div class="border-2 border-blue-500 h-6 mx-2"></div>
                <div class="font-bold text-xl"><span class="text-blue-500">
                        "百度"</span>最新文章</div>
            </div>
            <div v-for="(article, index) in baiduList" :key="index" class="hover:bg-gray-100 mt-2 rounded-xl">
                <a :href="article.url" target="_blank" class="font-mono hover:font-sans">
                    <div>
                        <span class="font-bold text-blue-500 ml-8 mr-2">{{ index + 1 }}.</span>
                        {{ article.title.substring(0, 18) }}
                    </div>
                    <div class="flex justify-between">
                        <div>
                            <span class="text-sm text-gray-400 ml-8 mr-2">{{ formatDate(article.created_time) }}</span>
                            <span class="text-sm text-blue-500">{{ article.emotion }}</span>
                        </div>
                    </div>
                </a>
            </div>

        </div>

    </div>

    <div class="max-w-7xl mx-auto mt-4 grid grid-cols-3 gap-4">
        <div class="bg-white p-4 rounded-xl">
            <div class="flex items-center space-x-1">
                <div class="border-2 border-blue-500 h-6 mx-2"></div>
                <div class="font-bold text-xl">情感分析</div>
            </div>
            <div id="emotion" style="width: 100%;height: 300px;"></div>
        </div>
        <div class="bg-white p-4 rounded-xl">
            <div class="flex items-center space-x-1">
                <div class="border-2 border-blue-500 h-6 mx-2"></div>
                <div class="font-bold text-xl">词云可视化</div>
            </div>
            <div id="wordcloud" style="width: 100%;height: 300px;"></div>
        </div>
        <div class="bg-white p-4 rounded-xl">
            <div class="flex items-center space-x-1">
                <div class="border-2 border-blue-500 h-6 mx-2"></div>
                <div class="font-bold text-xl">关键词统计</div>
            </div>
            <div id="treechart" style="width: 100%;height: 300px;"></div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import * as echarts from 'echarts';
import 'echarts-wordcloud';

export default {
    data() {
        return {
            allNum: 0,
            yanzhaoNum: 0,
            wechatNum: 0,
            baiduNum: 0,
            positiveNum: 0,
            normalNum: 0,
            negativeNum: 0,
            yanzhaoList: [],
            wechatList: [],
            baiduList: [],

            emotionChart: null,
            emotionData: [],
            wordChart: null,
            wordCloudData: [
                { name: '考研', value: 100 },
                { name: '经验分享', value: 80 },
                { name: '复试准备', value: 70 },
                { name: '上岸', value: 60 },
                { name: '考研人数', value: 50 },
                { name: '心路历程', value: 40 },
                { name: '院校选择', value: 30 },
                { name: '报录比', value: 20 },
                { name: '解压', value: 10 }
            ],
            treeChart: null
        }
    },
    // vue路由守卫，用来销毁 ECharts 实例
    beforeRouteLeave(to, from, next) {
        // 调用方法销毁 ECharts 实例
        this.destroyEmotionChart();
        this.destroywordChart();
        this.destroytreeChart();
        next();
    },
    mounted() {
        this.getTrendData();
        this.getKeywordData();
        // this.initWordCloud();
        // this.initTreeChart();
    },
    methods: {
        // 格式化时间为年月日
        formatDate(date) {
            // 只保留年月日
            const formatter = new Intl.DateTimeFormat('zh-CN', {
                year: 'numeric',
                month: '2-digit',
                day: '2-digit'
            });
            return formatter.format(new Date(date));

        },

        // 初始化渲染数据
        getTrendData() {
            axios.get('/api_scrapy/getScrapylist/')
                .then(response => {
                    const data = response.data;
                    this.allNum = data.allNum;
                    this.yanzhaoNum = data.yanzhaoNum;
                    this.wechatNum = data.wechatNum;
                    this.baiduNum = data.baiduNum;
                    this.positiveNum = data.positiveNum;
                    this.normalNum = data.normalNum;
                    this.negativeNum = data.negativeNum;
                    this.yanzhaoList = data.yanzhaoList;
                    this.wechatList = data.wechatList;
                    this.baiduList = data.baiduList;
                    // 根据返回的数据更新 emotionData
                    this.emotionData = [
                        { value: data.negativeNum, name: '消极' },
                        { value: data.normalNum, name: '中性' },
                        { value: data.positiveNum, name: '积极' },
                    ];
                    this.initEmotionChart();
                })
                .catch(error => {
                    console.error('Error fetching data:', error);
                });
        },
        // 获得词云数据
        getKeywordData() {
            axios.get('/api_scrapy/getScrapyKeywords/')
                .then(response => {
                    const data = response.data;
                    this.wordCloudData = data;
                    this.initWordCloud();
                    this.initTreeChart();
                })
                .catch(error => {
                    console.error('Error fetching data:', error);
                });
        },

        // 初始化情感分析饼状图
        initEmotionChart() {
            console.log(this.emotionData)
            // 基于准备好的dom，初始化echarts实例
            this.emotionChart = echarts.init(document.getElementById('emotion'));
            // 配置项和数据
            const option = {
                tooltip: {
                    trigger: 'item'
                },
                legend: {
                    top: '5%',
                    left: 'center'
                },
                series: [
                    {
                        name: '情感分析',
                        type: 'pie',
                        radius: ['40%', '70%'],
                        avoidLabelOverlap: false,
                        label: {
                            show: false,
                            position: 'center'
                        },
                        emphasis: {
                            label: {
                                show: true,
                                fontSize: 40,
                                fontWeight: 'bold'
                            }
                        },
                        labelLine: {
                            show: false
                        },
                        data: this.emotionData
                    }
                ]
            };

            // 使用刚指定的配置项和数据显示图表。
            option && this.emotionChart.setOption(option);
        },
        // 销毁情感分析饼状图
        destroyEmotionChart() {
            if (this.emotionChart) {
                this.emotionChart.dispose();
                console.log('情感分析饼状图销毁了')
            }
        },
        initWordCloud() {
            this.wordChart = echarts.init(document.getElementById('wordcloud'));
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
            option && this.wordChart.setOption(option);
            //随着屏幕大小调节图表
            window.addEventListener("resize", () => {
                this.wordChart.resize();
            });
            // 将 myChart 存储在组件的数据中，以便在销毁时使用
            console.log('词云图创建了');
        },
        // 销毁词云图
        destroywordChart() {
            if (this.wordChart) {
                this.wordChart.dispose();
                console.log('词云图销毁了')
            }
        },
        // 初始化磁盘图
        initTreeChart() {
            this.treeChart = echarts.init(document.getElementById('treechart'));
            const option = {
                series: [
                    {
                        type: 'treemap',
                        data: this.wordCloudData
                    }
                ]
            };
            option && this.treeChart.setOption(option);
        },
        // 销毁磁盘图
        destroytreeChart() {
            if (this.treeChart) {
                this.treeChart.dispose();
                console.log('磁盘图销毁了')
            }
        },
    }
}

</script>