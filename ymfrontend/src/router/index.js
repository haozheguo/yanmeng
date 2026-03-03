import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import ForumView from '../views/ForumView.vue'
import LoginView from '../views/LoginView.vue'
import SignupView from '../views/SignupView.vue'
import testView from '../views/testView.vue'
import ArticleView from '@/views/ArticleView.vue'
import CreatedView from '@/views/CreatedView.vue'
import PostView from '@/views/PostView.vue'
import SearchView from '@/views/SearchView.vue'
import TrendView from '@/views/TrendView.vue'
import UserView from '@/views/UserView.vue'
import OuterView from '@/views/OuterView.vue'
import OfferView from '@/views/OfferView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/forum',
      name: 'forum',
      component: ForumView
    },
    {
      path: '/search',
      name: 'search',
      component: SearchView
    },
    {
      path: '/trend',
      name: 'trend',
      component: TrendView
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView
    },
    {
      path: '/signup',
      name: 'signup',
      component: SignupView
    },
    {
      path: '/article/:id',
      name: 'article',
      component: ArticleView
    },
    {
      path: '/post/:id',
      name: 'post',
      component: PostView
    },
    {
      path: '/user/:id',
      name: 'user',
      component: UserView
    },
    {
      path: '/test',
      name: 'test',
      component: testView
    },
    {
      path: '/create',
      name: 'create',
      component: CreatedView
    },
    {
      path: '/outer',
      name: 'outer',
      component: OuterView
    },
    {
      path: '/offer',
      name: 'offer',
      component: OfferView
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    }
  ]
})

export default router
