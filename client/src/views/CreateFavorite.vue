
<template>
 <div class="create-favorite">
  <div class="new-favorite-wrapper">
     <div class="row">
        <h5>
          {{ editMode? 'Edit My Favorite': 'Create New Favorite' }}
          <router-link  class="right" :to="{ name: 'favorite', params: { id: data.category }}">
             <i class="material-icons waves-effect small-icon">navigate_before</i> back
          </router-link>
        </h5>
    <form class="col s12 form-class">
      <div class="row">
        <div class="input-field col s6">
          <input
            v-model="data.title"
            name="title"
            placeholder="Placeholder"
            id="title"
            type="text" class="validate">
          <label class="active-label" for="first_name">Title</label>
           <span v-if="isSubmit" class="red-text">{{data.title ? '': '*Field required'}}</span>
        </div>
        <div class="input-field col s6">
          <input v-model="data.ranking" id="ranking" type="number" min="1" class="validate">
          <label class="active-label" for="ranking">Ranking</label>
           <span v-if="isSubmit" class="red-text">{{data.ranking ? '': '*Field required'}}</span>
        </div>
      </div>
      <div class="row">
      <div class="input-field col s12">
          <textarea v-model="data.description" id="textarea1" class="materialize-textarea">
          </textarea>
          <label class="active-label" for="textarea1">Description</label>
          <span>Length: {{data.description.length}}</span>&nbsp;&nbsp;
          <span v-if="isSubmit" class="red-text">
            {{validateDescription ? '': 'The lenght of description must be greater than ten if specified'}}
          </span>
      </div>
      </div>
      <div class="row">
        <div class="input-field col s6">
          <div>
          <label class="typo__label">Single select / dropdown</label>
          <multiselect
              v-model="data.category"
              tagPosition="bottom"
              track-by="id"
              :custom-label="opt => {
                const option = categories.results.find(x => x.id == opt)
                return name = option ? option.name : ''
                }"
              placeholder="Select one"
              :options="categories.results.map(category => category.id)">
          </multiselect>
        </div>
        </div>
      </div>
      <div class="row">
        <h6 class="attribute-header">Attributes In {{ data.title | capitalize}}</h6>
        <div class="col s10">
            <div v-for="(data, index) in attributes" class="row" :key="index">
                <div class="input-field col s12 m5">
                    <input v-model="attributes[index].key" id="key" type="text" class="validate">
                    <label class="active-label" for="email">Key</label>
                    <span v-if="isSubmit" class="red-text">
                      {{data.key ? '': '*Field required'}}
                    </span>
                </div>
                <div class="input-field col s12 m5">
                    <input v-model="attributes[index].value" id="value"
                      type="text"
                      class="validate">
                    <label class="active-label" for="value">Value</label>
                    <span v-if="isSubmit" class="red-text">
                      {{data.value ? '': '*Field required'}}
                    </span>
                </div>
                <div class="input-field col s12 m2">
                    <i @click="deleteAttribute(index)"
                      class="material-icons waves-effect color-delete">
                        delete
                    </i>
                </div>
            </div>
        </div>
        <div class="col s2">
           <a @click="addAttribute" class="waves-effect btn favorite-btn right">
               <i class="material-icons color-delete">add</i>
               Add New {{favorite.title}}
            </a>
        </div>
      </div>
      <div class="col s12 center">
        <button @click="submit"
          class="btn submit waves-effect waves-light"
          type="submit"
          name="action">
            Submit
           <i class="material-icons right">send</i>
        </button>
       </div>
    </form>
  </div>
  </div>
  </div>
</template>

<script>
import { mapState } from 'vuex';
import Multiselect from 'vue-multiselect';
import Alert from '@/mixins/alert';
import FavoriteUrl from '@/mixins/favoriteUrls';

export default {
  name: 'NewFavorite',
  components: {
    Multiselect,
  },
  mixins: [Alert, FavoriteUrl],
  async created() {
    const { categoryId } = this.$route.query;
    const { id } = this.$route.params;
    // url
    const categoryUrl = 'category/';
    const favoriteUrl = `favorite/${id}/`;

    if (id) {
      const favoriteData = await this.$store.dispatch('favorite/get', { key: 'favorite', url: favoriteUrl });
      if (favoriteData.status === 'success') {
        this.editMode = true;
        this.data = favoriteData.data;
        this.formatAttributes(favoriteData.data);
      }
    }
    if (categoryId) {
      this.data.category = categoryId;
    }
    this.$store.dispatch('category/get', { key: 'categories', url: categoryUrl });
  },
  computed: {
    ...mapState({
      categories: state => state.category.categories,
      favorite: state => state.favorite.favorite,
    }),
    validateDescription() {
      if (this.data.description && this.data.description.length < 10) {
        return false;
      }
      return true;
    },
  },
  methods: {
    addAttribute() {
      this.attributes.push({ key: '', value: '' });
    },
    deleteAttribute(index) {
      this.attributes.splice(index, 1);
    },
    prepareAttributes() {
      const metaData = {};
      for (const attribute of this.attributes) {
        if (attribute.key && attribute.value) {
          metaData[attribute.key] = attribute.value;
        } else {
          return false;
        }
      }
      return metaData;
    },
    async submit(e) {
      e.preventDefault();
      this.isSubmit = true;
      const {
        category, title, description, ranking,
      } = this.data;
      if (this.prepareAttributes() && title && this.validateDescription && category && ranking) {
        const favorite = {
          category,
          title,
          ranking,
          description,
          metadata: this.prepareAttributes(),
        };

        const url = 'favorite/';
        let res;
        const { id } = this.$route.params;

        if (this.editMode && id) {
          res = await this.$store.dispatch('favorite/patch', { url: `${url}${id}/`, favorite });
        } else {
          res = await this.$store.dispatch('favorite/create', { url, favorite });
        }

        if (res.status === 'success') {
          const message = this.editMode ? `You have update ${this.data.title}` : `You have created ${this.data.title}`;
          const titleMessage = this.editMode ? 'Updated' : 'Created';
          this.Alert(titleMessage, 'success', { message }, 3000);
        } else {
          this.Alert('Error Occured', 'error', res.data.data, 4000);
        }
      }
    },
    formatAttributes(data) {
      const attributes = [];
      Object.entries(data.metadata).forEach((array) => {
        const obj = {};
        [obj.key, obj.value] = array;
        attributes.push(obj);
      });
      this.attributes = attributes;
    },
  },
  data: () => ({
    data: {
      value: 1,
      title: '',
      description: '',
      ranking: '',
      category: '',
    },
    editMode: false,
    attributes: [
      {
        key: '',
        value: '',
      },
    ],
    isSubmit: false,
  }),
};
</script>

<style src="vue-multiselect/dist/vue-multiselect.min.css"></style>
<style lang="scss" scoped>
.create-favorite {
    background-color: #fafafa;
    min-height: 100vh;
   .new-favorite-wrapper {
      margin: 0% 15% 1% 15%;
      padding-top: 10px;
   }
   .form-class {
    box-shadow: 0 0.025rem 0.5625rem 0 rgb(250, 250, 250);
    background-color: white;
    padding: 30px !important;
   }
    .active-label {
    transform: translateY(-14px) scale(0.8);
    transform-origin: 0 0;
     font-size: 19px !important;
  }
  label {
    font-size: 17px !important;
  }
  .attribute-header {
    margin-left: 1rem;
    font-size: 21px !important;
  }
  .favorite-btn {
    background-color: white;
    color: black;
    margin-top: 2rem;
  }
  .submit {
    background-color: #42b983;
  }
  .small-icon {
    font-size: 2rem;
  }
  a {
    color: #26a69a;
  }
}
</style>
