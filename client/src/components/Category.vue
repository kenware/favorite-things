
<template>
  <div class="category-wrapper">
    <br>
    <h4 class="center">My Favorite Categories</h4>
    <p class="center">
        Manage or keep track of all your favorite things or
        create a new category to add you favorite things<br>
        <a href="#" @click="modalShow" rel="noopener">Create new category</a>
        <a @click="modalShow" class="btn-floating btn-small cyan pulse">
          <i class="material-icons">navigate_next</i>
        </a>
    </p>
    <br>
    <div class="row">
        <div class="col s6 m4"
            v-for="category in categories.results" :key="category.id">
            <div class="analytic">
                <div class="title">
                   <router-link
                      :to="{name: 'favorite',
                       params: { things: category.name, id: category.id } }"
                    >
                    {{ category.name | capitalize }}
                  </router-link>
                </div>
                <p class="content">
                  <router-link :to="{name: 'favorite', params: { id: category.id } }">
                    {{category.favoriteInCategoryCount}}
                    <i class="material-icons">favorite</i>
                    {{ category.name | capitalize }}
                  </router-link>
                </p>
            </div>
        </div>
  </div>
  <div class="section center">
    <div class="divider" />
      <paginate
      :page-count="Math.ceil(categories.count/this.limit)"
      :margin-pages="3"
      :click-handler="handlePage"
      :prev-text="'Prev'"
      :next-text="'Next'"
      :container-class="'pagination'"
      :page-class="'page-item'">
    </paginate>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex';
import categoryUrl from '@/mixins/categoryUrls';

export default {
  name: 'Category',
  mixins: [categoryUrl],
  async created() {
    const url = this.categoryLimit(this.limit);
    this.$store.dispatch('category/get', { key: 'categories', url });
  },
  computed: {
    ...mapState({
      categories: state => state.category.categories,
    }),
  },
  methods: {
    handlePage(pageNum) {
      const { limit } = this;
      const offset = (pageNum - 1) * limit;
      const url = this.categoryLimit(this.limit, offset);
      this.$store.dispatch('category/get', { key: 'categories', url });
    },
    modalShow() {
      this.$modal.show('category');
    },
  },
  data: () => ({
    limit: 6,
  }),
};
</script>

<style lang="scss" scoped>
 .category-wrapper {
    margin-left: 2%;
    margin-right: 2%;
 a {
    color: #42b983;
 }
 .pulse {
  background-color: #42b983 !important;
}
 .analytic {
    box-shadow: 0 0.125rem 0.5625rem 0 rgba(0, 0, 0, 0.05);
    border-radius: 0.25rem;
    background-color: white;
    min-height: 150px;
    width: 80%;
    .title {
        font-size: 1.5rem;
        padding-top: 20px;
        margin-left: 30px;
        a {
           color: #2c3e50;
        }
    }
    .content {
        margin-top: 50px;
        font-size: 1.2rem;
        font-weight: 500;
        text-align: right;
        margin-right: 20px;
        color: #42b983;
    }
    .material-icons {
       font-size: inherit;
    }
  }
}
</style>
