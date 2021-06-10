# built in function
# 関数 : ある program をまとめて関数で定義したもの

# type ()
print(type("Hello"))
print(type(1))

# id ()
hello_id = id("hello")
print(hello_id)
hello = "hello"
hello2 = "hello"
print(id(hello))
print(id(hello2))
w = "world"
print(id(w))
print(id("world"))