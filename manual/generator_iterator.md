# generator
- ジェネレート : メモリを生み出すなにか
- メモリを節約する仕組み
- 全てのデータをメモリに置く代わりに、イテレーション時に毎回出力する（HDから取得したり、計算したり、もしくはその両方
- generator を使用すると必要最低限の data のみメモリに乗せることができる
### yield (イールド)
- return の代わりに yield を使うと、その関数は generator(generator function)になる
- generator function の戻り値は generator iterator と呼ばれるもんで、イテレーションにより yield の値を返す object になる
## iterator と iterable
- generator は iterator の一種
- iterator とは、next()で回すことができて、iter()関数でイテレータ（iterator） を返すものの総称
- iter()関数で iterator を返すものを iterable という
- つまり iterator も iterable である
### next() と .__ next __()
- next(obj)は obj.__ next __()と等しい
- __ xxx __ は magic method と呼ばれる特別な method
- 他の magic methods : __ init __ , __ len __ , __ str __ , __ doc __ , ...
- next()で値を返すということは、 __ next __ method を実装しているという事
- 同様に、 iter() は __ iter __() method を call している
  - つまり iterator は __ next __ () と __ iter __ () が正しく実装された objcet
### generator と iterator の違い
- generator は iterator の一種
- generator は関数で定義する
- iterator は class で定義する
- generator は yield を使用する
- iterator は yield を使用しない
- 使い方は同じ
### generator expression
- yield を使わないで generator を作る
- 書き方はリスト内包表記と同様で、括弧を[ ] ではなく（ ）を使う
- generator 関数よりも簡潔に記述できる
