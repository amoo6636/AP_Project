<template>
    <div class="page-my-account">
        <div class="columns is-multiline">
            <div class="column is-12">
                <div class="account-header">
                    <h1 class="title has-text-centered">My Account</h1>
                    <h3 class="is-size-4 mb-6">- My Orders:</h3>
                </div>
            </div>

            <hr>

            <div class="column is-12">
                <OrderSummary
                    v-for="order in orders"
                    v-bind:key="order.id"
                    v-bind:order="order"
                />
            </div>
        </div>
    </div>
</template>


<script>
import axios from 'axios'
import OrderSummary from '@/components/OrderSummary.vue'
export default {
    name: 'MyAccount',
    components:{
        OrderSummary
    },
    data() {
        return{
            orders: []
        }
    },
    methods: {
        // logout() {
        //     axios.defaults.headers.common["Authorization"] = ""
        //
        //     localStorage.removeItem("token")
        //     localStorage.removeItem("username")
        //     localStorage.removeItem("userid")
        //
        //     this.$store.commit('removeToken')
        //
        //     this.$router.push('/')
        // },
        getMyOrders() {

            axios
                .get('/api/v1/orders/')
                .then(response => {
                    this.orders = response.data
                })
                .catch(error => {
                    console.log(error)
                })
        }
    },
    mounted() {
        document.title = 'My Account | Total'

        this.getMyOrders()
    },
}
</script>

<style scoped>
.page-my-account .account-header {
    display: block;
}

.page-my-account .title,
.page-my-account .is-size-4 {
    margin: 0;
    padding-left: 10px;
}

.page-my-account .is-size-4 {
  margin-top: 50px;
  color: #7B3F00;
  font-weight: bold;
  font-style: italic;
  margin-left: 30px;
}
.page-my-account .title {
  margin-top: 20px;
  font-size: 2.5rem;
  color: #E1C16E;
}

</style>
