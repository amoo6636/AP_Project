import { createStore } from 'vuex'

export default createStore({
  state: {
    cart: {
      items: [],
    },
    isAuthenticated: false,
    token: '',
    isLoading: false,
    storage_sugar: '',
    storage_coffee: '',
    storage_flour: '',
    storage_chocolate: ''
  },
  getters: {
  },
  mutations: {
    initializeStore(state) {
      if (localStorage.getItem('cart')) {
        state.cart = JSON.parse(localStorage.getItem('cart'))
      } else {
        localStorage.setItem('cart', JSON.stringify(state.cart))
      }

      if (localStorage.getItem('token')) {
          state.token = localStorage.getItem('token')
          state.isAuthenticated = true
      } else {
          state.token = ''
          state.isAuthenticated = false
      } 
    },
    addToCart(state, item) {
      const exists = state.cart.items.filter(i => i.product.id === item.product.id)
      if (exists.length) {
        exists[0].quantity = parseInt(exists[0].quantity) + parseInt(item.quantity)
      } else {
        state.cart.items.push(item)
      }
      state.storage_sugar -= parseInt(item.quantity)*parseInt(item.sugar)
      state.storage_coffee -= parseInt(item.quantity)*parseInt(item.coffee)
      state.storage_flour -= parseInt(item.quantity)*parseInt(item.flour)
      state.storage_chocolate -= parseInt(item.quantity)*parseInt(item.chocolate)

      localStorage.setItem('cart', JSON.stringify(state.cart))
    },
    storageHandeler(state,item){
      if (state.storage_sugar - parseInt(item.quantity)*parseInt(item.sugar) <0 
      || state.storage_coffee - parseInt(item.quantity)*parseInt(item.coffee) <0
      || state.storage_flour - parseInt(item.quantity)*parseInt(item.flour) <0
      || state.storage_chocolate - parseInt(item.quantity)*parseInt(item.chocolate) <0) {
        return false
      } else { 
        return true
      }
    },
    setIsLoading(state, status) {
      state.isLoading = status
    },
    setToken(state, token) {
        state.token = token
        state.isAuthenticated = true
    },  
    removeToken(state) {
        state.token = ''
        state.isAuthenticated = false
    },
    clearCart(state) {
      state.cart = { items: [] }

      localStorage.setItem('cart', JSON.stringify(state.cart))
    },
  },
  actions: {
  },
  modules: {
  }
})
