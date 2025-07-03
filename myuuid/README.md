<!-- README.md -->
# myuuid

`myuuid` は、特定の名前空間UUIDと入力文字列に基づいて、決定的なUUIDバージョン5 (UUIDv5) を生成するためのシンプルな Python モジュールです。

「特定の入力に対して常に同じUUIDを生成したい」という場合に役立ちます。

## イントロダクション

UUIDv5 は、入力された名前（文字列）と固定の名前空間UUIDから、SHA-1ハッシュ関数を使って決定的にUUIDを生成します。これにより、同じ名前と名前空間からは常に同じUUIDが得られます。

このモジュールは、内部に持つ固定の名前空間UUIDを使用して、入力された文字列に対応するUUIDv5を生成する機能を提供します。

## インストール

このプロジェクトは Poetry を使用して依存関係を管理しています。まず Poetry がインストールされていることを確認してください。

1.  リポジトリをクローンまたはファイルをダウンロードします。
2.  プロジェクトのルートディレクトリ（`pyproject.toml` がある場所）で、以下のコマンドを実行します。

    ```bash
    poetry install
    ```

## 使い方

`myuuid.get_new_uuidv5` 関数に入力したい文字列を渡すだけで、対応する UUIDv5 を取得できます。

```python
from myuuid import get_new_uuidv5

# ユーザー名からUUIDを生成する場合など
user_name = "alice_smith"
user_uuid = get_new_uuidv5(user_name)

print(f"名前 '{user_name}' に対応するUUID: {user_uuid}")

# 同じ名前からは常に同じUUIDが生成されます
another_call_uuid = get_new_uuidv5("alice_smith")
print(f"再度同じ名前から生成したUUID: {another_call_uuid}")

# 異なる名前からは異なるUUIDが生成されます
another_user_name = "bob_johnson"
another_user_uuid = get_new_uuidv5(another_user_name)
print(f"名前 '{another_user_name}' に対応するUUID: {another_user_uuid}")
````

## 内部で使用されている名前空間UUID

このモジュールは内部で以下の固定された名前空間UUIDを使用しています。

```python
# myuuid/__init__.py より
MY_NAMESPACE_UUID = uuid.UUID('c8ee7542-57d0-4fb3-880a-739391e7c131')
```

## テスト

Poetry の開発環境内でテストを実行できます。

```bash
poetry run pytest
```

## ライセンス

[必要に応じてライセンス情報を追加 - 例: MIT]

## 貢献

[必要に応じて貢献方法などを追加]

```

**補足:**

* 「[必要に応じて...]」と書かれた箇所は、必要であれば追記・修正してください。
* README は通常 Markdown という形式で記述します。GitHub などでプロジェクトを公開する場合にきれいに表示されます。

