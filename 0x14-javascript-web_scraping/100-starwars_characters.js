#!/usr/bin/node
const request = require('request');
const argument = process.argv;

const url = 'https://swapi-api.alx-tools.com/api/films/' + argument[2];
request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const chars = JSON.parse(body).characters;
    // console.log(chars);
    for (let i = 0; i < chars.length; i++) {
      request(chars[i], (error, response, body) => {
        if (error) {
          console.log(error);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
