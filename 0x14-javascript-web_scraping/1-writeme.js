#!/usr/bin/node
/* A script that writes a string to a file. */
const fs = require('fs');
const arg1 = process.argv[2];
const arg2 = process.argv[3];
fs.writeFile(arg1, arg2, 'utf-8', function (error) {
  if (error) {
    console.log(error);
  }
});
