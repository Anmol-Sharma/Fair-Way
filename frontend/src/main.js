// import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

// Import global stylesheet
import './assets/styles/global.css';  // Adjust the path as necessary

// Bootstrap import
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap";

const app = createApp(App).use(router).mount('#app')
