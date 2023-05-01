import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AddUser from '../views/AddUserView.vue'
import LoginUser from '../views/LoginView.vue'
import ExplorePosts from '../views/ExplorePostsView.vue'
import UserProfileView from '../views/UserProfileView.vue'
import NewPostsView from '../views/NewPostsView.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    },
    {
      path: '/register',
      name: 'register',
      component: AddUser
    },
    {
      path: '/login',
      name: 'login',
      component: LoginUser
    },
    {
      path: '/explore',
      name: 'explore',
      component: ExplorePosts
    },
    {
      path: '/users/:id',
      name: 'UserProfile',
      component: UserProfileView
    },
    {
      path: '/posts/new',
      name: 'new_posts',
      component: NewPostsView
    },

  ]
})

// router.beforeEach((to, from, next) => {
//   const token = sessionStorage.getItem('current_user')
  
//   if (token) {
//     if (to.name == 'login' || to.name == 'register'){
//       next({ name: 'home' })
//     }else{
//       next()
//     }
//   } else {
//     if (to.name == 'login' || to.name == 'register') {
//       next()
//     }else {
//       next({ name: 'login' })
//     }
//   }
// })



export default router
