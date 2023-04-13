#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let x = 0;
  let count = 0;
  while (x < list.length) {
    if (searchElement === list[x]) {
      count = count + 1;
    }
    x = x + 1;
  }
  return count;
};
