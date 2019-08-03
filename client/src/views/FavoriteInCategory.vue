<template>
  <div class='dashboard'>
   <div class="favorite-container">
     <div class="row favorite-wrapper">
       <div class="col s12 m4">
         <h5>Analytics</h5>
         <div class="analytic">
            <div class="title center">
              {{category.favoriteInCategoryCount}}
              <i class="material-icons color">favorite</i>
              {{ category.name | capitalize }}
            </div>
            <p class="content center">
                <router-link :to="{ name: 'createFavorite', query: { categoryId: category.id }}">
                    Add favorite
                </router-link>
            </p>
         </div>
       </div>
       <div class="col s12 m8">
         <div class="row favorite-search">
             <div class="col s6"><h5 class="favorite-label">My Favorites</h5></div>
            <form class="col s6">
                <div class="row">
                    <div class="input-field col s11">
                    <i class="material-icons prefix">search</i>
                    <input id="icon_prefix"
                      type="text"
                      class="validate"
                      name="search"
                      v-model="search"/>
                    <label htmlFor="icon_prefix">Search</label>
                    </div>
                </div>
            </form>
         </div>
        <FavoriteTable :favorites="favorites.results" :deleteFavorite="deleteFavorite"/>
      <div v-if="favorites.results.length" class="section center">
        <div class="divider" />
          <paginate
            :page-count="Math.ceil(favorites.count/this.limit)"
            :margin-pages="3"
            :click-handler="handlePage"
            :prev-text="'Prev'"
            :next-text="'Next'"
            :container-class="'pagination'"
            :page-class="'page-item'">
          </paginate>
      </div>
       </div>
     </div>
   </div>
  </div>
</template>

<script>

import { mapState } from 'vuex';
import FavoriteTable from '@/components/FavoriteTable.vue';
import Alert from '@/mixins/alert';
import FavoriteUrl from '@/mixins/favoriteUrls';

export default {
  name: 'FavoriteCategory',
  data: () => ({
    search: '',
    delayTimer: '',
    limit: 7,
    id: null,
  }),
  components: {
    FavoriteTable,
  },
  mixins: [Alert, FavoriteUrl],
  methods: {
    handlePage(num) {
      const { limit } = this;
      const offset = (num - 1) * limit;
      const url = this.favoriteLimit(limit, this.id, offset);
      this.$store.dispatch('favorite/get', { key: 'favorites', url });
    },
    async deleteFavorite(id, name) {
      const url = this.favoriteDetail(id); // `favorite/${id}`;
      const categoryUrl = `category/${this.id}/`;
      const favoriteUrl = this.favoriteLimit(this.limit, this.id);
      await this.$store.dispatch('favorite/delete', { key: 'favorite', url });
      await this.$store.dispatch('category/get', { key: 'category', url: categoryUrl });
      await this.$store.dispatch('favorite/get', { key: 'favorites', url: favoriteUrl });
      this.Alert('Favorite Deleted', 'success', { m: `You have deleted ${name}` }, 3000);
    },
  },
  watch: {
    search(value) {
      this.isSearch = true;
      clearTimeout(this.delayTimer);
      this.delayTimer = setTimeout(() => {
        const url = this.favoriteSearch(this.limit, this.id, value);
        this.$store.dispatch('favorite/get', { key: 'favorites', url });
      }, 700); // Will do the api call after 1000 ms
    },
  },
  async created() {
    const { id } = this.$route.params;
    this.id = id;
    const url = `category/${id}/`;
    const favoriteUrl = this.favoriteLimit(this.limit, id);
    console.log(this.favoriteLimit(this.limit, id));
    this.$store.dispatch('category/get', { key: 'category', url });
    this.$store.dispatch('favorite/get', { key: 'favorites', url: favoriteUrl });
  },
  computed: {
    ...mapState({
      category: state => state.category.category,
      favorites: state => state.favorite.favorites,
    }),
  },
};
</script>

<style lang="scss" scoped>
body {
  background-color: #F6F9FC;
}
.material-icons {
   font-size: 20px !important;
}
.dashboard {
  background-color: #F6F9FC;
  height: 100vh;
  .value-align {
      min-height: 165px !important;
  }

}

.favorite-container {
    width: 90%;
    margin-left: auto;
    margin-right: auto;
    .favorite-wrapper {
      padding-top: 5rem;
    }
    .analytic {
    box-shadow: 0 0.125rem 0.5625rem 0 rgba(0, 0, 0, 0.05);
    border-radius: 0.25rem;
    background-color: white;
    min-height: 150px;
    width: 80%;
    .title {
        padding-top: 20px;
        font-size: 1.9rem;
        font-weight: 500;
    }
    .content {
        margin-top: 50px;
        padding-bottom: 20px;
        font-size: 1.5rem;
        font-weight: 500;
    }
    }
    .favorite-search {
       margin-bottom: 1px !important;
    }
    .favorite-label {
        margin-top: 3rem !important;
    }
}
.color {
  color: #42b983;
}
a {
  color: #42b983;
  cursor: pointer;
}
</style>
