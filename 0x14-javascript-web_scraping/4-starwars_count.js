#!/usr/bin/node

const request = require('request');
const fake = "http://swapi.co/api/films/";
const fake2 = process.argv[2];
const url = 'http://swapi.co/api/' + 'people/18';
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const val = JSON.parse(body);
    console.log(val.films.length);
  }
});
