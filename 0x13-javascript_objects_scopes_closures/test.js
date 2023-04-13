#!/usr/bin/node
const Rectangle = require('./4-rectangle.js');
const r1 = new Rectangle(2, 4);
r1.rotate();
console.log(r1.print());
r1.double();
console.log(r1.print());
