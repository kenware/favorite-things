import Vue from 'vue';
import Paginate from 'vuejs-paginate';
import VModal from 'vue-js-modal';
import Vue2Filters from 'vue2-filters';
import VueFilterDateFormat from 'vue-filter-date-format';
// css
import 'materialize-css';
import 'materialize-css/dist/css/materialize.css';
import 'vue-select/dist/vue-select.css';
// local imports
import App from './App.vue';
import router from './router';
import store from './store/store';
import './registerServiceWorker';
import { requestSetup, responseSetup } from './interceptors';
import monthConfig from './config/months';

responseSetup();
requestSetup();

Vue.use(VueFilterDateFormat, monthConfig);
Vue.component('paginate', Paginate);
Vue.use(VModal);
Vue.use(Vue2Filters);
Vue.config.productionTip = false;

new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app');
