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
    let x;
    const y = JSON.parse(body);
    const i = {};
    for (x = 0; x < y.length; x++) {
      if (y[x].completed === true) {
        if (i[y[x].userId]) {
          i[y[x].userId] += 1;
        } else {
          i[y[x].userId] = 1;
        }
      }
    }
    console.log(i);
  }
});
