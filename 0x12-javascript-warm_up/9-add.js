#!/usr/bin/node

const arg1 = parseInt(process.argv[2]);
const arg2 = parseInt(process.argv[3]);

function add (a, b) {
  const sum = a + b;
  console.log(sum);
}

if (isNaN(arg1) || isNaN(arg2)) {
  console.log('Invalid argument');
} else {
  add(arg1, arg2);
}
