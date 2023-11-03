import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      redirect: '/home',
    },
    {
      path: '/home',
      name: 'home',
      component: () => import('../components/anime/comparator.component.vue')
    },
    {
      path: '/picker',
      name: 'picker',
      component: () => import('../components/anime/picker.component.vue')
    }
  ]
})

export default router
