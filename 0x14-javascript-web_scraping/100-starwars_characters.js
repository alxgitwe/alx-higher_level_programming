#!/usr/bin/node
const request = require('request');

// Function to fetch characters from a given movie ID
const fetchStarWarsCharacters = (movieId) => {
    const movieUrl = `https://swapi.dev/api/films/${movieId}/`;

    request(movieUrl, (error, response, body) => {
        if (error) {
            console.error('Error fetching movie data:', error);
            return;
        }

        const movieData = JSON.parse(body);
        const characterUrls = movieData.characters;

        characterUrls.forEach((characterUrl) => {
            request(characterUrl, (err, res, charBody) => {
                if (err) {
                    console.error('Error fetching character data:', err);
                } else {
                    const characterData = JSON.parse(charBody);
                    console.log(characterData.name);
                }
            });
        });
    });
};

// Main execution
const main = () => {
    const movieId = process.argv[2];

    if (!movieId) {
        console.error('Usage: ./100-starwars_characters.js <movie_id>');
        process.exit(1);
    }

    fetchStarWarsCharacters(movieId);
};

// Run the main function
main();
