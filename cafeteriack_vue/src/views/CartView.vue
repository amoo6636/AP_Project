<template>
    <div class="page-cart">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Cart</h1>
            </div>

            <div class="column is-12 box">
                <table class="table is-fullwidth is-centered" v-if="cartTotalLength">
                    <thead>
                        <tr>
                            <th>Product</th>
                            <th>Price</th>
                            <th>Quantity</th>
                            <th>Total</th>
                            <th></th>
                        </tr>
                    </thead>

                    <tbody>
                        <CartItem
                            v-for="item in cart.items"
                            v-bind:key="item.product.id"
                            v-bind:initialItem="item"
                            v-on:removeFromCart="removeFromCart" />
                    </tbody>
                </table>

                <p v-else class="empty-cart-message">Your shopping cart is empty, your coffee is getting cold!</p>
            </div>

            <div class="column is-12 box">
                <h2 class="subtitle">Summary</h2>

                <strong class="total-price">${{ cartTotalPrice.toFixed(2) }}</strong>, {{ cartTotalLength }} items
                <p></p>
                <div class="field">
                    <input v-model="checked" type="checkbox" name="check" id="serveOutside" />
                    <label for="serveOutside">{{checked ? 'Yes' : 'No'}} Serve outside</label>
                </div>
                <hr>
                <template v-if="cartTotalLength">
                    <button class="button custom-button" @click="submitForm">Pay</button>
                </template>
                
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import CartItem from '@/components/CartItem.vue'

export default {
    name: 'Cart',
    components: {
        CartItem
    },
    data() {
        return {
            cart: {
                items: [],
                checked: '',
            }
        }
    },
    mounted() {
        this.cart = this.$store.state.cart
    },
    methods: {
        removeFromCart(item) {
            this.cart.items = this.cart.items.filter(i => i.product.id !== item.product.id)
        },
        async submitForm(){
            this.$store.commit('setIsLoading', true)

            const items = []
            for (let i = 0; i < this.cart.items.length; i++) {
                const item = this.cart.items[i]
                const obj = {
                    product: item.product.id,
                    quantity: item.quantity,
                    price: item.product.price * item.quantity
                }

                items.push(obj)
            }
            const data = {
                'items': items,
            }
        await axios
            .post('/api/v1/checkout/', data)
            .then(response => {
                this.$store.commit('clearCart')
                this.cart.items = []
                console.log(response)
                // You can clear the cart here if you want
                this.$router.push('/my-account')
                
            })
            .catch(error => {
                console.error(error)
            })

            this.$store.commit('setIsLoading', false)
        }
    },
    computed: {
        cartTotalLength() {
            return this.cart.items.reduce((acc, curVal) => {
                return acc += curVal.quantity
            }, 0)
        },
        cartTotalPrice() {
            return this.cart.items.reduce((acc, curVal) => {
                return acc += curVal.product.price * curVal.quantity
            }, 0)
        },
    }
}
</script>

<style scoped>
.page-cart {
    margin-top: 20px;
}
.title {
    color: #808000;
    font-size: 2.5rem;
    text-align: center;
    margin-bottom: 20px;
}
.table {
    border-collapse: collapse;
    width: 100%;
    margin-bottom: 20px;
    table-layout: fixed;
}
.table th, .table td {
    border: 1px solid #ddd;
    padding: 8px;
    text-align: center;
    vertical-align: middle;
}
.table th {
    background-color: #f5f5f5;
    color: #333;
}
.table tbody tr:nth-child(even) {
    background-color: #f9f9f9;
}
.table tbody tr:hover {
    background-color: #f1f1f1;
}
.box {
    border: 1px solid #ddd;
    padding: 20px;
    margin-bottom: 20px;
    background-color: #fafafa;
    border-radius: 8px;
    text-align: center;
}
.empty-cart-message {
    text-align: center;
    color: #7a7a7a;
    font-style: italic;
}
.subtitle {
    color: #808000;
    font-size: 1.5rem;
    margin-bottom: 10px;
    font-weight: bold;
}
.total-price {
    font-size: 1.25rem;
    color: #808000;
    font-weight: bold;
}
.field {
    margin-top: 10px;
    color: #808000;
    font-weight: bold;
}
.custom-button {
    background-color: #808000;
    border-color: #808000;
    color: white;
    width: 10%;
    margin-top: 20px;
}
</style>