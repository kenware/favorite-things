<template>
  <div class='favorite'>
    <router-link  class="right back-link"
        :to="{ name: 'favorite', params: { id: favorite.category }}">
          <i class="material-icons waves-effect small-icon">navigate_before</i> back
    </router-link>
    <div class="favorite-detail">
    <div class="detail-wrapper">
        <div class="row">
            <div class="col s12 m5 ">
               <img class="responsive-img section-img" src="/img/f1.png">
           </div>
           <div class="col s12 m7 ">
              <div class="section">
                  <div class="breadcrumbs hide-on-small-only show-on-medium-and-up">
                    <router-link to="/">Home</router-link>
                    &nbsp; / &nbsp;
                    {{ favorite.title | capitalize }}
                  </div>
                  <div>
                      <h5>{{ favorite.title | capitalize }} &nbsp;
                          <router-link :to="{ name: 'editFavorite', params: { id: this.id }}">
                             <i class="material-icons waves-effect">edit</i>
                          </router-link></h5>
                  </div>
                  <div>
                      <p>
                           {{ favorite.description | capitalize }}
                      </p>
                  </div>
                  <div>
                      <h6>Ranking</h6>
                      Ranked <span class="chip">
                        {{favorite.ranking}}
                        </span> out of total rank of <span class="chip">
                            {{ favorite.maxRanking}}
                        </span>
                  </div>
                  <div>
                      <h6>Attributes</h6>
                      <ul>
                          <li v-for="(value, key, index) in favorite.metadata" :key="index">
                              {{ key | capitalize }}: &nbsp; {{ value | capitalize }}
                          </li>
                      </ul>
                  </div>
              </div>
           </div>
        </div>
      </div><br>
      <div class="history-wrapper" v-if="favorite.auditLog.length">
          <div class="row">
              <div class="col s2"></div>
              <div class="col s8">
                 <h5>Audit History</h5><br>
                 <div class="history-section">
                     <div class="history-data"
                       v-for="(log, index) in favorite.auditLog" :key="log.date">
                        <h6>{{ index + 1 }}
                            &nbsp;&nbsp;&nbsp;
                            {{new Date(log.date) | dateFormat('MMM DD, YYYY') }}</h6>
                        <div class="divider"/>
                        <ul>
                            <li v-for="message in log.message" :key="message"> {{ message }}</li>
                        </ul>
                     </div>
                 </div>
              </div>
              <div class="col s2"></div>
          </div>

      </div>
    </div>
  </div>
</template>

<script>

import { mapState } from 'vuex';
import FavoriteUrl from '@/mixins/favoriteUrls';

export default {
  name: 'FavoriteCategory',
  data: () => ({
    id: 0,
  }),
  mixins: [FavoriteUrl],
  methods: {
  },

  created() {
    const { id } = this.$route.params;
    this.id = id;
    const url = `favorite/${id}`;
    this.$store.dispatch('favorite/get', { key: 'favorite', url });
  },
  computed: {
    ...mapState({
      favorite: state => state.favorite.favorite,
    }),
  },
};
</script>

<style lang="scss" scoped>
.favorite {
    background-color: #f5f5f5;
    min-height: 100vmin;
    .favorite-detail {
        padding-top: 4rem;
       .detail-wrapper {
            margin-left: 2%;
            margin-right: 2%;
            background-color: white;
            min-height: 70vmin;
            .section {
                font-size: 17px;
                padding: 3rem;
                .color {
                color: #42b983;
                }
                a {
                color: #42b983;
                cursor: pointer;
                }
                h6, h5 {
                   font-weight: 500;
                }
            }
            .section-img{
              min-height: 70vmin
            }
        }
        .history-wrapper {
            margin-left: 2%;
            margin-right: 2%;
            background-color: #fafafa;
            min-height: 40vmin;
            .history-section {
                font-size: 16px;
                width: 100%;
                background-color: white;
                min-height: 20vmin;
                .history-data {
                   padding: 0.7rem 1rem 0rem 1rem;
                   ul {
                       li {
                           margin-left: 1.8rem;
                       }
                   }
                }
            }
        }
    }
    .back-link {
        margin-right: 2%;
        padding-top: 1.5rem;
        font-size: 1.5rem;
        }
}

</style>
