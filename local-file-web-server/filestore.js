const fs = require('fs');
const path = require('path');

class FileStore {
  constructor(options = {}) {
    this.sessions = {};
    this.filePath = path.join(__dirname, 'sessions.json');
    this.loadSessions();
  }

  loadSessions() {
    if (fs.existsSync(this.filePath)) {
      const data = fs.readFileSync(this.filePath);
      this.sessions = JSON.parse(data);
    }
  }

  saveSessions() {
    fs.writeFileSync(this.filePath, JSON.stringify(this.sessions, null, 2));
  }

  get(sid, callback) {
    callback(null, this.sessions[sid] || null);
  }

  set(sid, session, callback) {
    this.sessions[sid] = session;
    this.saveSessions();
    callback(null);
  }

  destroy(sid, callback) {
    delete this.sessions[sid];
    this.saveSessions();
    callback(null);
  }
}

module.exports = FileStore;
