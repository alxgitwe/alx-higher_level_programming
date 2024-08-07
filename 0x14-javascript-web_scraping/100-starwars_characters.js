#!/usr/bin/node
const rqst = require('request');
const x = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
rqst.get(x, function (error, response, body) {
  if (error) console.log(error);
  else {
    for (let y = 0; y < JSON.parse(body).characters.length; y++) {
      rqst.get(JSON.parse(body).characters[y], function (error2, response2, body2) {
        console.log(JSON.parse(body2).name);
      });
    }
  }
});
