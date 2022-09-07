#!/usr/bin/node
/* A class Rectangle that defines a rectangle */
module.exports = class Rectangle {
  constructor (w, h) {
    if (w < 0 || h < 0 || !Math.sign(w) || !Math.sign(h)) { } else {
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

  rotate () {
    const tempWidth = this.width;
    const tempHeight = this.height;
    this.width = tempHeight;
    this.height = tempWidth;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
};
