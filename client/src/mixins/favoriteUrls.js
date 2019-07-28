
export default {
  methods: {
    favoriteList() {
      return 'favorite/';
    },
    favoriteDetail(id) {
      return `favorite/${id}/`;
    },
    favoriteLimit(limit, category, offset = null) {
      if (offset) {
        return `favorite/?categoryId=${category}&limit=${limit}&offset=${offset}`;
      }
      return `favorite/?categoryId=${category}&limit=${limit}`;
    },
    favoriteSearch(limit, category, search, offset) {
      return `${this.favoriteLimit(limit, category, offset)}&search=${search}`;
    },
  },
};
