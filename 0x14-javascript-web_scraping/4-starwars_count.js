#!/usr/bin/node
const request = require('request');
// const { json } = require('stream/consumers');
const argument = process.argv;
const url = argument[2];
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let count = 0;
    const results = JSON.parse(body).results;
    results.forEach((i) => {
      if (i.characters.indexOf('https://swapi-api.alx-tools.com/api/people/18/') !== -1) {
        count += 1;
      }
    });
    console.log(count);
  }
});
