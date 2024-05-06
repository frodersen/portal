<template>
  <div class="login-box">
    <form @submit.prevent="login">
      <!-- Country code and phone input container -->
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
      <!-- Password input container -->
      <div class="input-group">
        <input
          v-model="password"
          id="password"
          type="password"
          class="password-input"
          placeholder="Passord"
        />
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
import { ref, watch } from "vue"; // Ensure watch is imported
import axios from "axios";
import CountryCodes from "@/assets/CountryCodes.json";

export default {
  setup() {
    const selectedCountryCode = ref("no"); // Default value for the selected country code
    const countries = ref(CountryCodes); // Assuming CountryCodes is an array
    const phone = ref("");
    const password = ref("");
    const error = ref("");

    // Find the country object that matches the selectedCountryCode and return its dialCode
    const getDialCode = (isoCode) => {
      const country = countries.value.find((c) => c.iso2 === isoCode);
      return country ? `+${country.dialCode}` : "";
    };

    // Create a computed ref for the dial code
    const dialCode = ref(getDialCode(selectedCountryCode.value));

    // Watch for changes on the selectedCountryCode and update the dialCode accordingly
    watch(selectedCountryCode, (newIsoCode) => {
      dialCode.value = getDialCode(newIsoCode);
    });

    const login = async () => {
      // Concatenate the selected dial code with the phone number
      const fullPhoneNumber = `${dialCode.value}${phone.value}`;

      try {
        const response = await axios({
          method: "post",
          url: "http://localhost:8000/auth/login/",
          data: {
            phone_number: fullPhoneNumber,
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
      countryCode: "no",
      countries,
      selectedCountryCode,
      phone,
      password,
      error,
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
  border-radius: 10px; /* Slightly more rounded corners */
  width: auto; /* Increased width */
  color: #2c3e50; /* Darker text color */
  display: flex;
  flex-direction: column;
  align-items: flex-end; /* Align children to the right */
}

.login-box h1 {
  text-align: center;
  margin-bottom: 30px; /* More space below the heading */
  color: #000; /* Black color for the text */
  font-size: 15px; /* Larger font size */
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
  width: 93%;
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

.login-box .links {
  text-align: center;
  margin-top: 20px; /* Increased margin */
}

.error-message {
  color: #ff0000; /* Red color for error messages */
  text-align: center;
}
.input-group {
  width: 300px;
  display: flex;
  justify-content: space-between; /* Adjust as needed */
  margin-bottom: 15px; /* Increased margin */
}

.country-code {
  flex: 1;
  margin-right: 5px; /* Spacing between select and input */
  font-size: x-small;
}

.phone-number {
  flex: 3;
}

.links-wrapper {
  display: flex; /* Aligns children in a row */
  justify-content: space-evenly; /* Distributes space evenly around items */
  align-items: center; /* Aligns items vertically in the center */
  margin-top: 20px; /* Space above the link section */
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
</style>
