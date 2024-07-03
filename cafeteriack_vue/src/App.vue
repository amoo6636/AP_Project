<template>
  <div id="wrapper">
    <nav class="navbar is-dark">
      <div class="navbar-brand">
        <router-link to="/" class="navbar-item"><strong>Cafe Teriack</strong></router-link>
      </div>



      <div class="navbar-menu" id="navbar-menu">
        <div class="navbar-start">
          <div class="navbar-item">
            <form method="get" action="/search">
              <div class="field has-addons">
                <div class="control">
                  <input type="text" class="input" placeholder="What are you looking for?" name="query">
                </div>

                <div class="control">
                  <button class="button custom-search-button">
                    <span class="icon">
                      <i class="fas fa-search"></i>
                    </span>
                  </button>
                </div>
              </div>
            </form>
          </div>
        </div>

        <div class="navbar-end">
<!--          <router-link to="/hotdrinks" class="navbar-item">HOT DRINKS</router-link>-->
<!--          <router-link to="/icedrinks" class="navbar-item">ICE DRINKS</router-link>-->
<!--          <router-link to="/desserts" class="navbar-item">DESSERTS</router-link>-->
<!--          <router-link to="/cakes" class="navbar-item">CAKES</router-link>-->

          <div class="navbar-item">
            <div class="buttons">
              <template v-if="$store.state.isAuthenticated">
                <router-link to="/my-account" class="button custom-button">
                  <span class="icon"><i class="fas fa-user"></i></span>
                  <span>My Account</span>
                </router-link>
              </template>

              <template v-else>
                <router-link to="/log-in" class="button custom-button">
                  <span class="icon"><i class="fas fa-sign-in-alt"></i></span>
                  <span>Log in</span>
                </router-link>
              </template>

              <template v-if="$store.state.isAuthenticated">
                <button @click="logout()" class="button custom-logout-button">
                  <span class="icon"><i class="fas fa-sign-out-alt"></i></span>
                  <span>Log out</span>
                </button>
              </template>

              <router-link to="/cart" class="button custom-cart-button">
                <span class="icon"><i class="fas fa-shopping-cart"></i></span>
                <span>Cart ({{ cartTotalLength }})</span>
              </router-link>
            </div>
          </div>
        </div>
      </div>

      <div class="navbar-end custom-bar">
        <a class="navbar-item" @click="toggleSidebar">
          <span class="icon">
            <i class="fas fa-bars"></i>
          </span>
        </a>
      </div>
    </nav>

    <div :class="{'is-active': showSidebar}" class="sidebar">
      <router-link to="/hotdrinks" class="sidebar-item">Hot Drinks</router-link>
      <router-link to="/icedrinks" class="sidebar-item">Ice Drinks</router-link>
      <router-link to="/desserts" class="sidebar-item">Desserts</router-link>
      <router-link to="/cakes" class="sidebar-item">Cakes</router-link>
    </div>

    <div class="is-loading-bar has-text-centered" v-bind:class="{'is-loading': $store.state.isLoading }">
      <div class="lds-dual-ring"></div>
    </div>

    <section class="section">
      <router-view />
    </section>

    <footer class="footer">
      <p class="has-text-centered">Copyright (c) 2024 Made</p>
    </footer>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      showSidebar: false,
      cart: {
        items: []
      },
    }
  },
  beforeCreate() {
    this.$store.commit('initializeStore')

    const token = this.$store.state.token

    if (token) {
        axios.defaults.headers.common['Authorization'] = "Token " + token
    } else {
        axios.defaults.headers.common['Authorization'] = ""
    }
  },
  methods: {
    toggleSidebar() {
      this.showSidebar = !this.showSidebar;
    },
    navigateTo(vertical) {
      this.$router.push({ name: 'products', params: { vertical } });
      this.showSidebar = false;
    },
    logout() {
        axios.defaults.headers.common["Authorization"] = ""

        localStorage.removeItem("token")
        localStorage.removeItem("username")
        localStorage.removeItem("userid")

        this.$store.commit('removeToken')

        this.$router.push('/')
    }
  },
  mounted() {
    this.cart = this.$store.state.cart
  },
  computed: {
    cartTotalLength() {
      let totalLength = 0
      for (let i = 0; i < this.cart.items.length; i++) {
        totalLength += this.cart.items[i].quantity
      }
      console.log(totalLength)
      return totalLength
    }
  }
}
</script>


<style lang="scss">
@import '../node_modules/bulma';

.lds-dual-ring {
  display: inline-block;
  width: 80px;
  height: 80px;
}

.lds-dual-ring:after {
  content: " ";
  display: block;
  width: 64px;
  height: 64px;
  margin: 8px;
  border-radius: 50%;
  border: 6px solid #ccc;
  border-color: #ccc transparent #ccc transparent;
  animation: lds-dual-ring 1.2s linear infinite;
}
@keyframes lds-dual-ring {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}

.is-loading-bar {
  height: 0;
  overflow: hidden;

  -webkit-transition: all 0.3s;
  transition: all 0.3s;

  &.is-loading {
    height: 80px;
  }
}

.navbar-brand {
  background-color: #6F4E37;
}

.navbar-menu {
  background-color: #6F4E37;
}

.custom-search-button {
  background-color: #808000;
  border-color: #808000;
  color: white;
}

.custom-logout-button {
  background-color: #A52A2A;
  border-color: #A52A2A;

  color: white;
}

.custom-cart-button {
  background-color: #808000;
  border-color: #808000;
  color: white;
}
.custom-button {
  background-color: #CC7722;
  border-color: #CC7722;
  color: white;
}

.sidebar {
  position: absolute;
  top: 0;
  right: -250px;
  width: 165px;
  height: 35%;
  background-color: #6F4E37;
  color: white;
  overflow-x: hidden;
  transition: 0.5s;
  padding-top: 60px;
}

.sidebar.is-active {
  right: 0;
}

.sidebar-item {
  padding: 15px;
  text-decoration: none;
  font-size: 18px;
  color: white;
  display: block;
  transition: 0.3s;
}

.sidebar-item:hover {
  background-color: #808000;
}

.custom-bar {
  background-color: #6F4E37;
}
</style>
