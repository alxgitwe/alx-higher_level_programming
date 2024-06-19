#!/usr/bin/node

const firstArg = process.argv[2];
const numericValue = Number(firstArg);

if (isNaN(numericValue)) {
  console.log("Missing number of occurrences");
} else {
  for (let i = 0; i < numericValue; i++) {
    console.log("C is fun");
  }
}
