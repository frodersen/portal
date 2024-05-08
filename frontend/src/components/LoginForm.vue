<template>
  <div class="login-box">
    <div v-if="isLoading">
      <p>Loading...</p>
    </div>

    <div v-else-if="!isAuthenticated">
      <form @submit.prevent="login">
        <div class="input-group">
          <select v-model="countryCode" class="country-code">
            <option v-bind:value="'no'">Norge (+47)</option>
            <option
              v-for="country in countries"
              :key="country.iso2"
              v-bind:value="country.iso2"
            >
              {{ country.name }} (+{{ country.dialCode }})
            </option>
          </select>
          <input
            v-model="phone"
            id="phone"
            type="tel"
            class="phone-number"
            placeholder="Telefonnummer"
          />
        </div>
        <div class="input-group">
          <input
            v-model="password"
            id="password"
            type="password"
            class="password-input"
            placeholder="Passord"
          />
        </div>

        <div v-show="isError" class="error-message">
          {{ error }}
        </div>

        <button type="submit" class="login-button">LOGG INN</button>

        <div class="links-wrapper">
          <div class="link">
            <a href="#">Forgot Password</a>
          </div>
          <div class="link">
            <a href="#">Activate user</a>
          </div>
        </div>
      </form>
    </div>

    <div v-else class="auth-message">
      <p>
        Du er nå autentisert hos NTNUI! Nå kan du besøke andre tjenester til
        NTNUI uten å logge inn!
      </p>
      <button @click="logout" class="logout-button">Logg Ut</button>
    </div>
  </div>
</template>

<script>
import { ref, watch, onMounted } from "vue";
import axios from "axios";
import CountryCodes from "@/assets/CountryCodes.json";

export default {
  setup() {
    const selectedCountryCode = ref("no");
    const countries = ref(CountryCodes);
    const phone = ref("");
    const password = ref("");
    const error = ref("");
    const isError = ref(false);
    const isAuthenticated = ref(false);
    const isLoading = ref(true);

    const getDialCode = (isoCode) => {
      const country = countries.value.find((c) => c.iso2 === isoCode);
      return country ? `+${country.dialCode}` : "";
    };

    const dialCode = ref(getDialCode(selectedCountryCode.value));

    watch(selectedCountryCode, (newIsoCode) => {
      dialCode.value = getDialCode(newIsoCode);
    });

    const login = async () => {
      if (!phone.value.trim() || !password.value.trim()) {
        error.value = "Både telefonnummer og passord må fylles inn.";
        isError.value = true;
        setTimeout(() => (isError.value = false), 5000);
        return;
      }

      const fullPhoneNumber = `${dialCode.value}${phone.value}`;
      try {
        const response = await axios({
          method: "post",
          url: "http://localhost:8000/login/",
          data: {
            phone_number: fullPhoneNumber,
            password: password.value,
          },
          withCredentials: true,
          validateStatus: (status) => status < 500,
        });

        if (response.status === 401) {
          error.value = "Feil telefonnummer eller passord";
          isError.value = true;
          setTimeout(() => (isError.value = false), 5000);
          return;
        }

        const redirectUrl = getQueryParam("redirect_url");
        if (redirectUrl) {
          window.location.href = decodeURIComponent(redirectUrl);
        } else {
          isAuthenticated.value = true;
        }
      } catch (err) {
        error.value = "Server error or network issue";
        isError.value = true;
        setTimeout(() => (isError.value = false), 5000);
        console.error("Login error:", err);
      } finally {
        isLoading.value = false;
      }
    };

    const logout = async () => {
      try {
        const response = await axios({
          method: "post",
          url: "http://localhost:8000/logout/",
          withCredentials: true,
          validateStatus: (status) => status < 500,
        });

        if (response.status === 200) {
          isAuthenticated.value = false;
        } else {
          console.error("Logout failed with status:", response.status);
        }
      } catch (err) {
        console.error("Logout failed:", err);
      } finally {
        isLoading.value = false;
      }
    };

    function getQueryParam(param) {
      const urlParams = new URLSearchParams(window.location.search);
      return urlParams.get(param);
    }

    const checkAuthenticationStatus = async () => {
      try {
        const response = await axios({
          method: "post",
          url: "http://localhost:8000/verify/",
          withCredentials: true,
          validateStatus: (status) => status < 500,
        });

        if (response.status === 200) {
          isAuthenticated.value = true;
        }
      } catch (err) {
        console.error("Error:", err);
      } finally {
        isLoading.value = false;
      }
    };

    onMounted(checkAuthenticationStatus);

    return {
      countryCode: selectedCountryCode,
      countries,
      phone,
      password,
      error,
      isError,
      login,
      isAuthenticated,
      logout,
      isLoading,
    };
  },
};
</script>

<style scoped>
.login-box {
  background-color: transparent;
  padding: 40px;
  border-radius: 10px;
  width: 300px;
  max-width: 100%;
  color: #2c3e50;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.login-box h1 {
  text-align: center;
  margin-bottom: 30px;
  color: #000;
  font-size: 15px;
}

.login-box label {
  display: block;
  margin-bottom: 5px;
  color: #000;
  font-weight: bold;
}

.login-box select,
.login-box input[type="tel"],
.login-box input[type="password"] {
  width: 100%;
  padding: 15px;
  margin-bottom: 15px;
  border-radius: 5px;
  border: 1px solid #d3d3d3;
  background: #f7f7f7;
  color: #333;
}

.login-box select {
  -webkit-appearance: none;
  -moz-appearance: none;
  appearance: none;
  background-image: url('data:image/svg+xml;utf8,<svg fill="#333" height="24" viewBox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg"><path d="M7 10l5 5 5-5z"/></svg>');
  background-repeat: no-repeat;
  background-position: right 10px center;
}

.login-box button[type="submit"],
.logout-button {
  background-color: #007bff;
  color: #fff;
  padding: 15px;
  margin-top: 10px;
  border: none;
  border-radius: 5px;
  width: 100%;
  cursor: pointer;
  font-size: 16px;
  font-weight: bold;
  transition: background-color 0.3s;
}

.login-box p,
.auth-message p {
  text-align: center;
  margin-top: 20px;
}

.login-box p a {
  color: #007bff;
  text-decoration: none;
}

.login-box p a:hover {
  text-decoration: underline;
}

.links-wrapper,
.error-message {
  text-align: center;
  margin-top: 20px;
}

.error-message {
  color: #ff0000;
  max-width: 300px;
  word-wrap: break-word;
}

.auth-message {
  padding: 20px;
  background-color: #f4f4f4;
  border-radius: 5px;
  color: #2c3e50;
  width: 100%;
  box-sizing: border-box;
}

.input-group {
  width: 100%;
  display: flex;
  justify-content: space-between;
  margin-bottom: 15px;
}

.country-code,
.phone-number {
  flex: 1;
}

.country-code {
  margin-right: 10px;
}

.phone-number {
  margin-left: 10px;
}

.link {
  padding: 5px 15px;
  border: 2px solid #d3d3d3;
  border-radius: 10px;
  margin-right: 5px;
}

.link a {
  color: #d3d3d3;
}

.link a:hover {
  text-decoration: underline;
}
</style>
