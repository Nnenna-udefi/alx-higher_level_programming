#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const films = JSON.parse(body).results;
    const wedgeMovies = films.filter((film) =>
      film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/'));
    console.log(wedgeMovies.length);
  }
});
