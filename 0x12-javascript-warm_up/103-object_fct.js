#!/usr/bin/node

const myObject = {
  type: 'object',
  value: 12,
  incr: function () {
    this.value++;
  }
};

console.log(myObject);

myObject.incr();
myObject.incr();
myObject.incr();

console.log(myObject);
