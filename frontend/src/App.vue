<template>
  <div id="app">

    <component :is="layout">
      <router-view />
    </component>

  </div>
</template>
  
<script>
import BasicLayout from "./layouts/BasicLayout.vue";
import axios from 'axios';
export default {
  name: 'App',
  components: {
    'basic-layout': BasicLayout
  },
  computed: {
    layout() {
      return this.$route.meta.layout || "default-layout" 
    },
  },
  setup() {
    axios.defaults.baseURL = 'http://localhost:8000';
  },
}
</script>
  
<style>
  #app-app {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
  }
</style>
  