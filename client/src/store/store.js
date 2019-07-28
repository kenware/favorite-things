import Vue from 'vue';
import Vuex from 'vuex';
import category from './category';
import favorite from './favorite';

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    category,
    favorite,
  },
});
