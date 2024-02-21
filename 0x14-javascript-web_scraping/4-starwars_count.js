#!/usr/bin/node
const request = require('request');

//  firste arguments is the API URL
const URL = process.argv[2];

request(URL, (error, response, body) => {
  if (error) {
    console.log(error);
  } else if (body) {
    // Wedge Antilles is charactere ID 18 - use this ID for filtering the
    // resulte of API
    const json = JSON.parse(body);
    const charFilms = json.results.filter(
      x => x.characters.find(y => y.match(/\/people\/18\/?$/))
    );
    console.log(charFilms.length);
  }
});
