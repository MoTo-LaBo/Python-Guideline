class MyClass(object):  # (object) class は、全ての object の元となるものである
                        # 上記の object class には、__str__ が実装されている
    def __str__(self):
        return "My classの__str__"


def printvalu(arg):
        print(arg + 1)

printvalu(True)

various_types = [1, "1", True, [1, 2, 3], (1,), {'1': 1}, {1}]
for elem in various_types:
    print(elem)  # .__str__() という method を持っているから


# mc = MyClass()
# print(mc)  # mc.__Str__ = My classの__str__()
# print(1)  # 1.__str__()
# print("1")  # "1".__str__()
# print(True)  # True.__str__()
# print([1, 2, 3])  # [1, 2, 3].__str__()

# 上記が polymorphism(ポリモーフィズム)
# 全てのdata型が、print()というものに入れたら同じ振る舞いをしている
# 上記の object は printable それは全ての object に __str__ があるから出来ることである
# 全ての元となる object class に __str__ が実装されていて、全ての object は、object class を継承しているから出来る事
# 継承は、polymorphism を実現する手段の一つである

# 動的型付け言語 (dynamically typed language)
# python は実行して初めてその変数の型付けを行う
# 対義語は静的型付け言語(statically typed language)
# python では「型」よりも「振る舞い」に関心がある
# 例）int かどうかよりも, + 演算が出来るかどうかに関心がある
