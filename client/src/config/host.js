
const host = process.env.NODE_ENV === 'production' ? 'https://tshirtcollection-api.herokuapp.com/api/v1' : 'http://localhost:8000/api/v1';

export default host;
