#!/usr/bin/node
const argv = require('process').argv;
if (!argv[2] || isNaN(argv[2])) {
  console.log('Missing size');
} else {
  for (let i = 0; i < argv[2]; i++) {
    let square = '';
    for (let j = 0; j < argv[2]; j++) {
      square += 'X';
    }
    console.log(square);
  }
}
