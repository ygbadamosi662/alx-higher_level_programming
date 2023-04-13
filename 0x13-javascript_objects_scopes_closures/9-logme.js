#!/usr/bin/node
let g = 0;
exports.logMe = function (item) {
  const show = g + ': ' + item;
  console.log(show);
  g = g + 1;
};
