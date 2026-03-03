document.addEventListener("DOMContentLoaded", function () {
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
