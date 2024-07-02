<template>
    <div class="page-dashbort">

        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Dashbord</h1>
            </div>

            <div class="column is-9">
    
    
                <div class="container">
                    <Bar v-if="loaded" :data="chartData" />
                </div>
        
                <div class="field">
                    <label>Vertical</label>

                    <div class="control">
                        <input type="radio" id="one" value="hotdrinks" v-model="vertical_slug" />
                        <label for="one">Hot Drinks </label>

                        <input type="radio" id="two" value="icedrinks" v-model="vertical_slug"/>
                        <label for="two">Ice Drinks </label>

                        <input type="radio" id="three" value="desserts" v-model="vertical_slug"/>
                        <label for="three">Desserts </label>

                        <input type="radio" id="four" value="cakes" v-model="vertical_slug"/>
                        <label for="four">Cakes </label>

                    </div>

                    <div class="field">
                        <div class="control">
                            <button class="button is-success" @click="DrawChart">Draw</button>
                        </div>
                    </div>
                </div>    
            </div>

            <div class="column is-3">
                <div class="field">
                    <router-link :to="{name: 'AddProduct' }" class="button is-light mt-4">Add Product</router-link>
                </div>

                <div class="field">
                <router-link :to="{name: 'Storage' }" class="button is-light mt-4">Storage</router-link>
                </div>
            </div>
            
        </div>        
    </div>


</template>


<script>
import { Bar } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'
import axios from 'axios'

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

export default {
  name: 'BarChart',
  components: { Bar },
  data() {
    return {
        loaded: false,
        chartData: {},
        vertical_slug: ''
    }
  },
  mounted(){
    document.title = 'Dashbord | Cafe Teriack'
  },
  methods: {
    async DrawChart(){
        this.$store.commit('setIsLoading', true)
        const vertical_slug = this.vertical_slug

        await axios
                .get(`/api/v1/charts/${vertical_slug}`)
                .then(response =>{
                    console.log(response.data)
                    this.chartData = response.data
                    this.loaded = true
                })
                .catch(error =>{
                    console.log(error);
                })

        this.$store.commit('setIsLoading', false)
    }
  }
}

</script>


