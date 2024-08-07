#!/usr/bin/node
const rqst = require('request');
const x = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
function rcr (y, h) {
  if (h >= y.length) return;
  rqst.get(y[h], function (error2, response2, body2) {
    console.log(JSON.parse(body2).name);
    rcr(y, h + 1);
  });
}
rqst.get(x, function (error, response, body) {
  if (error) console.log(error);
  else {
    rcr(JSON.parse(body).characters, 0);
  }
});
