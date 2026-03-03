<template>
    <div class="max-w-9xl mx-auto grid grid-cols-5 gap-4">
        <div class="mt-12 main-center col-span-5">
            <!-- 主要介绍界面 -->
    <section class="section"> 
        <!-- is-large w -->
        <!-- 顶部显示的大盒子，第一行是logo，第二行是slogan，第三行是立即使用的button -->
        <div class="top_area mt-8">
            <!-- logo -->
            <div class="logo_line">
                <div class="logo_img">
                    <img src="http://127.0.0.1:8000/media/img/logo.svg" alt="" />
                </div>
                <div class="logo_text">
                    <img src="http://127.0.0.1:8000/media/img/logo_text.svg" alt="" />
                </div>
            </div>
            <!-- slogan --> 
            <div class="slogan title" id="random_symbol">通往<span class="text-blue-600">研途</span>的贴心助手</div>
            <!-- 立即使用按钮 -->
            <div class="rightnow_button_box mt-4">
                    <button @click="gotoHomePage" class="button is-link rightnow_button">
                    <span class="rightnow_button_text">立即使用</span>
                    <div class="button_img">
                        <img src="http://127.0.0.1:8000/media/img/redirect.svg" alt="Click Me" />
                    </div>
                </button>
            </div>
        </div>
        <!-- 底部card部分，每个card分三个部分,最上面矢量图标，然后是其他软件的缺点
            然后是我们软件的特点 -->
        <div class="bottom_area ">
            <!-- card1 -->
            <div class="card" id="card1">
                <div class="card-content">
                    <!-- card1的图标 -->
                    <div class="card-image">
                        <figure class="image is-4by3" id="userinfo_image">
                            <img src="http://127.0.0.1:8000/media/img/userinfo.svg"
                                alt="User Info" />
                        </figure>
                    </div>
                    <!-- card1的title-->
                    <div class="title card_title">用户信息</div>
                    <!-- card1的其他软件的缺点 -->
                    <div class="subtitle negative_subtitle">
                        <span>信息繁杂，登录<strong>繁琐</strong>?</span><br />
                        <span>难管空间，难理收藏?</span>
                        <img src="http://127.0.0.1:8000/media/img/dissatisfy.svg" alt="negative" />
                    </div>
                    <!-- card1的我们软件的特点 -->
                    <div class="subtitle postive_subtitle">
                        个性定制，学习无忧
                    </div>
                    <div class="content postive_discription">
                        <span>一键登录，专属空间待君享</span><br />
                        <span>收藏文章，足迹清晰不迷航</span><br />
                        <span>完善信息，风采尽展更出众</span><br />
                        <span>升级会员，特权尽享<strong>乐无穷</strong></span>
                        <img src="http://127.0.0.1:8000/media/img/satisfy.svg" alt="satisfy" />
                    </div>
                </div>
            </div>
            <!-- card2 -->
            <div class="card" id="card2">
                <div class="card-content">
                    <!-- card2的图标 -->
                    <div class="card-image">
                        <figure class="image is-4by3" id="image_64">
                            <img src="http://127.0.0.1:8000/media/img/puzzle.svg" alt="Puzzle" />
                        </figure>
                    </div>
                    <!-- card2的title-->
                    <div class="title card_title">信息整合</div>
                    <!-- card2的其他软件的缺点 -->
                    <div class="subtitle negative_subtitle">
                        <span>信息分散，查找艰难?</span><br />
                        <span>热门混杂，<strong>一眼难辨</strong>?</span>
                        <img src="http://127.0.0.1:8000/media/img/dissatisfy.svg" alt="negative" />
                    </div>
                    <!-- card2的我们软件的特点 -->
                    <div class="subtitle postive_subtitle">
                        一网打尽，热门尽在眼前
                    </div>
                    <div class="content postive_discription">
                        <span>分类浏览，标签速达目标明</span><br />
                        <span>热门文章，一览无遗尽收眼底</span><br />
                        <span>每周排行，热点追踪不失手</span><br />
                        <span>整合信息，学习高效<strong>更轻松</strong></span>
                        <img src="http://127.0.0.1:8000/media/img/satisfy.svg" alt="satisfy" />
                    </div>
                </div>
            </div>
            <!-- card3 -->
            <div class="card" id="card3">
                <div class="card-content">
                    <!-- card3的图标 -->
                    <div class="card-image">
                        <figure class="image is-4by3" id="userinfo_image">
                            <img src="http://127.0.0.1:8000/media/img/forum.svg" alt="Forum" />
                        </figure>
                    </div>
                    <!-- card3的title-->
                    <div class="title card_title">论坛交流</div>
                    <!-- card3的其他软件的缺点 -->
                    <div class="subtitle negative_subtitle">
                        <span><strong>氛围冷清</strong>，讨论难寻?</span><br />
                        <span>身份不明，信任难存?</span>
                        <img src="http://127.0.0.1:8000/media/img/dissatisfy.svg" alt="negative" />
                    </div>
                    <!-- card3的我们软件的特点 -->
                    <div class="subtitle postive_subtitle">
                        学霸汇聚，智慧共享
                    </div>
                    <div class="content postive_discription">
                        <span>发帖交流，心得分享共成长</span><br />
                        <span>精选回答，智慧指引迷津破</span><br />
                        <span>周活跃度，激励前行勇攀峰</span><br />
                        <span>智慧碰撞，学习之旅<strong>更有趣</strong></span>
                        <img src="http://127.0.0.1:8000/media/img/satisfy.svg" alt="satisfy" />
                    </div>
                </div>
            </div>
            <!-- card4 -->
            <div class="card" id="card4">
                <div class="card-content">
                    <!-- card4的图标 -->
                    <div class="card-image">
                        <figure class="image is-4by3" id="userinfo_image">
                            <img src="http://127.0.0.1:8000/media/img/ai.svg" alt="AI" />
                        </figure>
                    </div>
                    <!-- card4的title-->
                    <div class="title card_title">智能集成</div>
                    <!-- card4的其他软件的缺点 -->
                    <div class="subtitle negative_subtitle">
                        <span>推送不准，<strong>内容脱节</strong>?</span><br />
                        <span>缺乏深析，难觅真值?</span>
                        <img src="http://127.0.0.1:8000/media/img/dissatisfy.svg" alt="negative" />
                    </div>
                    <!-- card4的我们软件的特点 -->
                    <div class="subtitle postive_subtitle">
                        智能推荐，学习更懂你
                    </div>
                    <div class="content postive_discription">
                        <span>深度分析，词云呈现要点清</span><br />
                        <span>智能推送，精选文章更懂你</span><br />
                        <span>考研资讯，热点动态即时知</span><br />
                        <span>智能集成，学习之旅<strong>更轻松</strong></span>
                        <img src="http://127.0.0.1:8000/media/img/satisfy.svg" alt="satisfy" />
                    </div>
                </div>
            </div>

            
        </div>
    </section>

    <!-- 导航栏之下 -->
    <!-- <section class="hero_section">
        <div class="bottom_box">
            <div class="container">
                <div class="title tl1 text-blue-600">研梦</div>
                <div class="tl2" id="random_symbol"></div>
                <div class="title tl3">倾心打造</div>
                <div class="title tl4">助力学子圆梦平台</div>
            </div>
        </div>

        <div class="hero_video_box">
            <video controls class="hero_video" src="http://127.0.0.1:8000/media/yanemengvideo.mp4"
                autoplay loop></video>
        </div>
        
    </section> -->
        </div>
    </div>
    
</template>

<script>
export default {
    name: 'Home',
    data() {
        return {
            
        }
    },
    methods: {
        gotoHomePage(){
            this.$router.push({path: '/'})
        }
    }
}
</script>

<style scoped>
@import url('https://cdn.jsdelivr.net/npm/bulma@1.0.0/css/bulma.min.css');

/* 渐变 */
body {
    background-color: rgba(255, 255, 255, 0.8);
    /* 使用 rgba() 指定颜色和透明度，数值范围为 0 到 1 */
}

/* 定义彩虹动画 */
@keyframes rainbow {
    0% {
        background: linear-gradient(to right, rgba(255, 0, 0, 0.05), rgba(255, 255, 0, 0.05), rgba(0, 255, 0, 0.05), rgba(0, 255, 255, 0.05), rgba(0, 0, 255, 0.05), rgba(255, 0, 255, 0.05), rgba(255, 0, 0, 0.05));
    }

    100% {
        background: linear-gradient(to right, rgba(255, 0, 0, 0.05), rgba(255, 255, 0, 0.05), rgba(0, 255, 0, 0.05), rgba(0, 255, 255, 0.05), rgba(0, 0, 255, 0.05), rgba(255, 0, 255, 0.05), rgba(255, 0, 0, 0.05));
    }
}

/* 应用动画到 body 元素 */
body {
    animation: rainbow 10s infinite alternate;
    /* 指定动画名称、持续时间、重复次数和方向 */
}

* {
    margin: 0;
    padding: 0;
    font-family: 'Bulma sans-serif';
}

.w {
    /* 版心部分 */
    width: 1872px;
    margin: 0 auto;
}

.navbar {
    height: 84px;
    padding: 14px;
    margin: 0px auto;
    border-radius: 23px;
    align-items: center;
}

.navi-inner-container {
    display: flex;
    /* 水平方向上平均分布子元素 */
    justify-content: space-between;
    background-color: #fafafc;
    border-radius: 38px;
    padding: 0px 30px;
    align-items: center;
}

.logo {
    display: flex;
    /* 使子元素垂直居中对齐 */
    align-items: center;
    margin: 0 10px;
}

.logo_img {
    float: left;
    width: 58px;
}

.logo_text {
    float: left;
    width: 72px;
    margin-left: 10px;
}

#nav {
    margin-left: 1360px;
}

/* 鼠标悬停时下拉菜单链接字体颜色变为蓝色 */
a.navbar-link:hover {
    color: rgb(65, 65, 206);
}

.login_register_button {
    margin: 0 15px;
}

.hero_section {
    height: 900px;
    position: relative;
    z-index: 2;
}

.hero_video_box {
    border-radius: 24px;
    height: 535px;
    overflow: hidden;
    position: relative;
    display: flex;
    justify-content: center;
    align-items: center;
    border: none;
    /* background-color: #fff; */
}

.hero_section .hero_video {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    max-height: 100%;
    border-radius: 24px;
    /* 添加视频的圆角效果 */
    object-fit: cover;
    object-position: center;
    border: none;
    /* 确保没有边框 */
}


.container {
    margin: 30px 80px;
    position: relative;
    /* 让 .container 成为定位上下文 */

}

.bottom_box {
    display: flex;
    justify-content: left;
    align-items: center;
    text-align: left;
    border-radius: 24px;
    height: 340px;
}

.title {
    font-size: 53px;
    margin: 0 10px;
}

.tl1,
.tl2,
.tl3 {
    display: inline-block;
}

.tl1 {
    margin-right: 10px;
}

.tl2 {
    font-size: 45px;
    margin: auto;
}

.tl3 {
    position: absolute;
    /* 设置为绝对定位 */
    top: 0;
    /* 从顶部开始定位 */
    left: 24%;
    transform: translateX(-50%);
    /* 水平居中 */
}

/* 符号随机变化动画 */
@keyframes changeSymbol {

    0%,
    90%,
    95%,
    97% {
        content: "/";
    }

    3%,
    33%,
    63% {
        content: "_";
    }

    6%,
    36%,
    66% {
        content: "[";
    }

    9%,
    39%,
    69% {
        content: "*";
    }

    12%,
    42%,
    72% {
        content: "(";
    }

    15%,
    45%,
    75% {
        content: "]";
    }

    18%,
    48%,
    78% {
        content: "^";
    }

    21%,
    51%,
    81% {
        content: "+";
    }

    24%,
    54%,
    84% {
        content: "*";
    }

    27%,
    57%,
    87% {
        content: "-";
    }

    30%,
    60% {
        content: "~";
    }

    96%,
    98% {
        content: " ";
    }

}

#random_symbol::after {
    content: "/";
    color: rgb(97, 92, 237);
    animation: changeSymbol 5s infinite;
}

/* 主界面顶部区域 */
.top_area {
    display: flex;
    flex-direction: column;
    justify-content: center;
    /* 设置为纵向排列 */
    align-items: center;
    /* height: 100vh;占满整个视口的高度 */
    height: 200px;
}

.logo_line {
    display: flex;
    /* 使子元素垂直居中对齐 */
    align-items: center;
    margin: 0 10px;
}

/* 后代选择器，不同父类相同子类，体现不同效果 */
.logo_line>.logo_img {
    float: left;
    width: 100px;
}

.logo_line>.logo_text {
    float: left;
    width: 130px;
    /* 和logo_img控制间距 */
    margin-left: 30px;
}

/* slogan */
.slogan {
    font-family: 'Roboto', sans-serif;
    font-size: 40px;
    font-weight: bold;
    color: rgb(38, 36, 76);
    text-align: center;
    margin: 20px auto;
    letter-spacing: 0.1em;
}

/* 下面是 立即使用 按钮 */
.rightnow_button_box {
    height: 48px;
}

.button_img>img {
    /* 图片是64*64的 */
    width: 24px;
    height: 24px;
}

.rightnow_button_text {
    font-family: 'Roboto', sans-serif;
    font-size: 16px;
    color: #fff;
    text-align: center;
    margin: 0 16px;
}

.rightnow_button {
    border-radius: 32px;
    /* 设置整体的圆角半径 */
    overflow: hidden;
    /* 隐藏超出圆角范围的部分 */
}

.rightnow_button .button_img {
    width: 48px;
    height: 48px;
    border-radius: 24px;
    background-color: #fff;
    text-align: center;
    display: flex;
    align-items: center;
    justify-content: center;
}

.bottom_area {
    display: flex;
    /*使用 Flexbox 布局，将卡片水平居中，并设置卡片之间的间距*/
    justify-content: center;
    align-items: center;
    flex-wrap: wrap;
    /* 让卡片在一行排不下时换行 */
    margin-top: 60px;
    padding: 10px;
}

/* 介绍主要功能板块 */
.card {
    width: 300px;
    height: 390px;
    padding: 5px 10px;
    margin: 25px;
    border-radius: 35px;
    float: left;
}

/* 鼠标悬停加上边框 */
.card:hover {
    border: 2px solid rgb(97, 92, 237);
}

.card-image {
    margin: 10px auto;
}

/* card_title */
.card_title {
    color: #26244c;
    font-size: 24px;
    font-weight: 600;
    line-height: 34px;
    margin: 10px;
}

/*  negative文字*/
.negative_subtitle {
    font-size: 15px;
    color: #666666;
    text-decoration: underline;
    margin: 10px;
    align-items: center;
}

/* postive_subtitle */
.postive_subtitle {
    color: rgb(97, 92, 237);
    font-size: 17px;
}

/* postive_discription */
.postive_discription {
    font-size: 15px;
    margin: 5px auto;
}

#userinfo_image {
    width: 50px;
}

#image_64 {
    width: 50px;
    height: 50px;
}

/* 消极表情 */
.negative_subtitle>img,
.postive_discription>img {
    display: inline-block;
    margin-left: 14px;
    width: 25px;
}

/* 模态框的一些处理 */
.login_submit {
    padding: auto;
    margin: auto;
    align-items: center;
}

#loginSubmit {
    width: 400px;
    border-radius: 20px;
}

/* 页脚 */
.footer {
    padding: 20px 100px 40px;
    margin: 5px auto;
    border-top: 2px solid rgb(97, 92, 237);
}

.left_content {
    float: left;
}


.left_content .logo {
    margin-top: 20px;
}

.left_content p {
    margin: 10px 0 15px 0;
    font-size: 12px;
    color: #666666;
}

.links {
    float: right;
}

.links dl {
    float: left;
    margin-left: 100px;
}

.links dl dt {
    font-size: 16px;
    color: #333;
    margin-bottom: 5px;
}

.links dl dd a {
    font-size: 12px;
    color: #333;
}
</style>