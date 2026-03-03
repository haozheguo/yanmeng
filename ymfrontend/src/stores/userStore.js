import { defineStore } from 'pinia';

export const useUserStore = defineStore({
  id: 'user',
  state: () => ({
    name: '',
    phone:null,
    ymvalue: 0,
    is_vip: false,
  }),
  actions: {
    setUser(user) {
      this.name = user.name;
      this.phone = user.phone;
      this.ymvalue = user.ymvalue;
      this.is_vip = user.is_vip;
      console.log('user:', user);
    },
  },
});