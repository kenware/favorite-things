
<template>
  <div>
    <nav class="nav">
      <div class="nav-wrapper nav-fixed-bar-in white">
        <router-link class="brand-logo" to="/">
           <img class="logo-img" src="/img/fav3.png">
        </router-link>
        <a href="#" data-target="mobile-demo" class="sidenav-trigger">
        <i class="material-icons">menu</i></a>
        <ul class="right hide-on-med-and-down">
          <li><a href="#" @click="modalShow">Add category</a></li>&nbsp;&nbsp;&nbsp;
        </ul>
      </div>
    </nav>
    <ul class="sidenav" id="mobile-demo">
      <li><a href="#" @click="modalShow">Add category</a></li>
    </ul>
  </div>
</template>

<script>

export default {
  name: 'Nav',
  methods: {
    modalShow() {
      this.$modal.show('category');
    },
  },
};
</script>

<style lang="scss" scoped>
.white-c {
  background-color: transparent !important;
}
.nav {
    .logo-img {
      height: 65px;
      width: 110px;
    }
    .brand-logo {
      margin-left: 30px;
    }
    height: 87px !important;
    .nav-wrapper {
      height: inherit;
      a {
        margin-top: 15px !important;
        font-weight: bold;
        color: #2c3e50;
        &.router-link-exact-active {
          color: #42b983;
        }
      }
    }
  }
.nav-fixed-bar-in {
    position: fixed;
    right: 0;
    left: 0;
    top: 0;
    color: white;
    margin-bottom: 0px;
    z-index: 997;
  }
</style>
