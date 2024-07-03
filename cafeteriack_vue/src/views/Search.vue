<template>
    <div class="page-search">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title has-text-centered">Search</h1>

                <h2 class="is-size-5 has-text-grey has-text-centered">Search term: "{{ query }}"</h2>
            </div>

            <div
                class="column is-3"
                v-for="product in products"
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

export default {
    name: 'Search',
    data() {
        return {
            products: [],
            query: ''
        }
    },
    mounted() {
        document.title = 'Search | Cafe Teriack'

        let url = window.location.search.substring(1)
        let params = new URLSearchParams(url)

        if (params.get('query')) {
            this.query = params.get('query')

            this.performsearch()
        }
    },
    methods: {
        async performsearch() {
            this.$store.commit('setIsLoading', true)

            await axios
                .post('api/v1/products/search/', { 'query': this.query })
                .then(response => {
                    this.products = response.data
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
.page-search {
    margin-top: 20px;
}

.title {
    color: #808000;
    margin-bottom: 10px;
    font-size: 45px;
}

.is-size-5.has-text-grey {
    margin-bottom: 30px;
}

.product-box {
    transition: transform 0.3s, box-shadow 0.3s;
    text-align: center;
    border-radius: 10px;
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
