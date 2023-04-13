#!/usr/bin/node
const Square = require('./5-square.js');
module.exports = class Square extends Square {
  constructor (size) {
    super(size, size);
  }
  
  charPrint (c) {
    if (typeof c === 'undefined') {
      this.print();
    } else {
      let ww = 0;
      let ss = '';
      while (ww < this.width) {
        ss = ss + c;
        ww = ww + 1;
      }
      ww = 0;
      while (ww < this.height) {
        console.log(ss);
        ww = ww + 1;
      }
    }
};
