# 変数の定義
# correct
x = 1
y = 1

# wrong
# python では下記のような記述はしない、他の programing 言語によってはある
# 無駄に行の最後にスペースは入れない　x = 1'○'　
xxx  = 1
y    = 1

# 関数の引数の「=」にはスペースは不要
def complex(real, imag=0.0):
    return magic(r=real, i=imag)

# operator の周りにスペース1個
x = x + 1
x += 1
x = x*2 - 1  # operator に、priority がある場合はスペースをなくす
a = x*x + y*y
c = (a+1) * (a-1)

# カンマの後ろにはスペースを入れる
range = (1, 11)
a = [1, 2, 3, 4]
b = (1, 2, 3, 4)

# 下記の場合はカンマの後にスペースは不要
foo = (0,)  # tuple 何だけれども一つの要素しかない

# カンマがあっても無くてもどちらでもいいが… git version 管理の事を考えると
# ,(カンマ)を付けておいた方が楽変更された部分が、次の行からという事になるから
FILES = [
    'setup.cfg',
    'tox.ini',      # カンマを付けなくてもいいが、付けておいた方が楽
    # 'tox.ini',    # 行が増えたときに、git version 管理で余計なところまで変更されたことにはならないから
]

# 行の折り返し
# foo = long_function_name(var_one, var_two,
#                          var_three, var_four)
#
# foo = long_function_name(
#     var_one, var_two,
#     var_three, var_four)

def long_function_name(
        var_one, var_two, var_three, var_four):
    print(var_one)

# '\' (バックスラッシュ)を使用して改行
print("このように表示する文章が長かったりする場合\
バックスラッシュで区切る事ができます")

# + 演算子が並ぶように記述する　※ 最近はこちらの方が見やすいと言われている
a = 100000000000 \
    + 100000000 \
    + 10000000 \
    + 1000000000

# 関数間は二行開ける
def func1():
    pass


def func2():
    pass


class MyClass:
    def __init__(self):
        pass

    def method(self):
        pass

# import
# correct
import os
import sys

# wrong
import os, sys

# from を付ける場合は一行にまとめて記述OK
from subprocess import Popen, PIPE

# improt の順番
# 1, Standard library (time, sys)
# 2, Third party (numpy, pandas) pip で install してきたものを記述する
# 3, Our library
# 4, Local library
# それぞれの間に１行空ける・abc 順に記述する

# absolute import (なるべく、アブソルート import を使用する)
# import mypkg.sibling
# from mypkg import sibling
# from mypkg.sibling import example


# コメント
# コメントは常に最新になるように心がける
# なるべく英語で記述すること。絶対に日本語が分からない人が読まないのであれば日本語でOK
# 書くときは文章で書くのが望ましい
# ＃の後に半角スペースを入れる
# インラインコメントは code の後に半角スペースを２つ入れて＃を書く
# Docstring は基本的に全ての module, function, class, method に付ける(nonpublic な外からアクセスしない関数には不要)
# その code が「何をしているのか」より「なぜそう書いたのか」の方が有益


# Return
def foo(x):
    if x >= 0:
        return math.sprt(x)
    else:
        return None


# return で短縮出来るところもあるが、return を記述するときは全てしっかりと記述すること
# 下記の記述の仕方でも間違いではない。記述がなければ default で None になる
# def foo(x):
#     if x >= 0:
#         return math.sprt(x)

# object タイプの確認 isinstance() を使う
# correct
if isinstance(obj, int):
    pass

# wrong
type(obj) is type(1)

# Boolean に対して比較演算子を使用しない
bool_var == True
# correct
if bool_var:
    pass
# wrong
if bool_var == True:
    pass

# type hint (type annotation)
def greeting(name: str) -> str:
    return "Hello" + name
# 一つでも hint を付けたら全てに付ける
# python が type チェックをしてくれるわけではない
# python は動的型付け言語であることを意識する
# type hint を強制したり、命名規則に入れるべきではない