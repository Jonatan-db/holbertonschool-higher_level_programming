#!/usr/bin/node
let gremlin = 1;
if (!isNaN(process.argv[2])) {
  for (let i = 1; i <= parseInt(process.argv[2]); i++) {
    gremlin *= i;
  }
}
console.log(gremlin);
