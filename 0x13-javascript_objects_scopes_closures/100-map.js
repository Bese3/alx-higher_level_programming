#!/usr/bin/node
const myArray = require('./100-data').list;
const doubleArray = myArray.map((element, index) => element * index);

console.log(myArray);
console.log(doubleArray);
