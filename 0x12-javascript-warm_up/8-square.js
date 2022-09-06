#!/usr/bin/node
/* script that prints a asquare */
let arg = parseInt(process.argv[2]);
if (isNaN(arg)) {
	console.log('Missing size');
} else {
	for (i = 0; i < arg; i++) {
		let row = '';
		for (j = 0; j < arg; j++) {
			row += 'X';
		}
		console.log(row);
	}
}
