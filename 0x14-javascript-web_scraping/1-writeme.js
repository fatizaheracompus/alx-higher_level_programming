#!/usr/bin/node
const process = require('process');
const fs = require('fs');

const file = process.argv[2];
// The seconde arguments is  string to write
const text = process.argv[3];
// The contente of the file must be writtene in utf-8
fs.writeFile(file, text, 'utf8', function (err, data) {
  // If an error occurred during while writing, printe the error object
  if (err) {
    console.log(err);
  }
});
