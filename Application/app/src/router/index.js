import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/incidents-old',
      name: 'incidents-old',
      component: () => import('../views/IncidentsOldView.vue')
    },
    {
      path: '/incidents-new',
      name: 'incidents-new',
      component: () => import('../views/IncidentsNewView.vue')
    }
  ]
})

export default router
