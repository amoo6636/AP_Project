<template>
    <div class="page-sign-up">
        <div class="columns">
          <div class="column is-4 is-offset-4">
            <h1 class="title">Sign up</h1>

            <form @submit.prevent="submitForm">
              <div class="field">
                <label>Name</label>
                <div class="control">
                  <input type="text" class="input" v-model="name">
                </div>
              </div>

              <div class="field">
                <label>Username</label>
                <div class="control">
                  <input type="text" class="input" v-model="username">
                </div>
              </div>

              <div class="field">
                <label>Email</label>
                <div class="control">
                  <input type="email" class="input" v-model="email">
                </div>
              </div>

              <div class="field">
                <label>Password</label>
                <div class="control">
                  <input type="password" class="input" v-model="password">
                </div>
              </div>

              <div class="field">
                <label>Repeat password</label>
                <div class="control">
                  <input type="password" class="input" v-model="password2">
                </div>
              </div>

              <div class="field">
                <label>Phone Number</label>
                <div class="control">
                  <input type="tel" class="input" v-model="phoneNumber">
                </div>
              </div>

              <div class="notification is-danger" v-if="errors.length">
                <p v-for="error in errors" :key="error">{{ error }}</p>
              </div>

              <div class="field">
                <div class="control">
                  <button class="button is-dark">Sign up</button>
                </div>
              </div>

              <hr>

              Or
              <router-link to="/log-in">click here</router-link>
              to log in!
            </form>
          </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import {toast} from 'bulma-toast';

export default {
  name: 'SignUp',
  data() {
    return {
      name: '',
      username: '',
      email: '',
      password: '',
      password2: '',
      phoneNumber: '',
      errors: []
    };
  },
  methods: {
    submitForm() {
      this.errors = [];

      if (this.name === '') {
        this.errors.push('The name is missing');
      }

      if (this.username === '') {
        this.errors.push('The username is missing');
      }

      if (this.email === '') {
        this.errors.push('The email is missing');
      } else if (!this.validateEmail(this.email)) {
        this.errors.push('Invalid email address');
      }

      if (this.password === '') {
        this.errors.push('The password is too short');
      }

      if (this.password !== this.password2) {
        this.errors.push('The passwords don\'t match');
      }

      if (!this.phoneNumber) {
        this.errors.push('Phone number required.');
      } else if (!this.validatePhoneNumber(this.phoneNumber)) {
        this.errors.push('Invalid phone number.');
      }

      if (!this.errors.length) {
        const formData = {
          name: this.name,
          username: this.username,
          email: this.email,
          password: this.password,
          phoneNumber: this.phoneNumber
        };

        axios
            .post("/api/v1/users/", formData)
            .then(response => {
              toast({
                message: 'Account created, please log in!',
                type: 'is-success',
                dismissible: true,
                pauseOnHover: true,
                duration: 2000,
                position: 'bottom-right',
              });

              this.$router.push('/log-in');
            })
            .catch(error => {
              if (error.response) {
                for (const property in error.response.data) {
                  this.errors.push(`${property}: ${error.response.data[property]}`);
                }

                console.log(JSON.stringify(error.response.data));
              } else if (error.message) {
                this.errors.push('Something went wrong. Please try again');

                console.log(JSON.stringify(error));
              }
            });
      }
    },
    validatePhoneNumber(phoneNumber) {
      // Simple phone number validation (you can improve it based on your requirements)
      const phoneRegex = /^\+?[1-9]\d{1,14}$/;
      return phoneRegex.test(phoneNumber);
    },
    validateEmail(email) {
      // Simple email validation (you can improve it based on your requirements)
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      return emailRegex.test(email);
    }
  }
};
</script>