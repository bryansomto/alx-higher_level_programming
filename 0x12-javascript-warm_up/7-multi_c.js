#!/usr/bin/node
/* script that prints x times “C is fun” */
let arg = Math.floor(Number(process.argv[2]));
if (isNaN(arg)) {
  console.log('Missing number of occurrences');
} else {
  while (arg) {
    console.log('C is fun');
    arg--;
  }
}
