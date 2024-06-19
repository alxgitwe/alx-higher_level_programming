#!/usr/bin/node

function add(a, b) {
  return a + b;
}

const firstArg = Number(process.argv[2]);
const secondArg = Number(process.argv[3]);

console.log(add(firstArg, secondArg));
