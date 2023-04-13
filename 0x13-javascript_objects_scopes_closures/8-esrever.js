#!/usr/bin/node
exports.esrever = function (list) {
  const reverse = [];
  let x = list.length - 1;
  while (x >= 0) {
    reverse.push(list[x]);
    x = x - 1;
  }
  return reverse;
};
