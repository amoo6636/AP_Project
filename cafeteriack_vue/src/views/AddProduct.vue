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
                        <input type="text" name="name" class="input" v-model="name">
                    </div>
                </div>

                <div class="field">
                    <label>Slug</label>

                    <div class="control">
                        <input type="text" name="slug" class="input" v-model="slug">
                    </div>
                </div>

                <div class="field">
                    <label>Price</label>

                    <div class="control">
                        <input type="number" name="price" class="input" v-model="price">
                    </div>
                </div>

                <div class="field">
                    <label>Vertical</label>
                    
                    <div class="control">
                        <select name="Vertical" v-model="vertical">
                            <option disabled value="">Please select one</option>
                            <option value="1">Hot Drinks</option>
                            <option value="2">Ice Drinks</option>
                            <option value="3">Desserts</option>
                            <option value="4">Cakes</option>
                        </select>
                    </div>
                </div>

            </div>

            
            <div class="column is-6">
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

            </div>

            
            <div class="column is-12">
                <div class="field">
                    <label>Description</label>

                    <div class="control">
                        <input type="text" name="description" class="input" v-model="description">
                    </div>
                </div>

                <div class="file">
                    <label class="file-label">Image

                        <input type="file" ref="file" class="file-input" @change="selectFile">
                        <span class="file-cta">
                            <span class="file-labe">Choose an image...</span>
                        </span>
        
                    </label>
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
            name: '',
            slug: '',
            price:'',
            vertical: '',
            sugar: '',
            coffee: '',
            flour: '',
            chocolate: '',
            description: '',
            image: null
         }
    },
    mounted() {
        document.title = 'Add Product | Cafe Teriack'
    },
    methods: {
        selectFile(){
            this.image = this.$refs.file.files.item(0)
        },
        submitFrom(){

            let formData = new FormData();
            formData.append('name',this.name);
            formData.append('slug', this.slug);
            formData.append('price',this.price);
            formData.append('vertical',this.vertical);
            formData.append('sugar', this.sugar);
            formData.append('coffee', this.coffee);
            formData.append('flour', this.flour);
            formData.append('chocolate', this.chocolate);
            formData.append('description', this.description);
            formData.append('image', this.image);

            axios
                .post('/api/v1/add/', formData)
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