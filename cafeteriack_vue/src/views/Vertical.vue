<template>
    <div class="page-vertical">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h2 class="is-size-2 has-text-centered title">{{ vertical.name }}</h2>
            </div>

            <div
                class="column is-3"
                v-for="product in vertical.products"
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
import { toast } from 'bulma-toast'

export default {
  name: 'Vertical',
  data() {
    return {
      vertical: {
        products: []
      }
    }
  },
  mounted() {
    this.getVertical()
  },
  watch: {
    $route(to, from) {
      if (to.name === 'Vertical') {
        this.getVertical()
      }
    }
  },
  methods: {
    async getVertical() {
      const verticalSlug = this.$route.params.vertical_slug

      this.$store.commit('setIsLoading', true)
      await axios
          .get(`/api/v1/products/${verticalSlug}`)
          .then(response => {
            this.vertical = response.data

            document.title = this.vertical.name + ' | Cafe Teriack'
          })
          .catch(error => {
            console.log(error);

            toast({
              message: 'Something went wrong. Please try again.',
              type: 'is-danger',
              dismissible: true,
              pauseOnHover: true,
              duration: 2000,
              position: 'bottom-right',
            })
          })

      this.$store.commit('setIsLoading', false)
    }
  }
}
</script>

<style scoped>
.page-vertical {
  margin-top: 20px;
}

.title {
  color: #808000;
  margin-bottom: 30px;
  font-weight: bolder;
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
