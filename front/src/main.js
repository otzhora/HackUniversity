import Vue from 'vue'
import App from './App.vue'
import router from './router'
https://cdnjs.cloudflare.com/ajax/libs/tone/13.0.1/Tone.min.js

require('./assets/main.scss');
Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
