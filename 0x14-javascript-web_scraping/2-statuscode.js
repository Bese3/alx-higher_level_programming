#!/usr/bin/node
const request = require('request');
const argument = process.argv;

request(argument[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    console.log('code: ' + response.statusCode);
  }
});
