class MemoryStore {
    constructor() {
      this.sessions = {};
    }
  
    get(sid, callback) {
      callback(null, this.sessions[sid] || null);
    }
  
    set(sid, session, callback) {
      this.sessions[sid] = session;
      callback(null);
    }
  
    destroy(sid, callback) {
      delete this.sessions[sid];
      callback(null);
    }
  }
  
  module.exports = MemoryStore;
  