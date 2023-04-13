#!/usr/bin/node
const dict = require('./101-data.js').dict;
const list = [];
const newDict = {};

Object.keys(dict).foreach((key) => {
  if (!list.includes(dict[key])) {
    list.push(dict[key]);
    newDict[dict[key]] = [];
  }
});

Object.keys(dict).foreach((key) => {
  list.foreach((app) => {
    if (dict[key] === app) {
      newDict[dict[key]].push(key);
    }
  });
});
console.log(newDict);
