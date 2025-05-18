const https = require('https');
const fs = require('fs');
const path = require('path');

const url = 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/trainers/brock.png';
const outputPath = path.join(__dirname, '..', 'public', 'favicon.ico');

https.get(url, (response) => {
  const fileStream = fs.createWriteStream(outputPath);
  response.pipe(fileStream);

  fileStream.on('finish', () => {
    fileStream.close();
    console.log('Favicon downloaded successfully');
  });
}).on('error', (err) => {
  console.error('Error downloading favicon:', err.message);
}); 