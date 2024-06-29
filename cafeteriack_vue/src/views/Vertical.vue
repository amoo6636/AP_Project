<template>
    <div class="page-vertical">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h2 class="is-size-2 has-text-centered">{{ vertical.name }}</h2>
            </div>
 
        <div
            class="column is-3"
            v-for="product in vertical.products"
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
import {toast} from 'bulma-toast'

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
            if (to.name ==='Vertical') {
                this.getVertical()
            }
        }
    },
    methods: {
        async getVertical() {
            const verticalSlug = this.$route.params.vertical_slug

            this.$store.commit('setIsLoading',true)
            await axios
                    .get(`/api/v1/products/${verticalSlug}`)
                    .then(response =>{
                        this.vertical = response.data

                        document.title = this.vertical.name + ' | Cafe Teriack'
                    })
                    .catch(error =>{
                    console.log(error);

                    toast({
                        message: 'Something went wrong. Please try again.',
                        type: 'is-danger',
                        dismissable: true,
                        pauseOnHover: true,
                        duration: 2000,
                        position: 'bottom-right',
                    })
                })

            this.$store.commit('setIsLoading',false)

        }
    }

}
</script>