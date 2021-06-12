# 基本的な improt の記述の仕方
# imoprt 分は基本的に file の一番上からまとめて記述する
# 記述する順番は 1.標準ライブラリー 2,サードパーティーのライブラリ 3,自分達が作成したライブラリ　4, local ライブラリ
# 一行づつ開けて視認性をよくする

# 1, import sys

# 2, import NumPyとか

# 3, import 自社のライブラリ

# 4, local file etc...

# sys module を import
# python に default で入っている build in module
# path を通す事によって、別の project の file を呼び出す事もできる
import sys
sys.path.append("/Users/moto/Dropbox/udemy/PythonLecture/function")
import docstring

print(sys.path)
print(docstring.multiply(3, 4))


# import mymodule
# mymodule.myfunc()
# print(mymodule.myvariable)


# ある module から特定の関数だけを import する
# from mymodule import myfunc, myvariable, anotherfunc
# myfunc()
# anotherfunc()
# print(myvariable)


# こういう記述もできるが、こちらは非推奨である。何が import されているか分からないから
# あとは _(アンダースコア)から始まる関数は、import できない
#_func()
# from mymodule import *
# myfunc()
# anotherfunc()
# print(myvariable)


# package の中に module がある場合は、
# import package.mymodule と記述する
# import package.subpackage.mymodule と長くなる事がある。そういう場合は from を使用する


# import mymodule as (アズ)をつけると、名前を付け直す事ができる
# こちらも分かりづらくなるので、あまり推奨されていない
# import mymodule as mm
# mm.myfunc()
# print(mm.myvariable)


