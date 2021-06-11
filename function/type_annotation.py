# Type annotation : (タイプアノテーション)を付けて開発する事はほとんどない
# Python を使用するなら使わなくてもいいくらい。知識として頭の片隅に置いておく
# 引数はどういう data型 の引数を渡せばいいか実際の開発では簡単には分からない
# :(コロン) int(integer) で指定できる

def add_nmus(nmu1: int, num2: int) -> int:  # それぞれのdata型及びこの関数の返す値型をintegerにして下さい
    return nmu1 + num2


print(add_nmus(1, 2))

# Type annotation は Python の思考と少しずれている
# Type annotation は静的型付け言語よりの記述の仕方なので、python のメリットが薄らぐ
# Java のように、必ずdata型まで定義する　-> 静的型付け言語　（str_one = "hello", int_one = 1）

# Python -> 動的型付け言語
# Python はあまり型の事を意識せずに記述できる。
# Python は、それぞれの型が何の型か？というよりも、上記のような計算ができるか？というところに重きを置いている
# code を実行するまで、どういう・何のdata型なのかが分からない
# code を実行する事で、なんのdata型か分かる -> 動的型付け言語


