# Database (データベース)
- data を保管する場所
- data の量や種類が多い場合は database (DB) を用いて管理する
- ほぼ全てのアプリや service の data管理に DB が使用されている
## RDB (Relational Database)と NoSQL (not only SQL)
- 表形式で DB を保存しているもの
  - SQLite , PostgreSQL , MySQL
  - SQL (Structured Query Language)
  - python よりも学習範囲は狭い
- NoSQL (not only SQL)
  - SQL だけじゃないだよと言う意味
  - XML , JSON のドキュメントで管理する、ドキュメント型
  - データ間の繋がりを保管する、グラフ型
  - key : value を指定するやり方
  - カラムの概念を取り入れた、カラム型
