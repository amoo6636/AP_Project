<template>
    <div class="page-add-product">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Add Product</h1>
            </div>

            <div class="column is-4.5">
                <div class="box">
                    <div class="field">
                        <label class="label">Name</label>
                        <div class="control">
                            <input type="text" name="name" class="input" v-model="name">
                        </div>
                    </div>

                    <div class="field">
                        <label class="label">Slug</label>
                        <div class="control">
                            <input type="text" name="slug" class="input" v-model="slug">
                        </div>
                    </div>

                    <div class="field">
                        <label class="label">Price</label>
                        <div class="control">
                            <input type="number" name="price" class="input" v-model="price">
                        </div>
                    </div>

                    <div class="field">
                        <label class="label">Vertical</label>
                        <div class="control">
                            <div class="select is-fullwidth">
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
                </div>
            </div>

            <div class="column is-4.5">
                <div class="box">
                    <div class="field">
                        <label class="label">Sugar</label>
                        <div class="control">
                            <input type="number" name="sugar" class="input" v-model="sugar">
                        </div>
                    </div>

                    <div class="field">
                        <label class="label">Coffee</label>
                        <div class="control">
                            <input type="number" name="coffee" class="input" v-model="coffee">
                        </div>
                    </div>

                    <div class="field">
                        <label class="label">Flour</label>
                        <div class="control">
                            <input type="number" name="flour" class="input" v-model="flour">
                        </div>
                    </div>

                    <div class="field">
                        <label class="label">Chocolate</label>
                        <div class="control">
                            <input type="number" name="chocolate" class="input" v-model="chocolate">
                        </div>
                    </div>
                </div>
            </div>

            <div class="column is-3">
                <div class="box">
                    <div class="field">
                        <router-link :to="{ name: 'Dashbord' }" class="button is-light is-fullwidth mt-4">Dashboard</router-link>
                    </div>
                    <div class="field">
                        <router-link :to="{ name: 'Storage' }" class="button is-light is-fullwidth mt-4">Storage</router-link>
                    </div>
                </div>
            </div>

            <div class="column is-9">
                <div class="box">
                    <div class="field">
                        <label class="label">Description</label>
                        <div class="control">
                            <textarea name="description" class="textarea" v-model="description"></textarea>
                        </div>
                    </div>

                    <div class="field">
                        <label class="label">Image</label>
                        <div class="file has-name is-fullwidth">
                            <label class="file-label">
                                <input type="file" ref="file" class="file-input" @change="selectFile">
                                <span class="file-cta">
                                    <span class="file-label">Choose an image...</span>
                                </span>
                                <span class="file-name" v-if="image">{{ image.name }}</span>
                            </label>
                        </div>
                    </div>

                    <div class="field">
                        <div class="control">
                            <button class="button is-success is-fullwidth" @click="submitForm">Submit</button>
                        </div>
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
            price: '',
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
        selectFile() {
            this.image = this.$refs.file.files[0]
        },
        submitForm() {
            let formData = new FormData()
            formData.append('name', this.name)
            formData.append('slug', this.slug)
            formData.append('price', this.price)
            formData.append('vertical', this.vertical)
            formData.append('sugar', this.sugar)
            formData.append('coffee', this.coffee)
            formData.append('flour', this.flour)
            formData.append('chocolate', this.chocolate)
            formData.append('description', this.description)
            formData.append('image', this.image)

            axios
                .post('/api/v1/add/', formData)
                .then(response => {
                    this.$router.push('/dashboard')
                })
                .catch(error => {
                    console.log(JSON.stringify(error))
                })
        }
    }
}
</script>

<style scoped>
.page-add-product {
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
    color: #6F4E37;
    font-weight: bold;
    margin-bottom: 10px;
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

.file.has-name .file-name {
    max-width: 100%;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
}
</style>
