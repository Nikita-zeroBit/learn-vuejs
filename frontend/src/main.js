import { createApp } from "vue";
import App from "./App.vue";

const app = createApp(App);

import router from "./router";
import axios from 'axios';
app.config.globalProperties.$axios = axios;

app.use(router);
// app.render(h => h(App))
app.mount('#app')
