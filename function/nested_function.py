# nested function (関数の中で関数を定義する)
# def outer(outer_param):
#     def inner():
#         print("This is inner function")
#         print(outer_param)
#     inner()
#
#
# outer("outer arg")


# def outer():
#     outer_param = "outer arg"
#     def inner():
#         print("This is inner function")
#         print(outer_param)
#     inner()
#
#
# outer()


msg = "I am global"

def outer():
    msg = "I am outer"
                       # inner 関数を定義する時は一行開ける
    def inner():
        msg = "I am inner"
        print("This is inner function")
        print(msg)
    inner()
    print(msg)


outer()
print(msg)


# nonlocal を使用
msg = "I am global"

def outer():
    msg = "I am outer"
                       # inner 関数を定義する時は一行開ける
    def inner():
        nonlocal msg
        msg = "I am inner"
        print("This is inner function")
        print(msg)
    inner()
    print(msg)


outer()
print(msg)





