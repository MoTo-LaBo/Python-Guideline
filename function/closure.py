# Closure: クロージャー
# nested function の中では、closure は現場でよく使用される

# python は全てを object として扱う
# 全てのデータ型が object なので、データ型の種類を選ばずにデータ型をデータ型の中に入れるという全てを入子型にできる

# 関数はどうなのか？　関数も全てk object ではある
def compute_square(num):
    return num * num


print(compute_square)  # <function compute_square at 0x106fed040> function object
f = compute_square     # 関数自体も object なので代入できる
print(type(f))         # <class 'function'>
print(f(10))           # 関数の object を変数に入れる事によって、f(という変数)を使用して ()call する事ができる

function_list = ["1", 1, True, f]  # どんな種類のものでも代入できる
print(function_list[-1](10))       # list から取り出したり、dictionary の key とか value にも使用できる


# 関数も引数として渡す事がで切る
def execute_func(func, param):
    return func(param)


print(execute_func(f, 10))


# 関数をreturnする
def return_func():

    def inner_func():
        print("This is an inner function")
    return inner_func  # () が付いてないところに注意。実行結果自体は返さない。何も返さない関数 None。objectとして返される


f = return_func()
print(type(f))
f()


# closure : 状態をキープした関数
# 状態が静的な例
def power(exponent):
    def inner_power(base):
        return base ** exponent
    return inner_power


power_four = power(4)
print(power_four(3))

power_five = power(5)
print(power_five(2))

power_two = power(2)
print(power_two(5))


# 状態が動的な例
def average():
    nums = []

    def inner_naverage(num):
        nums.append(num)
        return sum(nums) / len(nums)
    return inner_naverage


average_nmus = average()
print(average_nmus(5))
print(average_nmus(15))
print(average_nmus(4))
print(average_nmus(10))
print(average_nmus(12))


