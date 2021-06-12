# lambda(ラムダ) 関数 (無名関数): 関数に名前を付けるほどでは無い小さい関数、単名な関数

def square(x):
    return x * x


print(square(3))

# 上記を lambda 関数にする
# lambda 関数にする事によって簡易的にできる
s = lambda x: x * x


print(square(3))
print(s(5))
# 実際には上記のように lambda 関数を変数に入れることはしない

# では、どのようにするか？
# 関数の戻り値として lambda 関数を定義したり、ある関数を呼ぶときに引数（　）として使用する事が多い

def power(exponent):
    def inner_power(base):
        return base ** exponent
    return inner_power


third_power = power(3)
print(third_power(2))

# 上記を lambda 関数にする (関数の戻り値として定義)
def power(exponent):
    return lambda base: base ** exponent


third_power = power(3)
print(third_power(2))


# 引数に lambda 関数を入れるケース
# 偶数の数字を除いた奇数だけを取り出したい時
numbers = [6, 2, 5, 43, 5, 36, 67, 2]

def filter_func(num):
    return num % 2


filter_nmu = filter(filter_func, numbers)  # filter 関数は (第一引数, 第二引数) 第一引数に入れた関数を
print(list(filter_nmu))                    # 第二引数に入れた list の各要素を第一引数の関数の引数に入れた時に
                                           # True(奇数) になる要素をfilter(True or False で選別)して取得する
# for num in numbers:
#     print(filter_func(num)

# 上記を lambda 関数にする (lambdaを引数に入れる)　実際の開発ではよく使用するので覚えておく
filter_nmu = filter(lambda num: num % 2, numbers)
print(list(filter_nmu))