<template>
  <div id="app">
    <LoginPage />
  </div>
</template>

<script>
import LoginPage from "./views/LoginPage.vue";

export default {
  name: "App",
  components: {
    LoginPage,
  },
};
</script>

<style>
html,
body {
  padding: 0;
  margin: 0;
  height: 100%;
  width: 100%;
  overflow: hidden;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background-color: #1a202c;
  overflow: hidden;
  width: 100%;
  height: 100%;
}
</style>
