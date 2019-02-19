#!/usr/bin/node
const request = require('request');
request(process.argv[2], 'utf-8', function (error, response, body) {
  if (error) {
    throw (error);
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
