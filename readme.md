# readme

## DBの設定

WebAppを動かすためにデータベースの設定が必要です。
データベースはMySQLもしくはMariaDBを想定しています。
```SQL
CREATE DATABASE jse_intern;
CREATE USER 'jseintern' identified by 'jseintern+';
GRANT ALL PRIVILEGES ON jse_intern.* TO jseintern;
```