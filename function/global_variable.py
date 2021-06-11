# global 変数 : 関数内からグローバル変数を変更する

# age = 30
#
#
# def print_age():
#     global age
#     age = 20
#     print(f"I'm {age} year old")
#
#
# print_age()
# print(age)


# global をたくさん使用してしまうと、自分の気づかないところでglobal変数が更新されてしまうのでbugの元になる
# 関数の外にアクセスするという記述の仕方はそんなに良い記述の仕方ではない
# なるべく local 変数で定義して、global 変数を使用しなくて良いようにする事がbest practice
# call_count = 0

CALL_COUNT = 0  # 後で書き換えられたくない時は、大文字で記述する : constant variable(コンスタントヴァリアブル)
                # 命名規則の暗黙の了解で、大文字の場合は後で書き換えないで下さいという意思表示
                # その方が安全な記述の仕方
def print_conut1():
    global call_count
    call_count += 1
    print(f"関数1 :{call_count}回目")


def print_conut2():
    global call_count
    call_count += 1
    print(f"関数2 :{call_count}回目")


print_conut1()
print_conut2()
print(call_count)