#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || arguments.length < 2) {

    } else {
      this.width = w;
      this.height = h;
    }
  }
};
