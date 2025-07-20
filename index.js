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


app.get('/v1/apis/test', async (req, res) => {
    try {
        API_KEY = ''
        const headers = {
            'Accept':'application/json','x-api-key': API_KEY
        };
        const response = await fetch('https://api.manyapis.com/v1-get-short-url',
        {
        method: 'GET',
        headers: headers
        })
        .then(function(res) {
            return res.json();
        }).then(function(body) {
            console.log(body);
        });

    }
    catch(e) {
        console.error(e)
        logger.error('Error occurred while fetching API', { error: e.message, stack: e.stack });
    }
})


app.listen(5000, () => {
    logger.info('Server is running on port 5000');
});