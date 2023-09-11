#!/usr/bin/node
const argv = require('process').argv;
if (!argv[2] || argv.length === 3) {
  console.log('0');
} else {
  let biggest = 0;
  for (let i = 0; i < argv.length; i++) {
    if (argv[i] > biggest) {
      biggest = i;
    }
  }
  argv[biggest] = 0;
  for (let i = 0; i < argv.length; i++) {
    if (argv[i] > biggest) {
      biggest = argv[i];
    }
  }
  console.log(biggest);
}
