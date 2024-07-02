<template>
    <div class="page-storage">
        <div class="columns is-multiline">

            <div class="column is-12">
                <h1 class="title">Storage</h1>
            
                <h1> Our storage have:</h1>
            </div>  

                <div class="column is-9">
                <div
                    v-for="storage in storages"
                    v-bind:key="storage.id"
                    >
                    <p class="is-size-6 has-text-grey">{{ storage.name }} : {{ storage.amount }}</p>

                </div>

                <div class="field">
                    <label>Sugar</label>

                    <div class="control">
                        <input type="number" name="sugar" class="input" v-model="sugar">
                    </div>
                </div>

                <div class="field">
                    <label>Coffee</label>

                    <div class="control">
                        <input type="number" name="coffee" class="input" v-model="coffee">
                    </div>
                </div>

                <div class="field">
                    <label>Flour</label>

                    <div class="control">
                        <input type="number" name="flour" class="input" v-model="flour">
                    </div>
                </div>

                <div class="field">
                    <label>Chocolate</label>

                    <div class="control">
                        <input type="number" name="chocolate" class="input" v-model="chocolate">
                    </div>
                </div>

                <div class="field">
                    <div class="control">
                        <button class="button is-success" @click="UpdateStorage">َUpdate Storage</button>
                    </div>
                </div>

            </div>

            <div class="column is-3">
                <div class="field">
                    <router-link :to="{name: 'Dashbord' }" class="button is-light mt-4">Dashbord</router-link>
                </div>

                <div class="field">
                <router-link :to="{name: 'AddProduct' }" class="button is-light mt-4">Add Product</router-link>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    name: 'Storage',
    data(){
        return {
            storages: {},
            sugar: '',
            coffee:  '',
            flour:  '',
            chocolate: ''
        }
    },
    mounted(){
        document.title = 'Storage | Cafe Teriack'
        this.getStorage()
    },
    methods: {
        async UpdateStorage(){
            this.$store.commit('setIsLoading', true)

            const sugar_amount = this.sugar
            const coffee_amount = this.coffee
            const flour_amount = this.flour
            const chocolate_amount = this.chocolate
            
            this.$store.commit('setStorage', sugar_amount, coffee_amount, flour_amount, chocolate_amount)
            axios
                .post('/api/v1/update-storage/',  {
                                            "sugar_amount": sugar_amount,
                                            "coffee_amount": coffee_amount,
                                            "flour_amount": flour_amount,
                                            "chocolate_amount": chocolate_amount
                                            })
                .catch(error =>{
                    console.log(error);
                })
            this.$router.push('/dashbord')

            this.$store.commit('setIsLoading', false)
        },
        getStorage() {
            axios
                .get('/api/v1/storage')
                .then(response =>{
                    this.storages = response.data
                })
                .catch(error =>{
                    console.log(error);
                })        

        }
    }

}
</script>

