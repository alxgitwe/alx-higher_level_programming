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
    const fs = require('fs');
    fs.writeFile(process.argv[3], body, (err) => {
      if (err) {
        console.log(err);
      }
    });
  }
});
