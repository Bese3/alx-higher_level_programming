#!/usr/bin/node
const fs = require('fs');
const argument = process.argv;
fs.readFile(argument[2], 'utf-8', (error, data) => {
  if (error) {
    console.log(error);
  } else {
    console.log(data);
  }
});
