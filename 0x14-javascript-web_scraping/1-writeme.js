#!/usr/bin/node
const ffs = require('fs');

ffs.writeFile(process.argv[2], process.argv[3], (err) => {
  if (err) {
    console.log(err);
  }
});
