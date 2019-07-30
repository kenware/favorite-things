
const host = process.env.NODE_ENV === 'production' ? 'http://ec2-34-221-201-174.us-west-2.compute.amazonaws.com/api/v1' : 'http://localhost:8000/api/v1';

export default host;
