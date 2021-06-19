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
  - 他の module や機能との結合 test
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
