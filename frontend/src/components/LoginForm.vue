<template>
    <div class="login-page">
      <div class="login-box">
        <h1>NTNUI PORTAL</h1>
        <form @submit.prevent="login">
          <label for="phone">TELEFON →</label>
          <input v-model="phone" id="phone" type="tel" placeholder="Telefonnummer">
          <label for="password">PASSORD</label>
          <input v-model="password" id="password" type="password" placeholder="Passord">
          <button type="submit">LOGG INN</button>
          <p><a href="#">GLEMT PASSORD</a> | <a href="#">AKTIVER BRUKER</a></p>
        </form>
      </div>
    </div>
  </template>
  
  <script>
import { ref } from 'vue';
import axios from 'axios';
import { useRouter } from 'vue-router';

export default {
  setup() {
    const phone = ref('');
    const password = ref('');
    const router = useRouter();

    const login = async () => {
      try {
        const response = await axios.post('http://127.0.0.1:8000/auth/login/', {
          phone_number: phone.value,
          password: password.value,
        });
        // Store the access token securely, consider using HttpOnly cookies
        // For this example, it's stored in localStorage but this is NOT recommended for production
        localStorage.setItem('access_token', response.data.access);
        router.push({ name: 'UserProfile' }); // Navigate to UserProfile route after login
      } catch (error) {
        console.error('Login error:', error.response.data);
        // Handle login error, show user feedback
      }
    };

    return {
      phone,
      password,
      login,
    };
  },
};
</script>

  
  <style scoped>
  .login-page {
    background-color: #007bff;
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  
  .login-box {
    background-color: #fff;
    padding: 30px;
    border-radius: 5px;
    width: 300px;
  }
  
  .login-box h1 {
    text-align: center;
    margin-bottom: 20px;
  }
  
  .login-box label {
    display: block;
    margin-bottom: 5px;
  }
  
  .login-box input[type="tel"],
  .login-box input[type="password"] {
    width: 100%;
    padding: 10px;
    margin-bottom: 10px;
    border-radius: 5px;
    border: 1px solid #ccc;
  }
  
  .login-box button[type="submit"] {
    background-color: #007bff;
    color: #fff;
    padding: 10px;
    border: none;
    border-radius: 5px;
    width: 100%;
    cursor: pointer;
  }
  
  .login-box p {
    text-align: center;
    margin-top: 20px;
  }
  
  .login-box p a {
    color: #007bff;
    text-decoration: none;
  }
  </style>