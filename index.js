const express = require('express');
const logger = require('./utils/logger');


const app = express();

app.get('/', (req, res) => {
    logger.info('Health check endpoint hit');
    res.send('OK');
})

app.get('/v1/apis' , (req, res) => {
    logger.info('API endpoint hit');
    res.json({'message': '/v1/api', 'version': '1.0.0', 'status': 'active'});
});


app.listen(5000, () => {
    logger.info('Server is running on port 5000');
});