
export default {
  methods: {
    categoryList() {
      return 'category/';
    },
    categoryDetail(id) {
      return `category/${id}/`;
    },
    categoryLimit(limit, offset = null) {
      if (offset) {
        return `category/?limit=${limit}&offset=${offset}`;
      }
      return `category/?limit=${limit}`;
    },
  },
};
