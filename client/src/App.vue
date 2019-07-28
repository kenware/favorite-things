<template>
  <div id="app">
    <header>
      <Nav />
    </header>
    <main>
      <Spinner />
      <CategoryModal />
      <router-view/>
    </main>
    <footer></footer>
  </div>
</template>

<script>
import materializeInit from '@/mixins/materializeInit';
import Nav from '@/components/Nav.vue';
import Spinner from '@/components/Spinner.vue';
import CategoryModal from '@/components/modals/category.vue';

export default {
  name: 'App',
  components: {
    Nav,
    Spinner,
    CategoryModal,
  },
  mounted() {
    this.init();
  },
  mixins: [materializeInit],
};
</script>

<style lang="scss">
body {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}
.pagination li.active {
    background-color: #42b983 !important;
}
// .vs__dropdown-toggle {
//     border: 0px !important;
// }
.vs__search {
    // border: 0px !important;
    border-bottom: 0px !important;
}
.vs__clear {
  height: 0px !important;
}
</style>
