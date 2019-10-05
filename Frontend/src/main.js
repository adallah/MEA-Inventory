import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import './registerServiceWorker'
import jQuery from 'jquery'
global.jQuery = global.$ = jQuery
import axios from 'axios'
import VueAxios from 'vue-axios'

Vue.config.productionTip = false

require('fastjs.shortcuts')
let Markdown = require('./assets/js/Markdown.Converter.js');
require('./assets/js/styleguide.js')
// require('./assets/js/jquery-scrollto.js')
require('./assets/js/clipboard.js')
require('./assets/js/featherlight.min.js')
require('./assets/js/selectTwo.js');





let materialize = require('materialize-css/dist/js/materialize')
Vue.use(VueAxios, axios)


import Vnav from './components/Vnav.vue'
Vue.component('v-nav', Vnav);

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
