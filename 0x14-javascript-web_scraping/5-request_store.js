#!/usr/bin/node
// Gets the contents of a webpage and stores it in a file.

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filename = process.argv[3];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(filename, body, { flag: 'wx', encoding: 'utf8' }, function (err) {
      if (err) {
        console.log(err);
      }
    });
  }
});
