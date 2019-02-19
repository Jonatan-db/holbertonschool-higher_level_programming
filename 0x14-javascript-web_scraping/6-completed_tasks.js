#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let data = JSON.parse(body);
    let dict = {};

    for (let i = 0; i < data.length; i++) {
      let user = data[i];

      if (dict[user.userId] === undefined) {
        dict[user.userId] = 0;
      }
      if (user.completed === true) {
        dict[user.userId]++;
      }
    }
    console.log(dict);
  }
});
// for each works here
// https://appdividend.com/2018/09/12/javascript-foreach-example/
