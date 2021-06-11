# 引数 () の部分
#              parameter:(引数)
# def function(first, second, third):
#     print(f"first: {first}, second: {second}, third: {third}")


# argument: ↓ 上記の ( 引数 ) に渡す部分 → parameter ↑
# function("1", "2", "3")  # 順番通りに parameter に入れていく

# 順不同の場合 ※ parameter を指定する
# function("1", third="3", second="2")


# default で定義する parameter の事を key word parameter
# default で定義しない parameter の事を positional parameter
# key word 引数は、positional 引数 の後に記述する規則がある
# 順番通りに引数を渡すときに、pcが混乱して分からなくなってしまうから
def function(first, second, third = "3"):
    print(f"first: {first}, second: {second}, third: {third}")


function("1", "2")
