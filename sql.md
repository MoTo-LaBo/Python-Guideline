# SQLlit 3
- 基本操作 command
#### sqllite3 を起動させる
    sqlite3
#### sqllite3 < dbfile > : dbfile という database を作成する
    sqlite3 mydb.db
- 拡張子は通常 .db を用いる
#### .help コマンド : sql で使用できる様々なコマンド一覧表示
    .help
- sqlite3 のコマンドは「 . 」(ドット)から始まる事に注意
### Table (テーブル)
- テーブル（表）の形で data を保管する
#### Table 作成 command
    CREATE TABLE < テーブル名 >(< カラム名>< data型>,< カラム名>< data型>,< カラム名>< data型>,...);
- NULL : 空、何もない data が入っていない
- INTEGER : 整数
- REAL : 小数
- TEXT : 文字列
- BLOB : Binary large object
#### constraint (ルール、制限、束縛)を付ける事が可能
- NOT NULL　　  : NULL を入れない（つまり値が空白なのを許さない）
- DEFAULT　　　 : デフォルトの値をせってする
- UNIQUE　　　　: 値が table 内でユニークになるように設定する（同じ値を持たない）
- PRIMARY KEY　: ID となるカラム
- CHECK　　　　 : ルールのロジックを設定する
#### .tables : 今定義している table の一覧を表示
    .tables
#### .schema : table の構造（schema）を表示する
    .schema
