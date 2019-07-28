<template>
  <div class="home">
    <LandingPage />
    <div class="category">
       <Categories />
    </div>
  </div>
</template>

<script>
import { Component, Vue } from 'vue-property-decorator';
import LandingPage from '@/components/LandingPage'; // @ is an alias to /src
import Categories from '@/components/Category';

@Component({
  components: {
    LandingPage,
    Categories,
  },
})
export default class Home extends Vue {}
</script>

<style lang="scss" scoped>
  .category {
  background-color: #F6F9FC;
  height: 100vh;
  }
</style>
