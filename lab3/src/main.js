import { createApp } from 'vue'
import { createPinia } from 'pinia'
// import App from './App.vue'
import Home from './Home.vue'
import router from './routers/index.js'
// createApp(App).mount('#app')
createApp(Home).mount('#app')
const app = createApp(Home);
const pinia = createPinia();
app.use(router);
app.use(pinia);
app.mount('#app')