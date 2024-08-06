#!/usr/bin/node
const rqst = require('request');

const optns = {
  url: process.argv[2],
  method: 'GET'
};
rqst(optns, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    console.log('code:', res.statusCode);
  }
});
