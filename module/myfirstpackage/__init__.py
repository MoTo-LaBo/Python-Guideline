# 名前空間（name space）
# module1 の myfunc は、myfirstpackage.module1.myfunc (という名前空間)に属する
# module1 module2 で同じ関数名でも、属する名前空間が異なれば別ものとして扱う事ができる

# 名前空間 package (python 3.3以降)
# __init__.py がない package
# 異なるパスに存在する同名の package を共通のものとしてまとめる事が可能
# 特に理由がなければ __init__.py を作って通常の package とすること


# __init__.py
# __init__.py を置く事で、python はその directory を package として認識する
# __init__.py には初期化用 code を記述する　(import 時に実行される)
# __init__.py に import文を書くことで module名をスキップして、package. のあとに関数名やクラス名に access できる
# __init__.py に __all__ を定義する事で、その package が import* で import された際に import させる関数やクラスを定義する事ができる
# __init__.py に関しては、import * はよく使われる！！　__init__.py に関しては問題はない

from myfirstpackage.subdir.module2 import *
