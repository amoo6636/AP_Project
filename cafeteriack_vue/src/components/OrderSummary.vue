<template>
    <div class="box mb-4 order-summary">
        <h4 class="is-size-5">Order {{ calc }}</h4>

        <table class="table is-fullwidth">
            <thead>
                <tr>
                    <th>Product</th>
                    <th>Price</th>
                    <th>Quantity</th>
                    <th>Total</th>
                </tr>
            </thead>

            <tbody>
                <tr v-for="item in order.items" :key="item.product.id">
                    <td>{{ item.product.name }}</td>
                    <td>${{ item.product.price }}</td>
                    <td>{{ item.quantity }}</td>
                    <td>${{ getItemTotal(item).toFixed(2) }}</td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
export default {
    name: 'OrderSummary',
    props: {
        order: Object
    },
    methods: {
        getItemTotal(item) {
            return item.quantity * item.product.price;
        },
        orderTotalLength(order) {
            return order.items.reduce((acc, curVal) => {
                return acc + curVal.quantity;
            }, 0);
        }
    }
};
</script>

<style scoped>
/* Container Styles */
.order-summary {
    padding: 20px;
    border: 1px solid #ddd;
    border-radius: 8px;
    background-color: #EADDCA;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    margin-bottom: 20px;
}

/* Heading Styles */
.order-summary h4 {
    margin-bottom: 15px;
    color: #333;
    font-weight: bold;
}

/* Table Styles */
.table {
    width: 100%;
    border-collapse: collapse;
}

.table th, .table td {
    padding: 10px;
    border: 1px solid #EADDCA;
    text-align: left;
}

.table th {
    background-color: #E1C16E;
    font-weight: bold;
}

.table tbody tr:nth-child(odd) {
    background-color: #f9f9f9;
}

.table tbody tr:hover {
    background-color: #f1f1f1;
}
</style>
