# OpenDHT Proxy Scripts

このリポジトリには、OpenDHT プロキシサーバーと通信するためのいくつかの Python スクリプトが含まれています。

## スクリプト一覧

1. `fetch_node_info.py`
2. `fetch_node_stats.py`
3. `fetch_value.py`
4. `insert_value.py`

## 使い方

### 前提条件

- Python 3.6 以降がインストールされていること。
- `requests` ライブラリがインストールされていること。インストールされていない場合は以下のコマンドでインストールできます。

  ```sh
  pip install requests
  ```

### `fetch_node_info.py`

このスクリプトは、OpenDHT ノードの情報を取得して表示します。

```sh
python fetch_node_info.py
```

### `fetch_node_stats.py`

このスクリプトは、OpenDHT ノードの統計情報を取得して表示します。

```sh
python fetch_node_stats.py
```

### `fetch_value.py`

このスクリプトは、OpenDHT システムから特定のキーに関連する値を取得して表示します。

#### 使用法

```sh
python fetch_value.py <key>
```

#### 例

```sh
python fetch_value.py example
```

### `insert_value.py`

このスクリプトは、OpenDHT システムに値を挿入します。

#### 使用法

```sh
python insert_value.py <key> <value>
```

#### 例

```sh
python insert_value.py example hehehe
```

## 注意事項

- これらのスクリプトは、デフォルトで `http://opendht.moukaeritai.work:4223` エンドポイントを使用しています。
- エンドポイントが変更された場合は、スクリプト内の URL を適宜変更してください。
