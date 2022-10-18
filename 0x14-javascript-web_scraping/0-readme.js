#!/usr/bin/node
/* A script that reads and prints the content of a file. */
const fs = require('fs');
const arg = process.argv[2];
fs.readFile(arg, 'utf-8', function (error, content) {
  if (error) {
    console.log(error);
  } else {
    console.log(content);
  }
});
