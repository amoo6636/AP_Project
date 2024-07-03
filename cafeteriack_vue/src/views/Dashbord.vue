<template>
    <div class="page-dashbort">

        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Dashboard</h1>
            </div>

            <div class="column is-9">
    
    
                <div class="box">
                    <div class="container">
                        <Bar v-if="loaded" :data="chartData" />
                    </div>
                </div>
        
                <div class="box">
                    <div class="field">
                        <label class="label">Vertical</label>
                        <div class="control">
                            <label class="radio">
                                <input type="radio" id="one" value="hotdrinks" v-model="vertical_slug" />
                                Hot Drinks
                            </label>

                            <label class="radio">
                                <input type="radio" id="two" value="icedrinks" v-model="vertical_slug" />
                                Ice Drinks
                            </label>

                            <label class="radio">
                                <input type="radio" id="three" value="desserts" v-model="vertical_slug" />
                                Desserts
                            </label>

                            <label class="radio">
                                <input type="radio" id="four" value="cakes" v-model="vertical_slug" />
                                Cakes
                            </label>
                        </div>
                    </div>

                    <div class="field">
                        <div class="control">
                            <button class="button is-success" @click="DrawChart">Draw</button>
                        </div>
                    </div>
                </div>    
            </div>

            <div class="column is-3">
                <div class="box">
                    <div class="field">
                        <router-link :to="{ name: 'AddProduct' }" class="button is-light is-fullwidth mt-4">Add Product</router-link>
                    </div>

                    <div class="field">
                        <router-link :to="{ name: 'Storage' }" class="button is-light is-fullwidth mt-4">Storage</router-link>
                    </div>
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

<style scoped>
.page-dashboard {
    margin-top: 20px;
}
.title {
    color: #CC7722;
    text-align: left;
    margin-bottom: 20px;
}
.box {
    margin-bottom: 20px;
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}
.label {
    color: #333;
    font-weight: bold;
    margin-bottom: 10px;
}
.radio {
    margin-right: 15px;
}
.button.is-success {
    background-color: #CC7722;
    border-color: #CC7722;
    color: #fff;
}
.button.is-success:hover {
    background-color: #B05D1E;
    border-color: #B05D1E;
}
.button.is-light {
    background-color: #f5f5f5;
    border-color: #ddd;
}
.button.is-light:hover {
    background-color: #e6e6e6;
    border-color: #ccc;
}
.button.is-fullwidth {
    width: 100%;
}
</style>
