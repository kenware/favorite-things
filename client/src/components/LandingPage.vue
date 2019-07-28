<template>
<div>
<div class="parallax-container center valign-wrapper">
  <div class="container">
    <div class="row">
      <div class="col s12 white-text">
        <h2 class="teal-text-landing lighten-2">My Favorite Things</h2>
        <h4 class="">Track your favorite things with little effort.</h4>
        <h5 class="teal-text-landing lighten-2">
          Get Started by tracking your favorite places, person etc.
        </h5>
      </div>
    </div>
  </div>
  <div class="parallax">
    <img src="/img/landing2.jpeg">
  </div>
</div>
</div>
</template>

<script>
import materializeInit from '@/mixins/materializeInit';

export default {
  name: 'LandingPage',
  props: {
    msg: String,
  },
  mounted() {
    this.init();
  },
  mixins: [materializeInit],
};
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss" scoped>

.parallax-container {
  height: 89vh;
  img {
  max-height: 200%;
  }
  .teal-text-landing {
    color: #42b983 !important;
  }
  .teal-text-landing-bg {
    color: #42b983 !important;
  }
}

</style>
