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
                <img class="mx-auto " src="http://127.0.0.1:8000/media/loginsvg.svg"
                    alt="Image description">

                <p class="mt-7 font-bold">
                    已经有账号了? <RouterLink to="/login"><span class="underline text-blue-500">点击这里</span></RouterLink> 去登录！
                </p>
            </div>
        </div>

        <div class="main-center col-span-2 space-y-4">
            <div class="p-12 bg-white border border-gray-200 rounded-lg">

                <h2 class="text-2xl text-center font-bold mb-2">注册开启研梦之旅</h2>

                <form class="space-y-6" @submit.prevent="register">
                    <div>
                        <div class="border-l-4 border-blue-500 mb-3 pl-2">
                            <label class=" text-xl font-bold">用户名</label>
                        </div>

                        <input type="text" placeholder="请输入你的用户名" v-model="form.name"
                            class="w-full mt-2 py-3 px-6 border border-gray-300 rounded-lg">
                    </div>

                    <div>
                        <div class="border-l-4 border-blue-500 mb-3 pl-2">
                            <label class=" text-xl font-bold">手机号</label>
                        </div>

                        <input type="text" placeholder="请输入你的手机号" v-model="form.phone"
                            class="w-full mt-2 py-3 px-6 border border-gray-300 rounded-lg">
                    </div>

                    <div>
                        <div class="border-l-4 border-blue-500 mb-3 pl-2">
                            <label class=" text-xl font-bold">密码</label>
                        </div>

                        <input type="password" placeholder="请输入你的密码" v-model="form.password"
                            class="w-full mt-2 py-3 px-6 border border-gray-300 rounded-lg">
                    </div>

                    <div>
                        <div class="border-l-4 border-blue-500 mb-3 pl-2">
                            <label class=" text-xl font-bold">确认密码</label>
                        </div>

                        <input type="password" placeholder="请再次输入你的密码" v-model="form.password1"
                            class="w-full mt-2 py-3 px-6 border border-gray-300 rounded-lg">
                    </div>

                    <div>
                        <button class="mt-6 py-3 px-8 bg-blue-500 text-white rounded-lg mx-auto block">登录</button>
                    </div>
                </form>
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
            form: {
                name: '',
                phone: '',
                password: '',
                password1: '',
            }
        }
    },
    methods: {
        async register() {
            if (this.form.password !== this.form.password1) {
                ElMessage.warning('两次输入的密码不一致！');
                return;
            }
            if (this.form.name === '' || this.form.phone === '' || this.form.password === '') {
                ElMessage.warning('请填写完整信息！');
                return;
            }
            try {
                const { password1, ...postData } = this.form; // Exclude password1 from the data to be posted
                const response = await axios.post('api_user/users/', postData);
                console.log(response.data);
                ElMessage.success('注册成功，请前往登录！');
                this.$router.push('/login');
            } catch (error) {
                console.error(error);
            }
        }
    }
}
</script>