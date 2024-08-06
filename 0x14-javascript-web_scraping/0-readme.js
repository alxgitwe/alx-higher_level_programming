#!/usr/bin/env node

const fs = require('fs');

// Function to read and display file content
const displayFileContent = (filePath) => {
    fs.readFile(filePath, 'utf8', (error, content) => {
        if (error) {
            console.error('Error reading file:', error);
        } else {
            console.log(content);
        }
    });
};

// Check if a file path argument is provided
if (process.argv.length < 3) {
    console.error('Usage: ./0-readme.js <file_path>');
    process.exit(1);
}

// Call the function with the provided file path
displayFileContent(process.argv[2]);
