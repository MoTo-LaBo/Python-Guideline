# casting (キャスティング): データ型の変換
# python はデータの変換をしてくれないので、明示的にデータ変換をしないといけない


# データ型一覧

# string
# '1'

# int(integer)
# 1

# float
# 1.0

# boolean
# True,False

# list
# [1, 2, 3, 4, 5]

# tuple
# (1, 2, 3)

# dictionary
# {"one": 1, "two": 2, "three": 3}

# set
# {1, 2, 3, 4, 5}

# casting 一覧
# str(), int(), float(), list(), bool(), tuple(), set()

print(1 + int("1"))  # 整数
print(str(1) + "1")  # 文字列 + 文字列
print(float("1"))    # 小数
print(list("hello"))     # ['h', 'e', 'l', 'l', 'o'] 文字列
print(bool(1))     # True
print(bool(0))     # False
print(tuple([1, 2, 3]))  # (1, 2, 3) list から tuple に変換
print(set([1, 2, 3, 4, 5, 5]))  # {1, 2, 3, 4, 5}　listから重複が無くなった set になる

# str() と int() はよく使用されるので覚えておく



