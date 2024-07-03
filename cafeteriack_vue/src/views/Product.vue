<template>
    <div class="page-product">
        <div class="columns is-multiline">
            <div class="column is-9">
                <figure class="image mb-6">
                    <img v-bind:src="product.get_image" alt="Product Image">
                </figure>
                <h1 class="title">{{ product.name }}</h1>

                <p>{{ product.description }}</p>

            </div>
            <div class="column is-3">
                <h2 class="subtitle">Information</h2>

                <p><strong>Price: </strong>$ {{ product.price }}</p>

                <div class="field has-addons mt-6">
                    <div class="control">
                        <input type="number" class="input" min="1" v-model="quantity" >
                    </div>

                    <div class="control">
                        <a class="button is-primary" @click="addtoCart">Add to cart</a>
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
                    message: 'Sorry, we do not have enough raw materials.',
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

<style scoped>
.page-product {
    margin-top: 20px;
}
.title {
    color: #CC7722;
    margin-bottom: 10px;
}
.subtitle {
    color: #333;
}
.field.has-addons {
    margin-top: 20px;
}
.control .input {
    border-radius: 5px 0 0 5px;
}
.control .button {
    border-radius: 0 5px 5px 0;
}
.image {
    border-radius: 10px;
    overflow: hidden;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}
.image img {
    max-width: 100%;
    transition: transform 0.3s;
}
.image img:hover {
    transform: scale(1.05);
}
a.button.is-primary {
    background-color: #CC7722;
    border-color: #CC7722;
    color: #fff;
}
a.button.is-primary:hover {
    background-color: #B05D1E;
    border-color: #B05D1E;
}
</style>
