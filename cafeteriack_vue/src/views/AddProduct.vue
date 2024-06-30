<template>
    <div class="page-add-product">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Add Product</h1>
            </div>

            <div class="column is-6">
                <div class="field">
                    <label>Name</label>

                    <div class="control">
                        <input type="text" name="name" class="input" v-model="product.name">
                    </div>
                </div>

                <div class="field">
                    <label>Slug</label>

                    <div class="control">
                        <input type="text" name="slug" class="input" v-model="product.slug">
                    </div>
                </div>

                <div class="field">
                    <label>Price</label>

                    <div class="control">
                        <input type="number" name="price" class="input" v-model="product.price">
                    </div>
                </div>

                <div class="field">
                    <label>Vertical</label>
                    
                    <div class="control">
                        <select name="Vertical" v-model="product.vertical">
                            <option disabled value="">Please select one</option>
                            <option value="hotdrinks">Hot Drinks</option>
                            <option value="icedrinks">Ice Drinks</option>
                            <option value="desserts">Desserts</option>
                            <option value="cakes">Cakes</option>
                        </select>
                    </div>
                </div>

            </div>

            
            <div class="column is-6">
                <div class="field">
                    <label>Sugar</label>

                    <div class="control">
                        <input type="number" name="sugar" class="input" v-model="product.sugar">
                    </div>
                </div>

                <div class="field">
                    <label>Coffee</label>

                    <div class="control">
                        <input type="number" name="coffee" class="input" v-model="product.coffee">
                    </div>
                </div>

                <div class="field">
                    <label>Flour</label>

                    <div class="control">
                        <input type="number" name="flour" class="input" v-model="product.flour">
                    </div>
                </div>

                <div class="field">
                    <label>Chocolate</label>

                    <div class="control">
                        <input type="number" name="chocolate" class="input" v-model="product.chocolate">
                    </div>
                </div>

            </div>

            
            <div class="column is-12">
                <div class="field">
                    <label>Description</label>

                    <div class="control">
                        <input type="text" name="description" class="input" v-model="product.description">
                    </div>
                </div>

                <div class="field">
                    <label>Image</label>

                    <div class="control">
                        <input type="file" id="file" ref="myImage" class="custom-file-input" @change="previewFiles">
                    </div>
                </div>

                <div class="field">
                    <div class="control">
                        <button class="button is-success" @click="submitFrom">Sumbmit</button>
                    </div>
                </div>

            </div>

        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'AddProduct',
    data() {
        return {
            product: {}
         }
    },
    mounted() {
        document.title = 'Add Product | Cafe Teriack'
    },
    methods: {
        previewFiles() {
            this.product.image = this.$refs.myImage.files
        },
        submitFrom() {
            console.log(this.product)
            axios
                .post('/api/v1/add/',this.product)
                .then(response =>{
                    this.$router.push('/')
                })
                .catch(error =>{
                    console.log(JSON.stringify(error))
                })
        }
        
    }
    
}

</script>