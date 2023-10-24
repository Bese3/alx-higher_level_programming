#!/usr/bin/node
const fs = require('fs');
const argument = process.argv;

fs.writeFile(argument[2], argument[3], 'utf-8', (error) => {
  if (error) {
    console.log(error);
  }
});
