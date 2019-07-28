<template>
    <div class="vld-parent">
        <loading
        :active.sync="isLoading"
        :is-full-page="fullPage"></loading>
    </div>
</template>
<script>
// Import component
import Loading from 'vue-loading-overlay';
import { mapState } from 'vuex';
// Import stylesheet
import 'vue-loading-overlay/dist/vue-loading.css';

export default {
  computed: {
    ...mapState({
      isLoading: state => state.category.spinner,
    }),
  },
  data: () => ({
    fullPage: true,
  }),
  components: {
    Loading,
  },
};
</script>
