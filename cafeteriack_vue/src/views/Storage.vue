<template>
    <div class="page-storage">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Storage</h1>
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
export default {

}
</script>

