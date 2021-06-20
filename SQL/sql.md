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
### Table 作成 command
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
### INSERT でレコード作成
    INSERT INTO < テーブル名 >(< カラム名 >,< カラム名 >) VALUES(< 値 >< 値 >,...)
- 1つの レコードは、１user を意味する
#### 例
    sqlite> INSERT INTO User (UserId, Name, Email, Age)
     ...> VALUES (1, 'John', 'john@gmail.com', 30);
- (UserId, Name, Email, Age) は省略しても良い
### SELECT でレコードを表示する
    SELECT < カラム名 >,< カラム名 >,...FROM < テーブル名 >;
- 最もよく使うSQL 文
- 全てのカラム情報を取得してくるなら SELECT * FROM <テーブル名>; でOK
- .headers on でヘッダーを表示できる
- SELECT 文にはレコード抽出の条件を指定したり、並びを替えをしたり多くの付属機能がある
#### 例
    SELECT * FROM User;
- User テーブル全てのレコードを表示する
### UPDATE と DELETE
    UPDATE <テーブル名> SET <カラム名>=<値> WHERE <条件>;
- 特定のレコードの特定のカラムの値を更新することができる
- WHERE を使用して条件を指定する
#### 例
    sqlite> UPDATE User SET Email="newjohn@gmail.com"
     ...> WHERE Name="John";
### DELETE
    DELETE FROM <テーブル名> WHERE <条件>;
- 特定のレコードを指定したテーブルから削除する
- WHERE を指定しないとテーブルごと削除するので注意！！
#### 例
    DELETE FROM User WHERE Name="John";
### .dump で今までのSQL出力する
- .dump コマンドで今までのSQLを全て出力することができる
- .dump コマンドで出力した時にSQL を実行すれば、今の Database の状態を作ることができる
## Chinook data set
- 大きなデータセットを使って様々なSELECT文を練習する
- Open Data
> https://github.com/lerocha/chinook-database
- Chinook_Sqlite.sql ファイルを使ってデータベースを作成
### ORDER BY でソートして表示する
- SELECT 時にソートして表示する
- SELECT 文に続けてかく
- WHERE の後にかく
- デフォルトでは昇順、DESC を付けると降順になる
#### 例
    SELECT * FROM Employee ORDER BY LastName;
#### 例
    sqlite> SELECT * FROM Employee
    ...> WHERE Title="Sales Support Agent"
    ...> ORDER BY lastName;
### LIKE で曖昧検索する
- WHERE 句に使うことで曖昧検索ができる
- ％は０文字以上の任意の文字、＿ が任意の一文字
- Case insensitive での検索となる("="での検索は Case sensitive)
  - 大文字、小文字を区別しない
#### 例
