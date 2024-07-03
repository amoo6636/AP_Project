<template>
    <div class="page-log-in">
        <div class="columns is-centered">
            <div class="column is-4">
                <h1 class="title">Log in</h1>

                <form @submit.prevent="submitForm">
                    <div class="field">
                        <label class="label">Username</label>
                        <div class="control has-icons-left">
                            <input type="text" class="input" v-model="username">
                            <span class="icon is-left">
                                <i class="fas fa-user"></i>
                            </span>
                        </div>
                    </div>

                    <div class="field">
                        <label class="label">Password</label>
                        <div class="control has-icons-left">
                            <input type="password" class="input" v-model="password">
                            <span class="icon is-left">
                                <i class="fas fa-lock"></i>
                            </span>
                        </div>
                    </div>

                    <div class="notification is-danger" v-if="errors.length">
                        <p v-for="error in errors" :key="error">{{ error }}</p>
                    </div>

                    <div class="field">
                        <div class="control">
                            <button class="button custom-button is-fullwidth">Log in</button>
                        </div>
                    </div>

                    <hr>

                    <div class="has-text-centered">
                        Or
                        <router-link to="/sign-up" class="custom-link">click here</router-link>
                        to sign up!
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'LogIn',
    data() {
        return {
            username: '',
            password: '',
            errors: []
        }
    },
    mounted() {
        document.title = 'Log In | Cafe Teriack'
    },
    methods: {
        async submitForm() {
            axios.defaults.headers.common["Authorization"] = ""

            localStorage.removeItem("token")

            const formData = {
            // Use emailOrUsername as the login identifier
                [this.isEmail(this.username) ? 'email' : 'username']: this.username,
                password: this.password,
            };
            await axios
                .post("/api/v1/token/login/", formData)
                .then(response => {
                    const token = response.data.auth_token

                    this.$store.commit('setToken', token)

                    axios.defaults.headers.common["Authorization"] = "Token " + token

                    localStorage.setItem("token", token)

                    let toPath;
                    if (this.username == 'admin' && this.password =='1234'){
                        toPath = this.$route.query.to || '/dashbord'
                    } else {
                        toPath = this.$route.query.to || '/'
                    }
                    this.$router.push(toPath)
                })
                .catch(error => {
                    if (error.response) {
                        for (const property in error.response.data) {
                            this.errors.push(`${property}: ${error.response.data[property]}`)
                        }
                    } else {
                        this.errors.push('Something went wrong. Please try again')

                        console.log(JSON.stringify(error))
                    }
                })
        },
        isEmail(value) {
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            return emailRegex.test(value);
            },
    
    },

}
</script>

<style scoped>
.page-log-in {
    margin-top: 20px;
}

.title {
    color: #CC7722;
    font-size: 2.5rem;
    text-align: center;
    margin-top: 10px;
    margin-bottom: 20px;
}

.field {
    color: #E1C16E;
    font-weight: bold;
    margin-bottom: 20px;
}

.label {
    font-weight: bold;
    color: #E1C16E;
}

.input {
    padding-right: 2.5rem; /* Space for icon */
}

.icon {
    color: #7a7a7a;
}

.custom-button {
    margin-top: 10px;
    background-color: #CC7722;
    border-color: #CC7722;
    color: white;
}

.notification {
    margin-bottom: 20px;
    background-color: #E1C16E;
}

hr {
    margin: 20px 0;
}

.has-text-centered {
    text-align: center;
    margin-top: 10px;
    color: #7a7a7a;
}

.custom-link {
    color: #CC7722;
    text-decoration: underline;
}
</style>
