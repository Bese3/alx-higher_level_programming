#!/usr/bin/node

const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === '' || c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let myStr = '';
      for (let j = 0; j < this.width; j++) {
        myStr += c;
      }
      console.log(myStr);
    }
  }
};
