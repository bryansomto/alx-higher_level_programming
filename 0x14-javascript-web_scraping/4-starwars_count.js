#!/usr/bin/node
/* A script that prints the number of movies where the character “Wedge Antilles” is present. */
const request = require('request');
const apiUrl = process.argv[2];

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error(error);
  } else if (response.statusCode === 200) {
    const movies = JSON.parse(body).results;
    let count = 0;
    for (const movieIndex in movies) {
      const movieCharacters = movies[movieIndex].characters;
      for (const characterIndex in movieCharacters) {
        if (movieCharacters[characterIndex].includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  } else {
    console.log('An error occured. Status code: ' + response.statusCode);
  }
});
