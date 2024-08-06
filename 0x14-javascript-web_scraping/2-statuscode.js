#!/usr/bin/env node

const request = require('request');

const requestOptions = {
    url: process.argv[2],
    method: 'GET'
};

request(requestOptions, (error, response, responseBody) => {
    if (error) {
        console.error('Error:', error);
    } else {
        console.log('Status Code:', response.statusCode);
        console.log('Response Body:', responseBody);
    }
});
