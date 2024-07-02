<template>
  <div class="home">
    <section class="hero is-small is-dark mb-6">
        <div class="hero-body has-text-centered">
            <p class="title mb-5">
                Welcome to Cafe Teriack
            </p>
            <p class="subtitle">
                Coffee is our love language
            </p>
        </div>
    </section>
    <carousel :slides="slides" :interval="3000" controls indicators></carousel>


    <div class="columns is-multiline">
      <div class="column is-12">
          <h2 class="is-size-2 has-text-centered">Latest products</h2>
      </div>

      <div
        class="column is-3"
          v-for="product in latestProducts"
          v-bind:key="product.id"
        >
            <div class="box">
            <figure class="image mb-4">
                <img :src="product.get_thumbnail">
            </figure>

            <h3 class="is-size-4">{{ product.name }}</h3>
            <p class="is-size-6 has-text-grey">${{ product.price }}</p>

            <router-link v-bind:to="product.get_absolute_url" class="button is-dark mt-4">View Details</router-link>
            </div>
        </div>

    </div>
  </div>
</template>

<script>
import axios from 'axios'
import Carousel from "../components/carousel/Carousel.vue";


export default {
  name: 'Home',
  data() {
    return {
      latestProducts: [],
      slides: [
        "https://wallpapercave.com/wp/wp9277620.jpg",
        "https://wallpapercave.com/wp/wp9277504.jpg",
        "https://wallpapercave.com/wp/wp4430573.jpg",
        "https://wallpapercave.com/wp/wp9278380.jpg",
        "https://wallpapercave.com/wp/wp9278197.jpg",
        ]
      }
  },
  components: {
       Carousel
       },
  mounted() {
    this.getLatestProducts()

    document.title = 'Home | Cafe Teriack'
  },
  methods: {
    async getLatestProducts() {
      this.$store.commit('setIsLoading', true)
      await axios
        .get('/api/v1/latest-products/')
        .then(response => {
          this.latestProducts = response.data
        })
        .catch(error => {
          console.log(error)
        })

      this.$store.commit('setIsLoading', false)
    }
  }
}
</script>

<style scoped>
.image {
    margin-top: -1.25rem;
    margin-left: -1.25rem;
    margin-right: -1.25rem;
  }
  .box {
    margin-top: 20px;
  }
  .title{
    font-size: 50px;
    color: #6F4E37;
  }
  .subtitle{
    font-size: 25px;
    color: #EADDCA;
    font-style: italic;
  }
  .hero.is-dark {
    background-color: #C4A484;
  }
  .home .is-12 {
    color: #6F4E37;
  }

</style>