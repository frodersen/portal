<template>
  <div class="wrapper">
    <div class="logo-container">
      <img src="@/assets/ntnui.svg" class="img" alt="ntnui-logo" />
      <h1 class="title">PORTAL</h1>
    </div>
    <div key="login-form" class="formWrapper">
      <login-form />
    </div>
  </div>
</template>

<script>
import LoginForm from "@/components/LoginForm.vue";

export default {
  name: "LoginPage",
  components: {
    LoginForm,
  },
};
</script>

<style>
.wrapper {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: rem(0) rem(0);
  max-width: 40vw;
  top: 0; /* Align top to the top of the viewport */
  left: 0; /* Align left to the left of the viewport */
}

.title {
  display: flex;
  flex-direction: column;
  justify-content: center;
  margin: 0.3125rem 0; /* Converted from rem(5) */
  margin-bottom: 30px;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen,
    Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
  color: rgb(255, 255, 255);
}

.formWrapper {
  width: 340;
}

@media (max-width: 599px) {
  .formWrapper {
    width: 100%;
  }
}

.img {
  height: rem(10);
  width: 50%;
  justify-content: center;
}
</style>
