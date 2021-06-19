# Python test
- 書いた code は必ずテストする
- 機能を開発するだけなら簡単、品質を保ちながら開発することが難しい
  - app 開発が失敗する原因は品質が保てない事にある
- 開発をするぐらい品質を保つという事は大切な事
- テスの種類
  - code を実行しながら行う test
    - code -> print( ) で実行
  - 自動で実行する test
    - assert a + b == 2, "a + b is equal to 2!" (assert code) python のもっとも基本的な形
  - 他の module や機との結合 test
  - ユーザー目線での動作 test
  - etc..
- 単体 test (Uni Test)と結合 test (Integeration Test)
   - コンポーネント単位の test とコンポーネント間 test
## Test runner
- テスト結果をチェックしてくれたり、デバックしやすいように結果を表示してくれる
- 実際の開発では Test runner を使用して開発するのが一般的
- unit test : python 標準ライブラリー（スタンダード）
  - pytest : テストフレームワーク、非常に有名で多くのプロジェクトで利用されている
### python test は基本ターミナルで、下記のコマンドを実行
     python -m unittest test_filename.py
### 例外ケースのテスト
- 誤ったデータを入れたらきちんとエラーを返すかをテストする
- 考えられる例外は無数に出てくるので、ある程度絞ってテストをする
- with ステートメントを使ってテストする
### pytest
- python のテストフレームワークで、多くのプロジェクトが採用している
- python 標準の assert を使って簡潔にかける
### install
    pip install pytest
### test command
    pytest tests/test_power_pytest.py -v
### test command
    pytest tests  -v
- directory 内の test という名前のつくfile全てを test する
### test カバレッチ
- test が通ったから全てが上手くいっているとは限らない
  - test がどれくらいカバーできているのかを確認する必要がある
  - どれだけの script が 記述した test  code でカバーされているか確認することを test カバレッチという
### pytest カバレッチ を見るには下記を install する
    pip install pytest-cov
### pytest カバレッチ実行
    pytest tests/test_power_pytest.py -v --cov=<file名>
### --cov-report term-missing をつけるとどこが実行されていないか行が表示される
    pytest tests/test_power_pytest.py -v --cov=power --cov-report term-missing
- 全てが cover（100%） されているからといって、 しっかりとした assert がされているとは限らないので、しっかり test ケースを作った上で実行する事
- 意味のないtest を実行しただけでも cover 率は 100% になるので注意！！
### カバレッチを html 形式で保存
    pytest tests/test_power_pytest.py -v --cov=power --cov-report html
### カバレッチを xml 形式で保存
    pytest tests/test_power_pytest.py -v --cov=power --cov-report xml
### 上書きではなく、今ある情報に追加 --cov-append
    pytest tests/test_power_pytest.py -v --cov=power --cov-report xml --cov-append
 > 実際の開発では、coverage.xlm を作成して上記のように何箇所づつに分けてtest しては append (追加)しての繰り返しで file を更新していく。 test script を増やしていく
- 何の為に html data で保存をするのか？
  - 構造化した dataで持つ事によって他の tool で表示する事ができる
  - 構造化した data は汎用性が高く、円グラフ、表 etc...
  - 視認性がよくとても分かりやすい data に変換できる
