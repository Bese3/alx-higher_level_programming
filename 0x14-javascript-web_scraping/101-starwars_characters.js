#!/usr/bin/node
const request = require('request');
const argument = process.argv;

const url = 'https://swapi-api.alx-tools.com/api/films/' + argument[2];
request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const chars = JSON.parse(body);
    // console.log(chars);
    chars.characters.forEach(ch => {
      request(ch, (error, response, body) => {
        if (error) {
          console.log(error);
        } else {
          const name = JSON.parse(body);
          console.log(name.name);
        }
      });
    });
  }
});
