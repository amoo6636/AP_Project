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
          <h2 class="is-size-2 has-text-centered">Popular Products</h2>
      </div>

      <div
            class="column is-3"
            v-for="product in popularProducts"
            v-bind:key="product.id"
        >
        <div class="box product-box">
            <figure class="image mb-4">
                <img :src="product.get_thumbnail" alt="Product Image">
            </figure>

            <h3 class="is-size-4">{{ product.name }}</h3>
            <p class="is-size-6 has-text-grey">${{ product.price }}</p>

            <router-link v-bind:to="product.get_absolute_url" class="button is-primary mt-4">View Details</router-link>
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
      popularProducts: [],
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
    this.getPopularProducts()

    document.title = 'Home | Cafe Teriack'
  },
  methods: {
    async getPopularProducts() {
      this.$store.commit('setIsLoading', true)
      await axios
        .get('/api/v1/popular-products/')
        .then(response => {
          this.popularProducts = response.data
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

.title {
  font-size: 4rem;
  color: #CC7722;
  margin-bottom: 0.5rem;
  font-weight: bold;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3); /* Text shadow for emphasis */
}

.subtitle {
  font-size: 1.5rem;
  color: #EADDCA;
  font-style: italic;
}

.hero.is-dark {
  background-color: #C4A484;
  background-image: linear-gradient(rgb(111, 78, 55, 0.2), rgba(196, 164, 132, 0.95)), url(@/assets/images/hero-background.jpg);
  background-size: cover;
  background-position: center;
  position: marker;
}

.hero-foot {
  position: absolute;
  bottom: 0;
  left: 50%;
  transform: translateX(-50%);
  width: 100%;
  text-align: center;
}

.hero-coffee {
  max-width: 300px;
  width: 100%;
  height: auto;
  display: inline-block;
  margin-bottom: -30px; /* Adjust to position coffee image */
}

.has-text-primary {
  color: #CC7722;
}
.product-box {
  transition: transform 0.3s, box-shadow 0.3s;
  text-align: center;
}
.product-box:hover {
  transform: translateY(-10px);
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}
.image {
  display: flex;
  justify-content: center;
  align-items: center;
  overflow: hidden;
  border-radius: 10px;
}
.image img {
  max-width: 100%;
  max-height: 200px;
  transition: transform 0.3s;
}
.image img:hover {
  transform: scale(1.05);
}
.is-primary {
  background-color: #808000 !important;
  border-color: #808000 !important;
  color: #fff !important;
}
.is-primary:hover {
  background-color: #808000 !important;
  border-color: #808000 !important;
}
h3 {
  margin-top: 10px;
  font-weight: bold;
}
p {
  margin-top: 5px;
  margin-bottom: 15px;
}
.mt-4 {
  margin-top: 1rem !important;
}
</style>