<template>
  <div class="login-box">
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
</template>

<script>
import { ref, watch } from "vue";
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

    const getDialCode = (isoCode) => {
      const country = countries.value.find((c) => c.iso2 === isoCode);
      return country ? `+${country.dialCode}` : "";
    };

    const dialCode = ref(getDialCode(selectedCountryCode.value));

    watch(selectedCountryCode, (newIsoCode) => {
      dialCode.value = getDialCode(newIsoCode);
    });

    const login = async () => {
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

        if (response.status === 200) {
          const redirectUrl = getQueryParam("redirect_url");
          window.location.href = decodeURIComponent(redirectUrl);
        }
      } catch (err) {
        error.value = "Server error or network issue";
        isError.value = true;
        setTimeout(() => (isError.value = false), 5000);
        console.error("Login error:", err);
      }
    };

    function getQueryParam(param) {
      const urlParams = new URLSearchParams(window.location.search);
      return urlParams.get(param);
    }

    return {
      countryCode: selectedCountryCode,
      countries,
      phone,
      password,
      error,
      isError,
      login,
    };
  },
};
</script>

<style scoped>
.login-box {
  width: 300px;
}
.login-box {
  background-color: transparent;
  padding: 40px;
  border-radius: 10px;
  width: auto;
  color: #2c3e50;
  display: flex;
  flex-direction: column;
  align-items: flex-end;
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
  width: 93%;
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
  background-image: url('data:image/svg+xml;utf8,<svg fill="#333" height="24" viewBox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg"><path d="M7 10l5 5 5-5z"/></svg>'); /* Add custom arrow */
  background-repeat: no-repeat;
  background-position-x: 95%;
  background-position-y: 50%;
}

.login-box button[type="submit"] {
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

.login-box p {
  text-align: center;
  margin-top: 20px;
}

.login-box p a {
  color: #007bff;
  text-decoration: none;
  margin: 0 5px;
}

.login-box p a:hover {
  text-decoration: underline;
}

.login-box .links {
  text-align: center;
  margin-top: 20px;
}

.error-message {
  color: #ff0000;
  text-align: center;
}
.input-group {
  width: 300px;
  display: flex;
  justify-content: space-between;
  margin-bottom: 15px;
}

.country-code {
  flex: 1;
  margin-right: 5px;
  font-size: x-small;
}

.phone-number {
  flex: 3;
}

.links-wrapper {
  display: flex;
  justify-content: space-evenly;
  align-items: center;
  margin-top: 20px;
}

.link {
  padding: 5px 15px;
  border: #d3d3d3 solid 2px;
  margin-right: 5px;
  border-radius: 10px;
}

.link a {
  color: #d3d3d3;
  text-decoration: none;
}

.link a:hover {
  text-decoration: underline;
}

.error-message {
  color: #ff0000;
  text-align: center;
  margin-top: 10px;
}
</style>
