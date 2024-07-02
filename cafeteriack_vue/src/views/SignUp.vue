<template>
    <div class="page-sign-up">
        <div class="columns is-centered">
          <div class="column is-4">
            <h1 class="title has-text-centered">Sign up</h1>

            <form @submit.prevent="submitForm">
              <div class="field">
                <label class="label">Name</label>
                <div class="control has-icons-left">
                  <input type="text" class="input" v-model="name">
                  <span class="icon is-left">
                    <i class="fas fa-user"></i>
                  </span>
                </div>
              </div>

              <div class="field">
                <label class="label">Username</label>
                <div class="control has-icons-left">
                  <input type="text" class="input" v-model="username">
                  <span class="icon is-left">
                    <i class="fas fa-user-circle"></i>
                  </span>
                </div>
              </div>

              <div class="field">
                <label class="label">Email</label>
                <div class="control has-icons-left">
                  <input type="email" class="input" v-model="email">
                  <span class="icon is-left">
                    <i class="fas fa-envelope"></i>
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

              <div class="field">
                <label class="label">Repeat password</label>
                <div class="control has-icons-left">
                  <input type="password" class="input" v-model="password2">
                  <span class="icon is-left">
                    <i class="fas fa-lock"></i>
                  </span>
                </div>
              </div>

              <div class="field">
                <label class="label">Phone Number</label>
                <div class="control has-icons-left">
                  <input type="tel" class="input" v-model="phoneNumber">
                  <span class="icon is-left">
                    <i class="fas fa-phone"></i>
                  </span>
                </div>
              </div>

              <div class="notification is-danger" v-if="errors.length">
                <p v-for="error in errors" :key="error">{{ error }}</p>
              </div>

              <div class="field">
                <div class="control">
                  <button class="button is-primary is-fullwidth custom-button">Sign up</button>
                </div>
              </div>

              <hr>

              <div class="has-text-centered">
                Or
                <router-link to="/log-in" class="custom-link">click here</router-link>
                to log in!
              </div>
            </form>
          </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import { toast } from 'bulma-toast';

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

<style scoped>
.page-sign-up {
  margin-top: 20px;
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

.button {
  margin-top: 10px;
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
  color: black;
}

.custom-link {
  color: #D27D2D;
  text-decoration: underline;
}
.custom-button {
  color: white;
  background-color: #D27D2D;
}
.title {
  color: #D27D2D;
  font-size: 2.5rem;
  margin-bottom: 20px;
}
</style>
