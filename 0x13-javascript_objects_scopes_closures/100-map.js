#!/usr/bin/node
const myArray = require('./100-data').list;
const doubleArray = [];
for (let i = 0; i < myArray.length; i++) {
  doubleArray.push(myArray[i] * i);
}
console.log(myArray);
console.log(doubleArray);
