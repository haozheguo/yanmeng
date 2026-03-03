<template>
    <!-- <div class="max-w-9xl mx-auto grid grid-cols-5 gap-4">
        <div class="main-center col-span-5">
        </div>
    </div> -->
    <section class="section">
      <div class="select_school is-grouped">
        <div class="button-container">
          <button class="button is-rounded is-outlined"
            @click="setSchool('清华大学', 'Tsinghua University', '邱勇', 'Qiu Yong')">
            清华大学
          </button>
          <button class="button is-rounded" @click="setSchool('北京大学', 'Peking University', '林建华', 'Lin Jianhua')">
            北京大学
          </button>
          <button class="button is-rounded" @click="setSchool('复旦大学', 'Fudan University', '张维迎', 'Zhang Weiying')">
            复旦大学
          </button>
          <button class="button is-rounded"
            @click="setSchool('上海交通大学', 'Shanghai Jiao Tong University', '姚钢', 'Yao Gang')">
            上海交通大学
          </button>
          <button class="button is-rounded"
            @click="setSchool('华中科技大学', 'Huazhong University of Science and Technology', '李武', 'Li Wu')">
            华中科技大学
          </button>
          <button class="button is-rounded" @click="setSchool('浙江大学', 'Zhejiang University', '吴朝晖', 'Wu Zhaohui')">
            浙江大学
          </button>
          <button class="button is-rounded" @click="setSchool('南京大学', 'Nanjing University', '吕建', 'Lv Jian')">
            南京大学
          </button>
          <button class="button is-rounded"
            @click="setSchool('中国科学技术大学', 'University of Science and Technology of China', '康国明', 'Kang Guoming')">
            中国科学技术大学
          </button>
          <button class="button is-rounded"
            @click="setSchool('哈尔滨工业大学', 'Harbin Institute of Technology', '韩杰才', 'Han Jiecai')">
            哈尔滨工业大学
          </button>
  
        </div>
      </div>
      <div class="simulate" id="content">
        <!-- logo -->
        <div class="logo">
          <div class="logo_img">
            <img src="http://127.0.0.1:8000/media/img/logo.svg" alt="" />
          </div>
          <div class="logo_text">
            <img src="http://127.0.0.1:8000/media/img/logo_text.svg" alt="" />
          </div>
        </div>
        <div class="backgroud_image">
          <img src="http://127.0.0.1:8000/media/img/admission-letter.svg" alt="">
        </div>
        <div class="admission-letter">
          <p class="subtitle" id="paragraph0">
            <input type="text" id="nameInput" class="bulma-placeholder-mixin input" />
            <span>同学：</span>
          </p>
  
          <p class="subtitle" id="paragraph2">
            <span class="block"></span><span>祝贺你跻身</span>
            <input type="text" readonly id="universityChiName" />
            <span>的星空！日月光华中有你闪亮的</span>
            <br />
            <span>眼睛，你计划的秋天已褪去童话的色彩，一个真实的现在可以开垦一万个美</span>
            <br />
            <span>好的未来！</span>
          </p>
          <p class="subtitle" id="paragraph3">
            <span class="block"></span><span>Dear Mr/Ms.</span>
            <input type="text" id="nameEng" class="bulma-placeholder-mixin input" />
            ,<br />
            <span class="block"></span><span>Congratulations! You have been successfully
              admitted into</span>
            <br />
            <input type="text" readonly id="universityEngName" class="bulma-placeholder-mixin input" />.
          </p>
          <p class="subtitle" id="paragraph4">
            <span class="block"></span>Please be advised that you should register with this letter
            of acceptance on September 1, 2024.<br />
          </p>
          <p class="subtitle" id="paragraph5">
            <span class="block"></span>I wish you all the best for your upcoming college life!
          </p>
          <p class="subtitle" id="paragraph6"><span class="block"></span>Yours sincerely,<br /></p>
          <p class="subtitle" id="paragraph7">
            <input type="text" readonly id="presidentEng" class="bulma-placeholder-mixin input" />
            <br /><span class="block"></span>President<br />
            <input type="text" readonly id="universityEngName2" class="bulma-placeholder-mixin input" />
          </p>
          <p id="paragraph8">
            <em>本网站提供的模拟录取通知书仅供娱乐，非法使用将被视为无效，一概与本网站无关。</em>
          </p>
          <div class="ending">
            <span class="subtitle">校长：</span>
            <input type="text" readonly id="presidentChi" class="bulma-placeholder-mixin input" />
            <br />
            <br />
            <div class="endingtime">
              <input type="text" readonly id="nowTime" class="bulma-placeholder-mixin input" />
            </div>
          </div>
        </div>
      </div>
      <div class="download">
        <button class="button is-success" @click="downloadImage">
          保存图片
        </button>
      </div>
  
      <!-- 保存图片区域 -->
      <div class="card" id="card">
        <div class="card-content" id="canvasContainer">
        </div>
        <footer class="card-footer">
          <div class="content text">
            <span class="block"></span>Tip: 右键可以保存图片哦~
          </div>
          <button class="button has-text-danger" @click="closeCard">关闭</button>
        </footer>
      </div>
  
    </section>
  </template>
  
  <script>
  import html2canvas from "html2canvas";
  export default {
    data() {
      return {
        showCard: false,
      };
    },
    mounted() {
  
    },
    methods: {
      setSchool(universityChiName, universityEngName, presidentChi, presidentEng) {
        // 更新学校信息
        this.updateSchoolInfo(universityChiName, universityEngName, presidentChi, presidentEng);
      },
      downloadImage() {
        this.showCard = true;
        // 生成并显示图片
        this.generateImage();
      },
      closeCard() {
        this.showCard = false;
        // 关闭图片显示区域
        this.closeImage();
      },
      updateSchoolInfo(universityChiName, universityEngName, presidentChi, presidentEng) {
        // 更新中文学校名和英文学校名
        document.getElementById("universityChiName").value = universityChiName;
        document.getElementById("universityEngName").value = universityEngName;
        document.getElementById("universityEngName2").value = universityEngName;
        document.getElementById("presidentChi").value = presidentChi;
        document.getElementById("presidentEng").value = presidentEng;
        this.setNowTime();
      },
      setNowTime() {
        var now = new Date();
        var currentTime = `${now.getFullYear()}年${now.getMonth() + 1}月${now.getDate()}日`;
        document.getElementById("nowTime").value = currentTime;
      },
      generateImage() {
        var content = document.getElementById('content');
        var canvasContainer = document.getElementById('canvasContainer');
  
        // 移除之前的 canvas 元素（如果存在）
        var previousCanvas = canvasContainer.querySelector('canvas');
        if (previousCanvas) {
          canvasContainer.removeChild(previousCanvas);
        }
  
        // 生成新的 canvas 元素
        html2canvas(content)
          .then(canvas => {
            canvasContainer.appendChild(canvas);
            // 将 canvas 转换为图片并提供下载链接
            var link = document.createElement('a');
            link.download = 'admission_letter.png';
            link.href = canvas.toDataURL();
            link.click();
          })
          .catch(error => {
            console.error('Failed to generate image:', error);
          });
      },
      closeImage() {
        var canvasContainer = document.getElementById('canvasContainer');
        var canvas = canvasContainer.querySelector('canvas');
        if (canvas) {
          canvasContainer.removeChild(canvas);
        }
      },
    },
  };
  </script>
  
  <style scoped>
  @import url('https://cdn.jsdelivr.net/npm/bulma@1.0.0/css/bulma.min.css');
  
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
  
  /* 遮罩 */
  #overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(255, 255, 255, 0);
    /* 初始透明 */
    z-index: 9999;
    /* 设置在其他元素之上 */
    transition: opacity 0.1s ease-in-out;
    /* 添加透明度过渡效果 */
  }
  
  /* 渐变 */
  body {
    background-color: rgba(255, 255, 255, 0.8);
    /* 使用 rgba() 指定颜色和透明度，数值范围为 0 到 1 */
    margin: 0;
  }
  
  .section {
    padding-top: 15px;
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
    margin: 0;
  }
  
  /* 介绍主要功能板块 */
  .card {
    display: none;
    position: absolute;
    top: 200px;
    right: 67px;
  
    width: 467px;
    height: 660px;
    padding: 5px 10px;
    margin: 25px;
    border-radius: 35px;
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
  
  #canvasContainer {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 95%;
    padding: 10px 2px;
  }
  
  canvas {
    max-width: 90%;
    max-height: 90%;
    position: relative;
  }
  
  .card-footer {
    height: 40px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: auto;
  }
  
  .card-footer button {
    border-radius: 10px;
    font-size: 16px;
    height: 24px;
    position: relative;
    right: 30px;
  }
  
  .card-footer .content {
    font-weight: 700;
  }
  
  .simulate {
    width: 653px;
    margin: 0 auto;
    /* 居中显示 */
    padding: auto;
    position: relative;
    /* 添加相对定位，以便内部绝对定位元素相对于它定位 */
  }
  
  /* 选择院校 */
  .select_school {
    width: 1600px;
    height: 50px;
    margin: 20px 15px;
  }
  
  .admission-letter {
    width: 653px;
    /* height: 670px; */
    position: absolute;
    top: 330px;
    left: 18px;
    padding: 10px auto;
  }
  
  .subtitle {
    font-size: 18px;
    font-weight: 700;
  }
  
  .logo {
    position: absolute;
    align-items: center;
    margin: 0 10px;
    top: 13px;
    left: 202px;
    z-index: 999;
  }
  
  .logo_img {
    float: left;
    width: 95px;
  }
  
  .logo_text {
    position: absolute;
    float: left;
    width: 100px;
    margin-left: 10px;
    top: 18px;
    left: 102px;
  }
  
  
  
  input[type="text"] {
    display: inline-block;
    border: none;
    outline: none;
    background-color: transparent;
    text-align: center;
    font-size: 18px;
    font-weight: 700;
    padding: 0;
  }
  
  .block {
    display: inline-block;
    width: 40px;
  }
  
  #paragraph1 {
    margin-bottom: 10px;
  }
  
  #paragraph2 {
    margin: 10px 0;
  }
  
  #paragraph3,
  #paragraph4,
  #paragraph5 {
    margin: 16px 0;
  }
  
  #paragraph6 {
    margin: 16px 0;
  }
  
  #paragraph8 {
    margin-left: 85px;
    color: #a8a9ab;
    font-size: 14px;
  }
  
  #nameInput {
    width: 120px;
    height: 22px;
    border-bottom: 1px solid black;
  }
  
  #majorInput {
    width: 200px;
    height: 22px;
    border-bottom: 1px solid black;
  }
  
  #nameEng {
    width: 200px;
    height: 22px;
    border-bottom: 1px solid black;
  }
  
  #nav {
    border-bottom: 1px solid;
    display: inline-block;
    text-align: right;
    vertical-align: auto;
    width: 200px;
    height: 32px;
  }
  
  .navbar-dropdown {
    background-color: whitesmoke;
    justify-content: space-between;
    border-radius: 20px;
    padding: 0px 30px;
    align-items: center;
    z-index: 1000;
  }
  
  a.navbar-item:hover {
    border-bottom: 1px solid #585353;
  }
  
  .navbar-link:hover {
    color: rgb(65, 65, 206);
  }
  
  .backgroud_image {
    position: relative;
  }
  
  .download {
    position: absolute;
    top: 140px;
    right: 480px;
    /* 调整按钮距离背景图右边的距离 */
  }
  
  #downloadBtn {
    border-radius: 10px;
  }
  
  #universityChiName {
    border-bottom: 1px solid black;
  }
  
  #universityEngName {
    text-align: center;
    width: 440px;
    height: 22px;
    font-size: 18px;
    border-bottom: 1px solid black;
  }
  
  #universityEngName2 {
    text-align: left;
    width: 440px;
    height: 22px;
    font-size: 18px;
  }
  
  #majorEngName {
    display: inline-block;
    text-align: center;
    width: 248px;
    height: 22px;
    font-size: 18px;
    border-bottom: 1px solid black;
  }
  
  #presidentEng {
    text-align: center;
    width: 140px;
    height: 22px;
    font-size: 18px;
  }
  
  #presidentChi {
    text-align: left;
    width: 120px;
    height: 22px;
  }
  
  .ending {
    position: absolute;
    left: 440px;
    top: 480px;
  }
  
  #nowTime {
    text-align: left;
    width: 150px;
    height: 22px;
  }
  
  
  #prevButton,
  #nextButton {
    width: 65px;
    height: 18px;
    margin-top: 5px;
    margin-left: 5px;
  }
  
  #C909 {
    background-color: rgba(185, 21, 185, 0.5);
  }
  
  #C908 {
    background-color: rgba(255, 192, 203, 0.5);
  }
  
  /* 学校选择 */
  .select_school {
    margin: 0 auto;
  }
  
  .button-container {
    display: flex;
    padding: 5px;
    border-radius: 5px;
    overflow: hidden;
  }
  
  .button-container .button {
    flex: 1 1 auto;
    margin-right: 10px;
    background-size: 200% 100%;
    background-position: left;
    transition: background-position 0.3s ease;
    border: none;
    font-family: Arial, Helvetica, sans-serif;
    color: #6e4141;
    font-size: 16px;
    font-weight: 700;
    cursor: pointer;
    border-radius: 15px;
    overflow: hidden;
  }
  
  .button-container .button:last-child {
    margin-right: 0;
  }
  
  /* 设置每个按钮的渐变 */
  .button-container .button:nth-child(1) {
    background-image: linear-gradient(to right, #FF5733, #FFC300);
  }
  
  .button-container .button:nth-child(2) {
    background-image: linear-gradient(to right, #FFC300, #DAF7A6);
  }
  
  .button-container .button:nth-child(3) {
    background-image: linear-gradient(to right, #DAF7A6, #85FFD9);
  }
  
  .button-container .button:nth-child(4) {
    background-image: linear-gradient(to right, #85FFD9, #5C6BC0);
  }
  
  .button-container .button:nth-child(5) {
    background-image: linear-gradient(to right, #5C6BC0, #D5D8DC);
  }
  
  .button-container .button:nth-child(6) {
    background-image: linear-gradient(to right, #D5D8DC, #FF5733);
  }
  
  .button-container .button:nth-child(7) {
    background-image: linear-gradient(to right, #FF5733, #FFC300);
  }
  
  .button-container .button:nth-child(8) {
    background-image: linear-gradient(to right, #FFC300, #DAF7A6);
  }
  
  .button-container .button:nth-child(9) {
    background-image: linear-gradient(to right, #DAF7A6, #85FFD9);
  }
  
  .button-container .button:hover {
    background-position: right;
  }
  </style>