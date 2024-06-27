import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

import Product from '../views/Product.vue'
import SignUp from '../views/SignUp.vue'
import Cart from '../views/CartView.vue'
import Vertical from '../views/Vertical.vue'
import LogIn from '../views/LogIn.vue'
import Search from '../views/Search.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/search',
    name: 'Search',
    component: Search
  },
  {
    path: '/sign-up',
    name: 'SignUp',
    component: SignUp
  },
  {
    path: '/log-in',
    name: 'LogIn',
    component: LogIn
  },

  {
    path: '/cart',
    name: 'Cart',
    component: Cart
  },
  {
    path: '/:vertical_slug/:product_slug',
    name: 'Product',
    component: Product
  },
  {
    path: '/:vertical_slug',
    name: 'Vertical',
    component: Vertical
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router





