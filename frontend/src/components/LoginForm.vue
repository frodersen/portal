<template>
  <div class="login-page">
    <div class="login-box">
      <h1>NTNUI PORTAL</h1>
      <form @submit.prevent="login">
        <!-- Country code and phone input container -->
        <div class="input-group">
          <select v-model="countryCode" id="countryCode" class="country-code">
            <option value="+47">Norge (+47)</option>
            <!-- other country options -->
          </select>
          <input
            v-model="phone"
            id="phone"
            type="tel"
            class="phone-number"
            placeholder="Telefonnummer"
          />
        </div>
        <label for="password">PASSORD</label>
        <input
          v-model="password"
          id="password"
          type="password"
          class="password-input"
          placeholder="Passord"
        />
        <button type="submit" class="login-button">LOGG INN</button>
        <div class="links">
          <a href="#">GLEMT PASSORD</a> | <a href="#">AKTIVER BRUKER</a>
        </div>
      </form>
    </div>
  </div>
</template>



<script>
import { ref } from "vue";
import axios from "axios";

export default {
  setup() {
    const countryCode = ref("+47"); 
    const phone = ref("");
    const password = ref("");
    const error = ref("");
    const phone_number = ref("");

    const login = async () => {
      try {
        const response = await axios({
          method: "post",
          url: "http://localhost:8000/auth/login/",
          data: {
            phone_number: countryCode.value + phone.value,
            password: password.value,
          },
          withCredentials: true,
          validateStatus: (status) => status < 500,
        });

        if (response.status === 401) {
          error.value = "Unauthorized, incorrect credentials";
          return;
        }

        if (response.status === 200) {
          const redirectUrl = getQueryParam("redirect_url");
          window.location.href = decodeURIComponent(redirectUrl);
        }
      } catch (err) {
        error.value = "Server error or network issue";
        console.error("Login error:", err);
      }
    };

    function getQueryParam(param) {
      const urlParams = new URLSearchParams(window.location.search);
      return urlParams.get(param);
    }

    return {
      phone_number,
      countryCode,
      phone,
      password,
      error,
      login,
    };
  },
};
</script>

<style scoped>
.login-page {
  background-color: #4b6b8b; /* Adjusted to match the blue background */
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
}

.login-box {
  background-color: #ffffff; /* White background for the form box */
  padding: 40px;
  border-radius: 10px; /* Slightly more rounded corners */
  width: 340px; /* Increased width */
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Soft box shadow */
  color: #2c3e50; /* Darker text color */
}

.login-box h1 {
  text-align: center;
  margin-bottom: 30px; /* More space below the heading */
  color: #000; /* Black color for the text */
  font-size: 24px; /* Larger font size */
}

.login-box label {
  display: block;
  margin-bottom: 5px;
  color: #000; /* Black color for the text */
  font-weight: bold; /* Bold font for labels */
}

.login-box select,
.login-box input[type="tel"],
.login-box input[type="password"] {
  width: 100%;
  padding: 15px; /* Increased padding */
  margin-bottom: 15px; /* Increased margin */
  border-radius: 5px;
  border: 1px solid #d3d3d3; /* Lighter border color */
  background: #f7f7f7; /* Light grey background */
  color: #333; /* Dark grey text */
}

.login-box select {
  -webkit-appearance: none; /* Removes default styling of select on WebKit browsers */
  -moz-appearance: none; /* Removes default styling of select on Firefox */
  appearance: none; /* Removes default arrow from select */
  background-image: url('data:image/svg+xml;utf8,<svg fill="#333" height="24" viewBox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg"><path d="M7 10l5 5 5-5z"/></svg>'); /* Add custom arrow */
  background-repeat: no-repeat;
  background-position-x: 95%;
  background-position-y: 50%;
}

.login-box button[type="submit"] {
  background-color: #007bff; /* Matching the blue button color */
  color: #fff;
  padding: 15px; /* Increased padding */
  margin-top: 10px; /* Added margin to the top */
  border: none;
  border-radius: 5px;
  width: 100%;
  cursor: pointer;
  font-size: 16px; /* Larger font size */
  font-weight: bold; /* Bold font */
  transition: background-color 0.3s; /* Transition for a hover effect */
}

.login-box button[type="submit"]:hover {
  background-color: #0056b3; /* Darker blue on hover */
}

.login-box p {
  text-align: center;
  margin-top: 20px;
}

.login-box p a {
  color: #007bff;
  text-decoration: none;
  margin: 0 5px; /* Spacing between links */
}

.login-box p a:hover {
  text-decoration: underline; /* Underline on hover */
}

.error-message {
  color: #ff0000; /* Red color for error messages */
  text-align: center;
}
.input-group {
  display: flex;
  justify-content: space-between; /* Adjust as needed */
  margin-bottom: 15px; /* Increased margin */
}

.country-code {
  flex: 1;
  margin-right: 5px; /* Spacing between select and input */
}

.phone-number {
  flex: 3;
}

</style>