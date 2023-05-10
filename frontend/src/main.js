import { createApp } from "vue";
import { createPinia } from 'pinia';
import PrimeVue from 'primevue/config'
import Button from "primevue/button"
import Menubar from 'primevue/menubar'
import router from './router'
import InputText from 'primevue/inputtext';
import InputNumber from 'primevue/inputnumber';

import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import ColumnGroup from 'primevue/columngroup';   // optional
import Row from 'primevue/row';
import Card from 'primevue/card';

import TabView from 'primevue/tabview';
import TabPanel from 'primevue/tabpanel';

import Toast from 'primevue/toast';
import ToastService from 'primevue/toastservice';

import Message from 'primevue/message';

//theme
import "primevue/resources/themes/mdc-dark-indigo/theme.css"
//core
import "primevue/resources/primevue.min.css";
//icons
import "primeicons/primeicons.css";
import App from "./App.vue";

const app = createApp(App);

import axios from 'axios';

app.config.globalProperties.$axios = axios;

const pinia = createPinia()

app.use(PrimeVue)
app.use(router)
app.use(pinia)
app.use(ToastService)


app.component('Toast-prime', Toast)

app.component('TabView-prime', TabView)
app.component('TabPanel-prime', TabPanel)

app.component('Button-prime', Button)
app.component('Menubar-prime', Menubar)
app.component('InputText-prime', InputText)
app.component('InputNumber-prime', InputNumber)

app.component('DataTable-prime', DataTable)
app.component('Column-prime', Column)
app.component('ColumnGroup-prime', ColumnGroup)
app.component('Row-prime', Row)
app.component('Card-prime', Card)
app.component('Message-prime', Message)

app.mount('#app')
