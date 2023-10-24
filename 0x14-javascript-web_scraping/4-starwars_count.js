#!/usr/bin/node
const request = require('request');
const argument = process.argv;
const url = argument[2];
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let i = 0;
    let count = 0;
    while (i < JSON.parse(body).count) {
      const characters = JSON.parse(body).results[i].characters;
      for (let character = 0; character < characters.length; character++) {
        if (characters[character] === 'https://swapi-api.alx-tools.com/api/people/18/') {
          count += 1;
        }
      }
      i += 1;
    }
    console.log(count);
  }
});
