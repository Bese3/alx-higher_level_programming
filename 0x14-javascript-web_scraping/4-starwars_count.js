#!/usr/bin/node
const request = require('request');
// const argument = process.argv/
const url = 'https://swapi-api.alx-tools.com/api/people/18/';
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).films.length);
  }
});
