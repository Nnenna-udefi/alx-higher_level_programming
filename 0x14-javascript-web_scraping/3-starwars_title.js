#!/usr/bin/node
const request = require('request');
const episodeNum = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + episodeNum;

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const movie = JSON.parse(body).title;
    console.log(movie);
  }
});
