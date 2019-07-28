import axios from 'axios';
import baseUrl from '../config/host';

export default {
  namespaced: true,
  state: {
    categories: { results: [] },
    category: {},
    spinner: false,
    errors: {
      category: '',
    },
  },
  mutations: {
    updateState(state, categoryObject) {
      state[categoryObject.key] = categoryObject.data;
    },
    updateError(state, errorObject) {
      state.errors[errorObject.key] = errorObject.data;
    },
  },
  actions: {
    async create({ commit }, data) {
      try {
        const response = await axios.post(`${baseUrl}/${data.url}`, data.category);
        commit('updateState', { key: 'category', data: response.data });
        return { status: 'success', data: response.data };
      } catch (error) {
        commit('updateError', { key: 'category', data: error.response });
        return { status: 'error', data: error.response };
      }
    },
    async get({ commit }, data) {
      try {
        const response = await axios.get(`${baseUrl}/${data.url}`);
        commit('updateState', { key: data.key, data: response.data });
        return { status: 'success', data: response.data };
      } catch (error) {
        commit('updateError', { key: data.key, data: error.response });
        return { status: 'error', data: error.response };
      }
    },
    toggleSpinner({ commit }, data) {
      commit('updateState', { key: 'spinner', data });
    },
  },
};
