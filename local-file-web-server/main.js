const fastify = require('fastify')();
const bcrypt = require('bcrypt');
const fs = require('fs');
const path = require('path');
const fastifyCookie = require('@fastify/cookie');
const fastifySession = require('@fastify/session');
const fastifyAuth = require('@fastify/auth');
const basicAuth = require('@fastify/basic-auth');
const FileStore = require('./filestore');
const MemoryStore = require('./memorystore');

// ハッシュ化されたパスワードを読み込み
const hashedPasswords = JSON.parse(fs.readFileSync('passwords.json'));

let store;
const filePath = path.join(__dirname, 'sessions.json');
try {
  fs.accessSync(filePath, fs.constants.W_OK);
  store = new FileStore();
} catch (err) {
  console.error(`File access error: ${err.message}. Using MemoryStore instead.`);
  store = new MemoryStore();
}

// プラグインの登録順序を修正
fastify.register(fastifyCookie);
fastify.register(fastifySession, {
  store: store,
  secret: process.env.SESSION_SECRET || 'a_secret_with_at_least_32_characters',
  cookie: { secure: process.env.NODE_ENV === 'production' },
  saveUninitialized: false,
});

// fastify-authプラグインの登録
fastify.register(fastifyAuth);

// 認証関数の定義
async function validate(username, password, req, reply) {
  if (hashedPasswords[username] && await bcrypt.compare(password, hashedPasswords[username])) {
    return;
  }
  throw new Error('Invalid credentials');
}

// @fastify/basic-authの登録
fastify.register(basicAuth, { validate });

// 認証を必要とするルート
fastify.after(() => {
  fastify.addHook('preHandler', fastify.auth([fastify.basicAuth]));

  fastify.route({
    method: 'GET',
    url: '/protected',
    onRequest: fastify.auth([fastify.basicAuth]),
    handler: async (request, reply) => {
      request.session.authenticated = true;
      return { message: '認証されたルートにアクセスしました' };
    }
  });
});

// 認証不要のステータス確認用ルート
fastify.route({
  method: 'GET',
  url: '/status',
  handler: async (request, reply) => {
    return { status: 'サーバーは動作中です' };
  }
});

// ログアウトルート
fastify.route({
  method: 'GET',
  url: '/logout',
  handler: async (request, reply) => {
    request.destroySession(err => {
      if (err) {
        return reply.status(500).send({ error: 'ログアウトに失敗しました' });
      }
      reply.send({ message: 'ログアウトしました' });
    });
  }
});

// サーバーの起動
fastify.listen({ port: 80, host: '127.1.2.3' }, err => {
  if (err) {
    console.error(err);
    process.exit(1);
  }
  console.log('サーバーが127.1.2.3:80で起動しました。');
});
