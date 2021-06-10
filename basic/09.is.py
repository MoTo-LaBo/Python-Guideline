# is 演算子：同じ object かどうかを判断・比較する演算子
a = 1
b = 1
c = 3
d = a
e = 2 - 1  # 1

# id は全て同じになる = 全て同じ object
print(id(a))
print(id(b))
print(id(1))
print(a is b)  # True
print(a is not c)  # True

print(d is a)  # True
print(d is b)  # True

print(a is e)  # True

hello = "hello"
hello2 = "h" + "e" + "l" + "l" + "o"  # "hello"
print(hello, hello2)  # hell hell
print(hello is hello2)  # True

hello = "konnichwa"  # 代入するので,ここから別の object になる
print(hello)
print(hello is hello2)  # False

# None かどうかの判定によく使う
nothing = None
print(nothing is None)
print(id(nothing))
print(id(None))

