#!/usr/bin/node
let array = [];
if (!isNaN(process.argv[3])) {
  for (let i = 2; i < process.argv.length; i++) {
    array[i - 2] = Number(process.argv[i]);
  }
  array.sort().reverse();
  console.log(array[1]);
} else {
  console.log(0);
}
