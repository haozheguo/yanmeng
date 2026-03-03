<template>
  <div class="mt-20 max-w-7xl mx-auto grid grid-cols-4 gap-4">
    <div class="main-left col-span-2">
      <div class="p-12 bg-white border border-gray-200 rounded-lg">
        <div class="border-l-4 border-blue-500 pl-2">
          <h1 class="mb-6 text-2xl font-bold">欢迎来到研梦信息平台</h1>
        </div>
        <hr class="mb-4">
        <p class="mb-6 text-gray-500">
          研梦相伴，快乐上岸！
        </p>
        <img class="mx-auto h-64" src="http://127.0.0.1:8000/media/loginsvg.svg"
          alt="Image description">

        <p class="mt-4 font-bold">
          还没有账号吗? <RouterLink to="/signup"><span class="underline text-blue-500">点击这里</span></RouterLink> 去注册！
        </p>
      </div>
    </div>

    <div class="main-center col-span-2 space-y-4">
      <div class="p-12 bg-white border border-gray-200 rounded-lg">

        <h2 class="text-2xl text-center font-bold mb-8">登录享受更多权益</h2>

        <form class="space-y-6" v-on:submit.prevent="login">
          <div>
            <div class="border-l-4 border-blue-500 pl-2">
              <label class="mb-6 text-xl font-bold">手机号</label>
            </div>
            <br>
            <input type="text" placeholder="请输入你的手机号" v-model="form.phone"
              class="w-full mt-2 py-4 px-6 border border-gray-300 rounded-lg">
          </div>

          <div>
            <div class="border-l-4 border-blue-500 pl-2">
              <label class="mb-6 text-xl font-bold">密码</label>
            </div>
            <br>
            <input type="password" placeholder="请输入你的密码" v-model="form.password"
              class="w-full mt-2 py-4 px-6 border border-gray-300 rounded-lg">
          </div>

          <div>
            <button class="mt-10 py-4 px-8 bg-blue-500 text-white rounded-lg mx-auto block">登录</button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<!-- <script>
import { useUserStore } from '@/stores/userStore';
import axios from 'axios';
import { ElMessage } from 'element-plus';
import { useRouter } from 'vue-router';

export default {
  setup() {
    const userStore = useUserStore();
    const router = useRouter();

    const form = {
      phone: '',
      password: ''
    };

    const login = async () => {
      try {
        const response = await axios.post('api_user/login/', form);
        const user = response.data;
        console.log(user);
        userStore.setUser(user);
        ElMessage({
          message: '登录成功，开始研梦之旅吧！',
          type: 'success',
        });
        router.push('/');
      } catch (error) {
        console.error(error);
        ElMessage.error('登录失败，请检查手机号和密码是否正确！');
      }
    };

    return {
      form,
      login,
    };
  },
};
</script> -->


<script>
import axios from 'axios';
import { ElMessage } from 'element-plus';

export default {
  data() {
    return {
      form: {
        phone: '',
        password: ''
      }
    };
  },
  methods: {
    async login() {
      try {
        const response = await axios.post('api_user/login/', this.form);
        const user = response.data;
        console.log(user)
        localStorage.setItem('user', JSON.stringify(user));
        ElMessage.success({
          message: '登录成功，开始研梦之旅吧！',
          duration: 2000
        })
        this.$router.push('/')
      } catch (error) {
        console.error(error);
        ElMessage.error('登录失败，请检查手机号和密码是否正确！')
      }
    }
  }
};
</script>
