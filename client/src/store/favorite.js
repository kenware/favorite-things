import axios from 'axios';
import baseUrl from '../config/host';

export default {
  namespaced: true,
  state: {
    favorites: { results: [] },
    favorite: { auditLog: [], category: 0 },
    errors: {
      favorite: '',
    },
  },
  mutations: {
    updateState(state, favoriteObject) {
      state[favoriteObject.key] = favoriteObject.data;
    },
    updateError(state, errorObject) {
      state.errors[errorObject.key] = errorObject.data;
    },
  },
  actions: {
    async create({ commit }, data) {
      try {
        const response = await axios.post(`${baseUrl}/${data.url}`, data.favorite);
        commit('updateState', { key: 'favorite', data: response.data });
        return { status: 'success', data: response.data };
      } catch (error) {
        commit('updateError', { key: 'favorite', data: error.response });
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
    async patch({ commit }, data) {
      try {
        const response = await axios.patch(`${baseUrl}/${data.url}`, data.favorite);
        commit('updateState', { key: 'favorite', data: response.data });
        return { status: 'success', data: response.data };
      } catch (error) {
        commit('updateError', { key: 'favorite', data: error.response });
        return { status: 'error', data: error.response };
      }
    },
    async delete({ commit }, data) {
      try {
        const response = await axios.delete(`${baseUrl}/${data.url}`, data.favorite);
        commit('updateState', { key: 'favorite', data: response.data });
        return { status: 'success', data: response.data };
      } catch (error) {
        commit('updateError', { key: 'favorite', data: error.response });
        return { status: 'error', data: error.response };
      }
    },
  },
};
