# 「:」コロンを使って、複数の要素をとってくることができる (slicing)
enve =[2, 4, 6, 8, 10, 12]
# index 0 1  2  3   4   5
# 1以上4未満のindex(integer:整数)をとってくる
# 基本は[開始:未満]
print(enve[1:4])
print(enve[0:4])
# 0は省略できる
print(enve[:4])

# 下記はどちらも同じ値になる
print(enve[3:5])
print(enve[3:-1])

# index 3 以上
print(enve[3:])

# 省略。全て表示
print(enve[:])

# 文字列にも使用可能
text = "hello world"
print(text[3:])

# [開始:未満:step]
print(text[2:10:2])  # 2個飛ばし

print(text[::-1])  # 全て表示で、逆順になる
