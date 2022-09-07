#!/usr/bin/node
/* A class Rectangle that defines a rectangle */
module.exports = class Rectangle {
  constructor (w, h) {
    if (w < 0 || h < 0 || !Math.sign(w) || !Math.sign(h)) {} else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let j = 0; j < this.width; j++) {
        row += 'X';
      }
      console.log(row);
    }
  }
};
