<template>
  <div class="max-w-9xl mx-auto grid grid-cols-5 gap-4">
      <div class="main-center col-span-5">
          <section class="section">
              <div class="select_school is-grouped">
                  <div class="button-container">
                      <button class="button is-rounded is-outlined" id="C901">
                          清华大学
                      </button>
                      <button class="button is-rounded" id="C902">
                          北京大学
                      </button>
                      <button class="button is-rounded" id="C903">
                          复旦大学
                      </button>
                      <button class="button is-rounded" id="C904">
                          上海交通大学
                      </button>
                      <button class="button is-rounded" id="C905">
                          华中科技大学
                      </button>
                      <button class="button is-rounded" id="C906">
                          浙江大学
                      </button>
                      <button class="button is-rounded" id="C907">
                          南京大学
                      </button>
                      <button class="button is-rounded" id="C908">
                          中国科学技术大学
                      </button>
                      <button class="button is-rounded" id="C909">
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
                      <p class="subtitle" id="paragraph1">
                          <span class="block"></span><span>你被我校</span>
                      </p>
                      <p class="subtitle" id="paragraph2">
                          <span>通知入学报到。</span><br />
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
                          <input type="text" readonly id="universityEngName" class="bulma-placeholder-mixin input" />
                          as
                          a<br />
                          <input type="text" readonly id="majorEngName" class="bulma-placeholder-mixin input" />
                          <span> major</span>.
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
                  <button id="downloadBtn" class="button is-success">
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
                      <button class="button has-text-danger" id="closeBtn">关闭</button>
                  </footer>
              </div>

          </section>
      </div>
  </div>

</template>

<script>
import html2canvas from "html2canvas";
export default {
  mounted() {
      document.addEventListener("DOMContentLoaded", function () {
          // 在这个块内放置提供的JavaScript代码
          // 获取下拉菜单,创建下拉菜单选项，然后把选项归到下拉菜单
          var paragraph1 = document.getElementById("paragraph1");
          var dropdown = document.createElement("div");
          dropdown.id = "nav";
          dropdown.classList.add("navbar-item", "has-dropdown", "is-active");
          var dropdownLink = document.createElement("a");
          dropdownLink.classList.add("navbar-link");
          dropdownLink.textContent = "专业选择";
          var dropdownList = document.createElement("div");
          dropdownList.classList.add("navbar-dropdown", "is-hidden");

          // 控制下拉菜单的显示和隐藏
          dropdownLink.addEventListener("click", function () {
              dropdownList.classList.toggle("is-hidden");
          });

          // 专业及其英文名的映射关系
          var majorTranslations = {
              "计算机科学": "Computer Science",
              "软件工程": "Software Engineering",
              "网络工程": "Network Engineering",
              "信息安全": "Information Security",
              "人工智能": "Artificial Intelligence",
              "数据科学": "Data Science",
              "数学": "Mathematics",
              "统计学": "Statistics",
              "物理学": "Physics",
              "化学": "Chemistry",
              "生物学": "Biology",
              "地球科学": "Earth Sciences",
              "环境科学": "Environmental Science",
              "工程学": "Engineering",
              "电气工程": "Electrical Engineering",
              "机械工程": "Mechanical Engineering",
              "土木工程": "Civil Engineering",
              "化工与制药工程": "Chemical and Pharmaceutical Engineering",
              "材料科学与工程": "Materials Science and Engineering",
              "航空航天工程": "Aerospace Engineering",
              "汽车工程": "Automotive Engineering",
              "医学": "Medicine",
              "临床医学": "Clinical Medicine",
              "药学": "Pharmacy",
              "护理学": "Nursing",
              "法律": "Law",
              "金融学": "Finance",
              "会计学": "Accounting",
              "经济学": "Economics",
              "市场营销": "Marketing",
              "管理学": "Management",
              "人力资源管理": "Human Resource Management",
              "物流管理": "Logistics Management",
              "国际贸易": "International Trade",
              "心理学": "Psychology",
              "社会学": "Sociology",
              "国际关系": "International Relations",
              "政治学": "Political Science",
              "历史学": "History",
              "哲学": "Philosophy",
              "文学": "Literature",
              "音乐学": "Music",
              "戏剧与影视学": "Drama and Film Studies",
              "舞蹈学": "Dance",
              "视觉艺术": "Visual Arts",
              "设计学": "Design",
              "建筑学": "Architecture",
              "城市规划": "Urban Planning",
              "景观设计": "Landscape Design",
              "教育学": "Education",
              "教育技术学": "Educational Technology",
              "体育学": "Sports Science",
              "体育训练": "Sports Training",
              "运动康复": "Sports Rehabilitation",
              "社会工作": "Social Work",
              "公共管理": "Public Administration",
              "社区发展": "Community Development",
              "旅游管理": "Tourism Management",
              "体育管理": "Sports Management",
              "航空服务": "Aviation Services",
              "电子商务": "E-commerce",
              "新闻传播学": "Journalism and Communication",
              "广告学": "Advertising",
              "公共关系": "Public Relations",
              "传媒管理": "Media Management"
          };

          // 每页显示的专业数量
          var itemsPerPage = 8;
          // 当前页数
          var currentPage = 1;
          // 总页数
          var totalPages = Math.ceil(Object.keys(majorTranslations).length / itemsPerPage);
          // 更新下拉菜单的选项列表
          function updateDropdownList() {
              // 清空当前的选项列表
              dropdownList.innerHTML = "";
              // 计算当前页的起始索引和结束索引
              var startIndex = (currentPage - 1) * itemsPerPage;
              var endIndex = Math.min(startIndex + itemsPerPage, Object.keys(majorTranslations).length);
              // 遍历当前页的专业，添加到选项列表中
              Object.keys(majorTranslations).slice(startIndex, endIndex).forEach(function (major) {
                  var option = createOptionElement(major);
                  dropdownList.appendChild(option);
              });

              // 添加上一页按钮
              var prevButton = document.createElement("button");
              prevButton.classList.add("button", "is-success");
              prevButton.id = "prevButton";
              prevButton.textContent = "上一页";
              prevButton.addEventListener("click", function () {
                  updateCurrentPage(currentPage - 1);
              });
              dropdownList.appendChild(prevButton);

              // 添加下一页按钮
              var nextButton = document.createElement("button");
              nextButton.classList.add("button", "is-success");
              nextButton.id = "nextButton";
              nextButton.textContent = "下一页";
              nextButton.addEventListener("click", function () {
                  updateCurrentPage(currentPage + 1);
              });
              dropdownList.appendChild(nextButton);
          }

          // 创建选项元素
          function createOptionElement(major) {
              var option = document.createElement("a");
              option.classList.add("navbar-item");
              option.textContent = major; // 使用中文专业名称作为选项的文本内容
              // 为每个选项添加点击事件
              option.addEventListener("click", function () {
                  dropdownLink.textContent = major; // 更新下拉菜单显示的文本
                  var englishName = majorTranslations[major]; // 获取对应的英文专业名称
                  document.getElementById("majorEngName").value = englishName; // 更新英文专业名称输入框的内容
                  dropdownList.classList.toggle("is-hidden");
              });
              return option;
          }
          // 更新当前页数
          function updateCurrentPage(page) {
              currentPage = Math.max(1, Math.min(page, totalPages));
              updateDropdownList();
          }
          updateDropdownList();
          // 将链接和选项列表添加到下拉菜单中
          dropdown.appendChild(dropdownLink);
          dropdown.appendChild(dropdownList);
          paragraph1.appendChild(dropdown);
          // 专业后面的话
          var majorSpan = document.createElement("span");
          majorSpan.classList.add("subtitle");
          majorSpan.textContent = "专业录取，请于2024年9月1日凭本";
          paragraph1.appendChild(majorSpan);

          // 更新时间
          var setNowTime = function () {
              var now = new Date();
              var currentTime = `${now.getFullYear()}年${now.getMonth() + 1}月${now.getDate()}日`;
              document.getElementById("nowTime").value = currentTime;
          }

          // 按键绑定
          var setSchool = function (universityChiName, universityEngName, presidentChi, presidentEng) {
              // 更新中文学校名和英文学校名
              document.getElementById("universityChiName").value = universityChiName;
              document.getElementById("universityEngName").value = universityEngName;
              document.getElementById("universityEngName2").value = universityEngName;
              document.getElementById("presidentChi").value = presidentChi;
              document.getElementById("presidentEng").value = presidentEng;
              setNowTime();
          }
          // 为按键绑定
          {
              var TsinghuaBtn = document.getElementById("C901");
              TsinghuaBtn.addEventListener("click", function () {
                  setSchool("清华大学", "Tsinghua University", "邱勇", "Qiu Yong");
              });
              var PekingBtn = document.getElementById("C902");
              PekingBtn.addEventListener("click", function () {
                  setSchool("北京大学", "Peking University", "林建华", "Lin Jianhua");
              });
              var FudanBtn = document.getElementById("C903");
              FudanBtn.addEventListener("click", function () {
                  setSchool("复旦大学", "Fudan University", "张维迎", "Zhang Weiying");
              });
              var SJTUBtn = document.getElementById("C904");
              SJTUBtn.addEventListener("click", function () {
                  setSchool("上海交通大学", "Shanghai Jiao Tong University", "姚钢", "Yao Gang");
              });
              var HUSTBtn = document.getElementById("C905");
              HUSTBtn.addEventListener("click", function () {
                  setSchool("华中科技大学", "Huazhong University of Science and Technology", "李武", "Li Wu");
              });
              var ZJUBtn = document.getElementById("C906");
              ZJUBtn.addEventListener("click", function () {
                  setSchool("浙江大学", "Zhejiang University", "吴朝晖", "Wu Zhaohui");
              });
              var NJUBtn = document.getElementById("C907");
              NJUBtn.addEventListener("click", function () {
                  setSchool("南京大学", "Nanjing University", "吕建", "Lv Jian");
              });
              var USTCBtn = document.getElementById("C908");
              USTCBtn.addEventListener("click", function () {
                  setSchool("中国科学技术大学", "University of Science and Technology of China", "康国明", "Kang Guoming");
              });
              var HITBtn = document.getElementById("C909");
              HITBtn.addEventListener("click", function () {
                  setSchool("哈尔滨工业大学", "Harbin Institute of Technology", "韩杰才", "Han Jiecai");
              });
          }

          document.getElementById('downloadBtn').addEventListener('click', function () {
              var card = document.getElementById('card');
              card.style.display = "block";
              var content = document.getElementById('content');
              var canvasContainer = document.getElementById('canvasContainer');

              // 移除之前的 canvas 元素（如果存在）
              var previousCanvas = canvasContainer.querySelector('canvas');
              if (previousCanvas) {
                  canvasContainer.removeChild(previousCanvas);
              }

              // 生成新的 canvas 元素
              html2canvas(content, {
                  onrendered: function (canvas) {
                      console.log(canvas); // 打印生成的 canvas 元素
                      canvasContainer.appendChild(canvas);
                  }
              });
          });

          document.getElementById('closeBtn').addEventListener('click', function () {
              var card = document.getElementById('card');
              card.style.display = "none";

              var canvasContainer = document.getElementById('canvasContainer');
              var canvas = canvasContainer.querySelector('canvas');
              if (canvas) {
                  canvasContainer.removeChild(canvas);
              }
          });
      });
  }
}
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

#nameEng {
  width: 100px;
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