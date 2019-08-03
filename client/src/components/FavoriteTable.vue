
<template>
    <table class="responsive-table striped highlight">
        <thead>
        <tr>
            <th>Title</th>
            <th>Description</th>
            <th>Ranking</th>
            <th>Created Date</th>
            <th>Modified Date</th>
            <th>Actions</th>
        </tr>
        </thead>

        <tbody>
        <tr v-for="favorite in favorites" :key="favorite.id">
            <td class="table-td" @click="onClick(favorite.id)">{{favorite.title}}</td>
            <td class="table-td" @click="onClick(favorite.id)">
              {{favorite.description | truncate(15) }}
            </td>
            <td class="table-td" @click="onClick(favorite.id)">
              {{favorite.ranking}}
            </td>
            <td class="table-td" @click="onClick(favorite.id)">
              {{ new Date(favorite.createdDate) | dateFormat('MMM DD, YYYY') }}
            </td>
            <td class="table-td" @click="onClick(favorite.id)">
              {{ new Date(favorite.modifiedDate) | dateFormat('MMM DD, YYYY') }}
            </td>
            <td class="action">
                <i
                  class="material-icons tooltipped color"
                  data-position="top"
                  data-tooltip="view">
                <router-link :to="{ name: 'favoriteDetail', params: { id: favorite.id }}">
                  visibility
                </router-link>
              </i>&nbsp;&nbsp;
              <i class="material-icons color">
                <router-link :to="{ name: 'editFavorite', params: { id: favorite.id }}">
                  edit
                </router-link>
              </i>&nbsp;&nbsp;
              <i @click="deleteFavorite(favorite.id, favorite.title)"
                class="material-icons waves-effect">
                  delete
              </i>
              </td>
        </tr>
        </tbody>
    </table>
</template>

<script>
import materializeInit from '@/mixins/materializeInit';

export default {
  name: 'FavoriteCategoryTable',
  props: {
    favorites: Array,
    deleteFavorite: Function,
  },
  mixins: [materializeInit],
  mounted() {
    this.init()
  },
  methods: {
    onClick(id) {
      this.$router.push(`/favorite/${id}/detail`);
    },
  },
};
</script>

<style lang="scss" scoped>
  a {
    color: #2c3e50 !important;
  }
  table {
    tbody {
      tr:hover {
        box-shadow: 0 0.125rem 0.5625rem 0 rgba(0, 0, 0, 0.05);
        background-color: rgba(0, 0, 0, 0.05) !important;
        .action {
          background-color: #F6F9FC !important;
          box-shadow: 0 0.001rem 0.0005rem 0 rgba(0, 0, 0, 0.01) !important;
        }
      }
      .table-td{
        cursor: pointer;
      }
    }
  }
  .waves-effect {
    vertical-align: top !important;
  }

</style>
