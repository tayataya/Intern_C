# セットアップ

WebAppを動かすためにデータベースの設定が必要です。
データベースはMySQLもしくはMariaDBを想定しています。

```SQL
CREATE DATABASE jse_intern
CREATE USER 'jseintern' identified by 'jseintern+'
GRANT ALL PREVILEGES ON jse_intern.* to jseintern