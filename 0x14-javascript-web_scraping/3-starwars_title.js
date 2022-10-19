#!/usr/bin/node
/* A script that displays the status code of a GET request */
const request = require('request');
const id = process.argv[2];
const api_url = `https://swapi-api.hbtn.io/api/films/${id}`;

request(api_url, function (error, response, body)
{
  console.log(JSON.parse(body).title);
});
