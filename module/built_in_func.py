# built in function
# python に標準で入っている function

from re import search
import time

print(dir())
# dir 関数を使う事によって何に、アクセスできるか確認できる
# ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'search', 'time']

# dir(): () の属性を取得できる

# print(dir(__builtins__))
__builtins__.print('hello world')  # 上記のprint と同じ。いつもは__builtins__.が省かれている
                                   # print()は、__builtins__に格納されている

# __file__
# __doc__
# 上記のような属性、（関数・変数）は、マジックメソッドと呼ばれる。
# 開発者側は定義する事はない。できない！


