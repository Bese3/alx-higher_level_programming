#!/usr/bin/node
const argv = require('process').argv;
if (!argv[2] || argv.length === 3) {
  console.log('0');
} else {
  const num = [];
  for (let i = 2; i < argv.length; i++) {
    num.push(parseInt(argv[i]));
  }
  num.sort((a, b) => a - b);
  console.log(num[num.length - 2]);
}
