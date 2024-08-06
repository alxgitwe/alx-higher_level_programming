#!/usr/bin/node
const rqst = require('request');

const opts = {
  url: process.argv[2],
  method: 'GET'
};
rqst(opts, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    let c = 0;
    let x;
    let y;
    const json = JSON.parse(body);
    for (x = 0; x < json.results.length; x++) {
      for (y = 0; y < json.results[x].characters.length; y++) {
        if (json.results[x].characters[y].includes('18')) {
          c++;
        }
      }
    }
    console.log(c);
  }
});
