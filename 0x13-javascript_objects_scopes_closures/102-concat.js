#!/usr/bin/node
const fs = require('fs');
const contentA = fs.readFile(process.argv[2]);
const contentB = fs.readFile(process.argv[3]);
const contentC = Buffer.concat([contentA, contentB]);
fs.writeFile(process.argv[4], contentC);
