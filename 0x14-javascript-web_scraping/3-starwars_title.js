#!/usr/bin/node
/* A script that displays the status code of a GET request */
const request = require('request');
const id = process.argv[2];
const apiUrl = `https://swapi-api.hbtn.io/api/films/${id}`;

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
