# *args: 不特定多数の引数を関数に渡す事が可能
# tuple で受け取る
# print("hello", "world", "test")
# def get_average(*args):
#     print(args)
#
#
# get_average(1, 2, 3, 4, 5)


def get_average(*args):  # *args 1 2 3 4 5 6 7 8 ※ *(アスタリスク)をつけると unpacking される
    num = len(args)  # args の length (引数の数をnumに代入) (1, 2, 3, 4, 5, 6, 7, 8)
    if num == 0:      # 受け取る側は*(アスタリス)を抜いて tuple で受け取ることができる
        return 0
    total = sum(args)  # sum()は、要素や tuple の合計を出してくれる
    return total / num


average = get_average(1, 2, 3, 4, 5, 6, 7, 8)
print(average)


# **kwargs : dictionary 形式で受け取る version
# def kwargs_func(**kwargs):
#     print(kwargs)
#
#
# kwargs_func(param1=10, param2=6, param3=100)

def kwargs_func(**kwargs):
    parame1 = kwargs.get('param1', 1)
    parame2 = kwargs.get('param2', 2)
    parame3 = kwargs.get('param3', 3)

    print(f"param1: {parame1}, param2: {parame2}, param3: {parame3}")


kwargs_func(param1=10, param2=6, param3=100, param4=4)

# * と ** は unpacking operator
numbers = (1, 2, 3)
print(numbers)   # tuple
print(*numbers)  # unpacking
print(1, 2, 3)   # * と同じ unpacking

a = {'a': 1, 'b': 2}
b = {'c': 3, 'd': 4}
c = {**a, **b}
print(c)


