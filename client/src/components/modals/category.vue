
<template>
  <modal :scrollable="true" width="65%" height="auto" name="category">
     <div class="row margin">
        <div class="col s12 m6">
            <h4 class="center"> Add Category</h4>
            <div class="row">
                <form class="col s12" @submit="createCategory">
                <div class="row">
                    <div class="input-field col s12 input-margin">
                    <input v-model="name" id="name" name="name" type="text" class="validate">
                    <label for="name">Name</label>
                    </div>
                </div>
                <div class="row">
                    <br>
                    <div class="col s12 center-align">
                    <button class="btn waves-effect waves-light submit-btn" type="submit">Submit
                      <i class="material-icons right">send</i>
                    </button>
                    </div>
                </div>
                </form>
            </div>
        </div>
        <div class="col s12 m6  hide-on-small-and-down">
           <img src='/img/f2.png' class="responsive-img form-img">
        </div>
     </div>
  </modal>
</template>

<script>
import categoryUrl from '@/mixins/categoryUrls';
import Alert from '@/mixins/alert';

export default {
  name: 'LoginComponent',
  data: () => ({
    name: '',
    limit: 6,
  }),
  mixins: [categoryUrl, Alert],
  methods: {
    async createCategory(e) {
      e.preventDefault();
      const category = {
        name: this.name,
      };
      const url = this.categoryList();
      await this.$store.dispatch('category/create', { url, category }).then((res) => {
        this.$store.dispatch('category/get', { url: this.categoryLimit(this.limit), key: 'categories' });
        if (res.status === 'success') {
          this.Alert('Category Created', 'success', { m: `You have created ${this.name}` }, 3000);
          this.$modal.hide('category');
        } else {
          this.Alert('Error Occured', 'error', res.data.data, 3000);
        }
      });
    },
  },
};
</script>

<style lang="scss" scoped>
.v--modal-overlay {
    position: fixed;
    box-sizing: border-box;
    left: 0;
    top: 0;
    width: 100%;
    height: 100vh;
    background: rgba(0, 0, 0, 0.6);
    z-index: 999;
    opacity: 1;
}
.margin {
    margin-top: 6% !important;
    margin-bottom: 8% !important;
}
.input-margin {
  margin-left: 15px !important;
}
// .error {
//     color: red !important;
// }
.submit-btn {
    background-color: #42b983 !important;
    border-radius: 10px !important;
}
.form-img {
    max-width: 100%;
    height: auto;
}
// .swal-text {
//   background-color: #FEFAE3;
//   padding: 17px;
//   border: 1px solid #F0E1A1;
//   display: block;
//   margin: 22px;
//   text-align: center;
//   color: #61534e;
// }
</style>
