#!/usr/bin/node
// class Square that defines a square and inherits from Rectangle of 4-rectangle.js

const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  /**
   * charPrint - prints a rectangle of characters with a specified width and height, using
   * the character `c` as the fill.
   * @c: - The parameter `c` is a character that will be used to print a pattern. If no character
   * is provided, the default character 'X' will be used.
   */
  charPrint (c) {
    if (c === undefined) {
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
