# recursive function (再帰関数): 関数内で自身の関数をcallする関数
# 階乗: (factorial) 3! = 3 × 2 × 1 = 6
# n! = n * (n-1) * (n-2) * ... * 1
# n! = n * (n-1)!

# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)
#
#
# print(factorial(4))

# challenge1 再帰バージョン
# fibonacci 数を計算する関数を再帰で実装してみる
def fibonacci_recursive(n):
    if n < 2:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
# (1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89 ...)
# (1, 2, 3, 4, 5, 6,  7,  8,  9, 10, 11 ...)index


print(fibonacci_recursive(7))  # (7-1 = 6=(fibonacci = 8)) + (7-2 = 5=(fibonacci = 5)) = fibonacci = 13

# challenge2
# 再帰じゃないバージョン
def fibonacci(n):
    if n < 2:
        return n
    else:
        n_1 = 1
        n_2 = 0
        for _ in range(n-1):
            result = n_2 + n_1
            n_2 = n_1
            n_1 = result
        return result


# print(fibonacci(6))
#
for i in  range(50):
#     # print(i, fibonacci_recursive(i))
    print(i, fibonacci(i))

# 再帰version を使用すると、一見大きな問題も小さい問題を繰り返していくだけで簡単に解ける
# code がスッキリしてエレガントに記述できる
# 再帰関数は便利だがキャッシュ利用をしないとかなり処理速度がかなり落ちるので注意！！
# 同じ計算をしないように、キャッシュを利用をする事
