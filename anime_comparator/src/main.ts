import '../public/assets/main.css'

import { createApp } from 'vue'
import PrimeVue from 'primevue/config';
import App from './App.vue'
import router from './router'

import Image from "primevue/image";
import Dropdown from "primevue/dropdown";
import Knob from "primevue/knob";
import Button from "primevue/button";
import InputText from "primevue/inputtext";

const app = createApp(App)

app.use(router)
app.use(PrimeVue);
app.component("pv-image", Image)
app.component("pv-dropdown", Dropdown)
app.component("pv-knob", Knob)
app.component("pv-button", Button)
app.component("pv-input", InputText)
app.mount('#app')
