// pouchdb_example.js

// Import the PouchDB library
const PouchDB = require('pouchdb');

// Create a new PouchDB instance
const db = new PouchDB('my_database');

// Define a simple document
const doc = {
    _id: 'example_doc',
    title: 'Sample Document',
    content: 'This is a sample document stored in PouchDB.'
};

// Function to add or update a document in the database
async function addOrUpdateDocument() {
    console.log('Document to be added or updated:', doc);
    try {
        const existingDoc = await db.get(doc._id);
        doc._rev = existingDoc._rev; // Set the revision ID for updating
        const result = await db.put(doc);
        console.log('Document updated:', result);
    } catch (error) {
        if (error.status === 404) {
            try {
                const result = await db.put(doc);
                console.log('Document added:', result);
            } catch (addError) {
                console.error('Error adding document:', addError);
            }
        } else {
            console.error('Error adding or updating document:', error);
        }
    }
}

// Function to retrieve a document from the database
async function getDocument() {
    try {
        const retrievedDoc = await db.get('example_doc');
        console.log('Retrieved document:', retrievedDoc);
    } catch (error) {
        console.error('Error retrieving document:', error);
    }
}

// Close the PouchDB instance
async function closeDatabase() {
    try {
        await db.close();
        console.log('Database closed successfully.');
    } catch (error) {
        console.error('Error closing the database:', error);
    }
}

// Main function to run the operations
async function main() {
    await addOrUpdateDocument();
    await getDocument();
    await closeDatabase();  // Close the database at the end
}

// Execute the main function
main();
