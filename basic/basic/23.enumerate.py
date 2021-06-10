# enumerate (エニュメレイト)
# enumerate を使用すると list の値と index の情報を取得してくる事ができる
# object だけではなく、index も ループで実行（回す）事ができる

fruits = ['apple', 'peach', 'grapes', 'banana']
# index  |   0    |   1   |    2    |    3    |
# index  |  -4    |  -3   |   -2    |   -1    |

for idx, fruit in enumerate(fruits):
    print(idx)
    print(fruit)
# enumerate 関数は、２つの値を出す: index , element
# なので index用 , element用 の２つの変数を用意する必要がある
# indexによく使われる変数は " idx " がよく用いられる ※ ,(カンマ)" "(スペース)で区切る

for x in enumerate(fruits):
    print(x)
# 上記を実行すると下記が表示される ※ enumerate 値の返し方（処理のされ方)
# (0, 'apple')
# (1, 'peach')
# (2, 'grapes')
# (3, 'banana')
# (idx, 'fruits') ※ ,(カンマ)" "(スペース) Tuple (タプル)
