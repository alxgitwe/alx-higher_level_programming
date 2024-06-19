#!/usr/bin/node

function secondBiggest() {
  if (process.argv.length === 1) {
    console.log(0);
  } else if (process.argv.length === 2) {
    console.log(0);
  } else {
    const numbers = process.argv.slice(2).map(Number);
    numbers.sort((a, b) => b - a);
    if (numbers.length > 1) {
      console.log(numbers[1]);
    } else {
      console.log(0);
    }
  }
}

secondBiggest();
