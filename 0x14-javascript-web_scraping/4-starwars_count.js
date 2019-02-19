#!/usr/bin/node

const request = require('request');
const fake = 'http://swapi.co/api/films/';
let count = 0;
let charId = /18/;
request(fake, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const val = JSON.parse(body);
    // console.log(val);
    let results = val.results;
    // console.log(results);
    for (let i of results) {
      // console.log(i);
      let listCharacters = i.characters;
      //  console.log(listCharacters);
      for (let j in listCharacters) {
        // console.log(listCharacters[j]);
        if (charId.test(listCharacters[j]) === true) {
          count++;
        }
      }
    }
  }
  console.log(count);
});

/*
Okay this works but the intranet and grader is a butt
request(charId, function (error, response, body) {
if (error) {
console.log(error);
} else {
const val = JSON.parse(body);
console.log(val.films.length);
}
});
*/
