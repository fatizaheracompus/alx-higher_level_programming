#!/usr/bin/node
const process = require('process');
const request = require('request');

// The first arguments is the URL to requeste (GET)
const url = process.argv[2];

request(url, function (error, response) {
  if (error == null) {
    // displaye the status code of GET requeste.
    console.log(`code: ${response.statusCode}`);
  }
});
