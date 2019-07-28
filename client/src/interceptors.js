import axios from 'axios';
import store from './store/store';

export const requestSetup = () => {
  axios.interceptors.request.use((config) => {
    // document.body.classList.add('loading-indicator');
    store.dispatch('category/toggleSpinner', true);
    return config;
  }, (error) => {
    store.dispatch('category/toggleSpinner', false);
    return Promise.reject(error);
  });
};

export const responseSetup = () => {
  axios.interceptors.response.use((response) => {
    // document.body.classList.remove('loading-indicator');
    store.dispatch('category/toggleSpinner', false);
    return response;
  }, (error) => {
    store.dispatch('category/toggleSpinner', false);
    return Promise.reject(error);
  });
};
