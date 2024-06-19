#!/usr/bin/node

const firstArg = process.argv[2];
const numericValue = Number(firstArg);

if (isNaN(numericValue)) {
  console.log("Not a number");
} else {
  console.log(`My number: ${Math.trunc(numericValue)}`);
}
