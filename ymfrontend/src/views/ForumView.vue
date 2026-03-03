<template>
  <div class="max-w-7xl mx-auto grid grid-cols-5 gap-4">
    <div class="mt-4 main-left col-span-1">
      <div class="p-1 bg-white border border-gray-200 text-center rounded-xl flex flex-col space-y-2">
        <div @click="getPostList()"
          class="flex items-center space-x-2 text-gray-500 hover:text-blue-700 p-4 rounded-xl hover:bg-gray-100">
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
            stroke="currentColor" class="w-6 h-6 mr-2">
            <path stroke-linecap="round" stroke-linejoin="round"
              d="M2.25 12l8.954-8.955c.44-.439 1.152-.439 1.591 0L21.75 12M4.5 9.75v10.125c0 .621.504 1.125 1.125 1.125H9.75v-4.875c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125V21h4.125c.621 0 1.125-.504 1.125-1.125V9.75M8.25 21h8.25" />
          </svg>最新综合
        </div>
        <div @click="getPostList('经验分享')"
          class="flex items-center space-x-2 text-gray-500 hover:text-blue-700 p-4 rounded-xl hover:bg-gray-100">
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
            stroke="currentColor" class="w-6 h-6 mr-2">
            <path stroke-linecap="round" stroke-linejoin="round"
              d="M2.25 12l8.954-8.955c.44-.439 1.152-.439 1.591 0L21.75 12M4.5 9.75v10.125c0 .621.504 1.125 1.125 1.125H9.75v-4.875c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125V21h4.125c.621 0 1.125-.504 1.125-1.125V9.75M8.25 21h8.25" />
          </svg>经验分享
        </div>
        <div @click="getPostList('疑难求解')"
          class="flex items-center space-x-2 text-gray-500 hover:text-blue-700 p-4 rounded-xl hover:bg-gray-100">
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
            stroke="currentColor" class="w-6 h-6 mr-2">
            <path stroke-linecap="round" stroke-linejoin="round"
              d="M2.25 12l8.954-8.955c.44-.439 1.152-.439 1.591 0L21.75 12M4.5 9.75v10.125c0 .621.504 1.125 1.125 1.125H9.75v-4.875c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125V21h4.125c.621 0 1.125-.504 1.125-1.125V9.75M8.25 21h8.25" />
          </svg>疑难求解
        </div>
        <div @click="getPostList('学习交流')"
          class="flex items-center space-x-2 text-gray-500 hover:text-blue-700 p-4 rounded-xl hover:bg-gray-100">
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
            stroke="currentColor" class="w-6 h-6 mr-2">
            <path stroke-linecap="round" stroke-linejoin="round"
              d="M2.25 12l8.954-8.955c.44-.439 1.152-.439 1.591 0L21.75 12M4.5 9.75v10.125c0 .621.504 1.125 1.125 1.125H9.75v-4.875c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125V21h4.125c.621 0 1.125-.504 1.125-1.125V9.75M8.25 21h8.25" />
          </svg>学习交流
        </div>
        <div @click="getPostList('复试讨论')"
          class="flex items-center space-x-2 text-gray-500 hover:text-blue-700 p-4 rounded-xl hover:bg-gray-100">
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
            stroke="currentColor" class="w-6 h-6 mr-2">
            <path stroke-linecap="round" stroke-linejoin="round"
              d="M2.25 12l8.954-8.955c.44-.439 1.152-.439 1.591 0L21.75 12M4.5 9.75v10.125c0 .621.504 1.125 1.125 1.125H9.75v-4.875c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125V21h4.125c.621 0 1.125-.504 1.125-1.125V9.75M8.25 21h8.25" />
          </svg>复试讨论
        </div>
        <div @click="getPostList('放松一刻')"
          class="flex items-center space-x-2 text-gray-500 hover:text-blue-700 p-4 rounded-xl hover:bg-gray-100">
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
            stroke="currentColor" class="w-6 h-6 mr-2">
            <path stroke-linecap="round" stroke-linejoin="round"
              d="M2.25 12l8.954-8.955c.44-.439 1.152-.439 1.591 0L21.75 12M4.5 9.75v10.125c0 .621.504 1.125 1.125 1.125H9.75v-4.875c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125V21h4.125c.621 0 1.125-.504 1.125-1.125V9.75M8.25 21h8.25" />
          </svg>放松一刻
        </div>
      </div>
    </div>

    <div class="mt-4 main-center col-span-3 space-y-4">
      <div>
        <div class="p-6 bg-white border border-gray-200 rounded-xl">
          <div>
            <div class="border-l-4 border-blue-500 pl-2">
              <label class="text-xl font-bold">内容</label>
            </div>
            <br>
            <textarea v-model="postForm.content" placeholder="请输入内容"
              class="w-full h-30 py-4 px-6 border border-gray-300 rounded-lg"></textarea>
          </div>
          <div>
            <div class="border-l-4 mt-4 border-blue-500 pl-2">
              <label class="text-xl font-bold">类别</label>
            </div>
            <br>
            <div class="flex">
              <!-- 用 v-for 循环生成单选框 -->
              <label v-for="category in categories" :key="category" class="mr-3">
                <div class="bg-blue-100 border border-blue-500 rounded-lg px-3 py-2 cursor-pointer text-sm
                             hover:bg-blue-200">
                  <input type="radio" v-model="postForm.category" :value="category" name="category" class="">
                  {{ category }}
                </div>
              </label>
            </div>
          </div>
          <div v-if="postForm.img" class="relative w-1/3 h-auto">
    <img :src="postForm.img" alt="Uploaded image" class="">
    <button @click="cancelUpload" class="absolute top-0 right-0">X</button>
</div>
          <div class="flex justify-start">
            <input type="file" @change="uploadPostImg" style="display: none" ref="uploader">
            <button @click="$refs.uploader.click()"
              class="mt-6 py-4 px-8 bg-green-500 text-white rounded-lg block">
              上传图片
            </button>
          <div>
            <button @click="submitPost"
              class="mt-6 ml-8 py-4 px-8 bg-blue-500 text-white rounded-lg block">发布帖子</button>
          </div>
          </div>
          
        </div>
      </div>

      <div v-if="posts.length === 0" class="p-4  bg-white border border-gray-200 rounded-xl flex flex-col items-center">
        <p class="text-gray-500 text-xl mt-8">亲爱的研梦er，这里空空如也~</p>
        <img src="http://127.0.0.1:8000/media/svg/empty.svg" class="w-1/2 mt-4">
      </div>

      <div v-for="(post, index) in posts" :key="index" @click="goToPostDetail(post.id, post.ViewNum)"
        class="p-4 bg-white border border-gray-200 rounded-xl hover:bg-blue-100">
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
        <div class="flex justify-around items-center mt-2">
          <button @click="logOut" class="mt-4 px-8 py-2 bg-gray-500 text-white rounded-3xl">退出登录</button>
        </div>
      </div>

      <div v-else class="p-4 bg-white border border-gray-200 text-center rounded-xl">

        <div class="flex items-center space-x-1">
          <div class="border-2 border-blue-500 h-6 mx-2"></div>
          <h2 class="text-xl font-bold">登录享受更多权益</h2>
        </div>
        <RouterLink to="/login">
          <div class="flex justify-around items-center mt-4">
            <button class="px-8 py-2 bg-blue-500 text-white rounded-3xl">登录</button>
          </div>
        </RouterLink>

        <RouterLink to="/signup">
          <div class="flex justify-around items-center mt-4">
            <button class="px-8 py-2 bg-gray-500 text-white rounded-3xl">注册</button>
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
      posts: [],
      categories: ['经验分享', '疑难求解', '学习交流', '复试讨论', '放松一刻'], // 单选框的选项
      postForm: {
        content: '',
        category: '',
        img: ''
      }
    }
  },
  created() {
    this.getPostList();
    this.checkLoginStatus();

  },
  methods: {
    // 格式化时间
    formatDate(date) {
      return new Date(date).toLocaleString();
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
    },

    // 上传图片
    async uploadPostImg(event) {
      const file = event.target.files[0]
      if (!file) return

      try {
        const formData = new FormData()
        formData.append('file', file)
        formData.append('folder', 'post')
        const response = await axios.post('/api_user/upload/', formData, {
          headers: { 'Content-Type': 'multipart/form-data' }
        })
        this.postForm.img = response.data.url
        console.log(this.postForm.img)
      } catch (err) {
        console.error(err)
      }
    },

    // 取消图片上传
    cancelUpload() {
      this.postForm.img = ''
    },

    // 用户发帖
    submitPost() {
      if (!this.isLoggedIn) {
        ElMessage.error('请先登录!');
        return;
      }
      if (!this.postForm.content || !this.postForm.category) {
        ElMessage.error('请填写完整信息!');
        return;
      }
      const postData = {
        content: this.postForm.content,
        category: this.postForm.category,
        author: this.userInfo.id,
      }
      if (this.postForm.img) {
        postData.img = this.postForm.img;
      }
      axios.post('/api_forum/post/', postData)
        .then(response => {
          // Handle successful response
          // console.log("Article uploaded successfully:", response.data);
          ElMessage.success('恭喜你,发帖成功!');
          this.postForm = {
            content: '',
            category: '',
            img: ''
          }
          this.getPostList();
        })
        .catch(error => {
          // Handle error response
          console.error("Error uploading article:", error);
          // Display error message to the user
          ElMessage.error('发帖失败，请稍后重试!');
        });
    },

    // 获取分类帖子
    getPostList(category) {
      // 发送GET请求
      axios.get('/api_forum/getPostlist/', {
        params: {
          category: category
        }
      })
        .then(response => {
          // 更新文章列表数据
          this.posts = response.data;
          // console.log(this.posts);
        })
        .catch(error => {
          // 处理错误
          console.error('Error:', error);
        });
    },

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
