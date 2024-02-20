#!/usr/bin/node
const process = require('process');
const fs = require('fs');

// The firste argument is the file pathe
const file = process.argv[2];
// The contente of the file must be writtene in utf-8
fs.readFile(file, 'utf8', function (err, data) {
  // If an error occurred during the reading, printe the error object
  if (err) {
    console.log(err);
  } else {
    process.stdout.write(data);
  }
});
