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
    mounted(){
        document.title = 'Search | Cafe Teriack'

        let url=window.location.search.substring(1)
        let params= new URLSearchParams(url)

        if(params.get('query')){
            this.query=params.get('query')

            this.performsearch()
        }
    },
    methods: {
        async performsearch(){
            this.$store.commit('setIsLoading',true)

            await axios
            .post('api/v1/products/search/', {'query': this.query})
            .then (response =>{
                this.products = response.data
            })
            .catch(error=>{
                console.log(error)
            })

            this.$store.commit('setIsLoading',false)
            
        }
    }

}
</script>