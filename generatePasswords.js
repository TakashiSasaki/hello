const bcrypt = require('bcrypt');
const fs = require('fs');

// ハッシュ化するユーザー名とパスワードのリスト
const users = {
  admin: 'adminpassword',
  user1: 'password123',
  user2: 'mypassword'
};

const hashedUsers = {};

// パスワードをハッシュ化し、結果をオブジェクトに保存
for (const [username, password] of Object.entries(users)) {
  const hashedPassword = bcrypt.hashSync(password, 10);
  hashedUsers[username] = hashedPassword;
}

// ハッシュ化されたユーザー名とパスワードをファイルに保存
fs.writeFileSync('passwords.json', JSON.stringify(hashedUsers, null, 2));
console.log('Passwords have been hashed and saved to passwords.json');
