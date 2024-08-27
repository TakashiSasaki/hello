// leveldb_reader.js
// Set the environment variable LANG to English
process.env.LANG = 'en_US.UTF-8';

const level = require('level');

// Path to your LevelDB database
const dbPath = 'my_database';
const db = level(dbPath);

db.createReadStream()
  .on('data', function (data) {
    // Display the key in hex format
    const keyHex = Buffer.from(data.key).toString('hex');
    
    // Display the key in binary format
    const keyBinary = Buffer.from(data.key).toString('binary');
    
    console.log(`Key (hex): ${keyHex}`);
    console.log(`Key (binary): ${keyBinary}`);
    console.log('Value:', data.value);
  })
  .on('error', function (err) {
    console.error('Error reading LevelDB:', err);
  })
  .on('close', function () {
    console.log('Stream closed');
  })
  .on('end', function () {
    console.log('Stream ended');
  });
