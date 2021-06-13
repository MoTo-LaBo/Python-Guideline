# Decorator : 関数に機能を付属する(デコレートする)
# nested function
# Python で開発する上で必ずと言って良いほど出てくるので確実に覚える

def say_name(name):
    print(f"I'm {name}")


say_name("Jiro")

# 上記の例をDecorator する
# decorator を使用する時は、(*ags, **kwargs) を使用する事
# (*ags, **kwargs) を使用する事によってどんな引数を持った関数でも対応できる
def greeting(func):
    # def inner(name):     # decorator を使用する時はもっと繁栄的に記述する ※ 複数の時に対応できなくなる
    def inner(*args, **kwargs):
        print("Hello")
        # func(name)       # decorator を使用する時はもっと繁栄的に記述する ※ 複数の時に対応できなくなる
        func(*args, **kwargs)
        print("Nice to meet you!")
    return inner


@greeting
def say_name(name):
    print(f"I 'm {name}")


@greeting
def say_name_origin(name, origin):
    print(f"I'm {name}, I'm from {origin}")


# say_name = greeting(say_name)
say_name("Jiro")
say_name_origin("Taro", "Tokyo")


