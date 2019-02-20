#!/usr/bin/node

const request = require('request');
const url = 'http://swapi.co/api/films/' + process.argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let data = JSON.parse(body).characters;

    for (let i = 0; i < data.length; i++) {
      request.get(data[i], function (error, response, body) {
        if (error) {
          throw error;
        }
        console.log(JSON.parse(body).name);
      });
    }
    // console.log(data['name']);

    // data.forEach(name => {
    // request.get(name, function(error, response, body) {
    // console.log(JSON.parse(body).name);
    // });
    // });
  }
});
