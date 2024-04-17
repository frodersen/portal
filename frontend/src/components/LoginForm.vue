<template>
  <div class="login-page">
    <div class="login-box">
      <h1>NTNUI PORTAL</h1>
      <form @submit.prevent="getToken">
        <label for="phone">TELEFON →</label>
        <input
          v-model="phone"
          id="phone"
          type="tel"
          placeholder="Telefonnummer"
        />
        <label for="password">PASSORD</label>
        <input
          v-model="password"
          id="password"
          type="password"
          placeholder="Passord"
        />
        <button type="submit">LOGG INN</button>
        <p><a href="#">GLEMT PASSORD</a> | <a href="#">AKTIVER BRUKER</a></p>
      </form>
      <p v-if="error">{{ error }}</p>
    </div>
  </div>
</template>

<script>
import { ref } from "vue";
import axios from "axios";

export default {
  setup() {
    const phone = ref("");
    const password = ref("");
    const error = ref("");

    const getToken = async () => {
      try {
        const response = await axios({
          method: "post",
          url: "http://127.0.0.1:8000/auth/login/",
          data: {
            phone_number: phone.value,
            password: password.value,
          },
          validateStatus: (status) => status < 500,
        });

        if (response.status === 401) {
          error.value = "Unauthorized, incorrect credentials";
          return;
        }

        if (response.status === 200) {
          localStorage.setItem("access_token", response.data.access);
          await getUserData(response.data.access);
        }
      } catch (err) {
        error.value = "Server error or network issue";
        console.error("Login error:", err);
      }
    };

    const getUserData = async (token) => {
      try {
        const userProfileResponse = await axios({
          method: "get",
          url: "http://127.0.0.1:8000/auth/user-profile/",
          headers: { Authorization: `Bearer ${token}` },
          validateStatus: (status) => status < 500,
        });

        if (userProfileResponse.status == 403) {
          console.log("Invalid or expired token.");
          return;
        }

        if (userProfileResponse.status === 200) {
          console.log(userProfileResponse.data);
          // Redirect user back to the client which they came from
        } else {
          error.value = "Failed to fetch user profile";
        }
      } catch (error) {
        console.error("Error fetching user data:", error);
        error.value = "Error fetching user data";
      }
    };

    return {
      phone,
      password,
      error,
      getToken,
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
