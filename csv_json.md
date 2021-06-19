## csv file
- CSV : comma separated values. カンマ区切りでデータを保持するフォーマット(拡張子は.csv)
- csv モジュールを使ってアクセスする
- カンマ以外でも、tab や 「：」、「；」で区切る事がある。この区切り文字の事を delimiter (デリミター)と呼ぶ
- csv は表形式のデータになるのでデータの量が大きくなる可能性がある

## json file
  - JSON : javascript object notation. 特にweb でのデータ送受信によく使われる
  - json module を使う
### json module (improt json)
#### json file を python のデータ構造で読み込む
    json.load
#### python のデータ構造を json file に書き込み
    json.dump
#### json 文字列を python のデータ構造に変換
    json.loads
#### python のデータ構造を json 文字列に変換
    json.dumps
