#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (Number.isInteger(w) && Number.isInteger(h) && w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let ww = 0;
    let ss = '';
    while (ww < this.width) {
      ss = ss + 'X';
      ww = ww + 1;
    }
    ww = 0;
    while (ww < this.height) {
      console.log(ss);
      ww = ww + 1;
    }
  }
};
