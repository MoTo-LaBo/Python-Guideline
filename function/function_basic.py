# function (関数)
# 関数の命名規則は、基本的には変数の命名規則と同じ

# build in function(python に元々入っているもの)
# print()
# len()
# input()
# 基本的には実際の開発では、関数をたくさん作って coding していく

# 華氏から摂氏に変換する
fahrenheit = 72


def fahrenheit_to_celsius(fahrenheit):  # define: 定義する、意味を明確にする、(…と)定義する
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius


celsius = fahrenheit_to_celsius(fahrenheit)
print(celsius)
# 関数と関数の間は2行開ける。pythonではよく言われている
# 関数は関数で完結。関数の外は関数の外で完結するので関数内の変数・引数と関数外の変数と引数が同じである必要はない
# 同じでなくてもprogramは実行される。同じにする理由は、コメントを書く事を省く為。誰が見てもすぐに分かるようにする為
