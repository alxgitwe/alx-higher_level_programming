#!/usr/bin/env node

const fs = require('fs').promises;

// Function to read and log file content
const readFileContent = async (filePath) => {
    try {
        const data = await fs.readFile(filePath, 'utf-8');
        console.log(data);
    } catch (error) {
        console.error('Error:', error);
    }
};

// Main execution
const main = () => {
    const filePath = process.argv[2];

    if (!filePath) {
        console.error('Usage: ./0-readme.js <file_path>');
        process.exit(1);
    }

    readFileContent(filePath);
};

// Run the main function
main();
