<template>
    <div class="login-page">
      <div class="login-box">
        <h1>NTNUI PORTAL</h1>
        <form @submit.prevent="login">
          <label for="phone">TELEFON →</label>
          <input v-model="phone" id="phone" type="tel" pattern="[0-9]{8}">
          <label for="password">PASSORD</label>
          <input v-model="password" id="password" type="password">
          <button type="submit">LOGG INN</button>
          <p><a href="#">GLEMT PASSORD</a> | <a href="#">AKTIVER BRUKER</a></p>
        </form>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        phone: '',
        password: ''
      }
    },
    methods: {
      login() {
        // Send a request to your API to log in the user
      }
    }
  }
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