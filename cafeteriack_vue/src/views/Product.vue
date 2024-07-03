<template>
    <div class="page-product">
        <div class="columns is-multiline">
            <div class="column is-9">
                <figure class="image mb-6">
                    <img v-bind:src="product.get_image">
                </figure>
                <h1 class="title">{{ product.name }}</h1>

                <p>{{ product.description }}</p>

            </div>
            <div class="column is-3">
                <h2 class="subtitle">Information</h2>

                <p><strong>Price: </strong>$ {{ product.price }}</p>

                <div class="fields has-addons mt-6">
                    <div class="control">
                        <input type="number" class="input" min="1" v-model="quantity" >
                    </div>

                    <div class="control">
                        <a class="button is-dark" @click="addtoCart">Add to cart</a>
                    </div>

                </div>
            </div>
        </div>

    </div>
</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'

export default {
    name: 'Product',
    data(){
        return {
            product : {},
            quantity: 1,
            storages: {}
            
        }
    },
    mounted() {
        this.getProduct()
    },
    methods: {
        async getProduct(){
            this.$store.commit('setIsLoading', true)

            const vertical_slug = this.$route.params.vertical_slug
            const product_slug = this.$route.params.product_slug

            await axios
                .get(`/api/v1/products/${vertical_slug}/${product_slug}`)
                .then(response =>{
                    this.product = response.data

                     document.title = this.product.name + ' | Cafe Teriack'
                })
                .catch(error =>{
                    console.log(error);
                })

            this.$store.commit('setIsLoading', false)
        },
        storagehandler(item){
            const sugar_store = this.storages[0]['amount']-this.quantity*this.product.sugar
            const coffee_store = this.storages[1]['amount']-this.quantity*this.product.coffee
            const flour_store = this.storages[2]['amount']-this.quantity*this.product.flour
            const chocolate_store = this.storages[3]['amount']-this.quantity*this.product.chocolate

            if (sugar_store >= 0 && coffee_store>= 0 && flour_store >= 0 && chocolate_store >= 0){
                
            axios
                .post('/api/v1/update-storage/',  {
                                            "sugar_amount": sugar_store,
                                            "coffee_amount": coffee_store,
                                            "flour_amount": flour_store,
                                            "chocolate_amount": chocolate_store
                                            })
                .then(response =>{
                    this.$store.commit('addToCart', item)
                    toast({
                        message: 'Sweet hot tastes added to your card! make ready',
                        type: 'is-success',
                        dismissible: true,
                        pauseOnHover: true,
                        duration: 2500,
                        position: 'bottom-right',
                    })
                }) 
                .catch(error =>{
                    console.log(error);
                })
            } else {
                toast({
                message: 'Sory we do not have raw materials',
                type: 'is-danger',
                dismissible: true,
                pauseOnHover: true,
                duration: 2500,
                position: 'bottom-right',
                }) 
            }

        },
        async addtoCart(){
            this.$store.commit('setIsLoading',true)

            if (isNaN(this.quantity) || this.quantity < 1){
            this.quantity = 1
            }
            const item = {
                product: this.product,
                quantity: this.quantity
            }
            
            await axios
                .get('/api/v1/storage')
                .then(response =>{
                    this.storages = response.data
                    this.storagehandler(item)
                })
                .catch(error =>{
                    console.log(error);
                })
                
            this.$store.commit('setIsLoading',false)

        }
    
    }

}
</script>
