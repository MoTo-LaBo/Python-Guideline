#  bylef : 参照渡し <-> 値渡し : byvalue

# python では、全てが「参照渡し」になる！！
# 参照渡し(bylef)とは、下記の例を使って説明すると、one の中に入っている値は " 1 "である
# 関数の引数 a と 変数 one は同じものかどうか？
# 参照渡し(bylef)は、one も a も = (イコール) で同じ object である ※(id も同じ)同じ場所を参照している
# 値渡し(byvalue)は、one に代入されている " 1 " という情報だけを渡している
# なので、値渡し(byvalue)では a <=> 1(one:value) イコール関係にはならない


# def add_numU(a, b):
#     print(f"第1引数aのid:{id(a)}")
#     print(f"第2引数bのid:{id(b)}")
#     return a + b
#
#
# one = 1
# two = 2
# print(f"oneのid:{id(one)}")
# print(f"twoのid:{id(two)}")
# print(add_numU(one, two))


# mutable と immutable では bylef の挙動が変わってくる。下記参照 ↓

# mutable(ミュータブル): 変更可能なオブジェク　list,dict,set
# mutable の object の場合、関数の引数に渡すと関数の引数の中でその " list " が更新されてしまっている
# これは、bug につながるので、注意する事！！
# mutable な object を引数で渡すと、参照渡し(bylef)そのままの挙動になる
def add_fruit(fruits, fruit):
    print(f"変更前のID:{id(fruits)}")  # 4371382720
    fruits.append(fruit)
    print(f"変更後のID:{id(fruits)}")  # 4371382720
    return fruits


myfruits = ['apple', 'lemon', 'peach']
myfruit = 'banana'
print(f"関数呼び出し前のmyfruits:{myfruits}")  # ['apple', 'lemon', 'peach']
add_fruit(myfruits, myfruit)
print(f"関数呼び出し後のmyfruits:{myfruits}")  # ['apple', 'lemon', 'peach', 'banana']


# immutable(イミュータブル): 変更不可能なオブジェクト
# int,float,str,bool,tuple　の場合は変更不可なので、one(integer)自体は上書きされない
# return num で、値が 2 になるが、挙動としては、one は、one のままである
# immutable の場合は、参照渡し(bylef)をしているが表面上の挙動としては、値渡し(byvalue)をしているように見える
def add_one(num):
    print(f"変更前のID{id(num)}")  # 変更前のID4444580144
    num += 1
    print(f"変更後のID{id(num)}")  # 変更後のID4444580176
    return num


one = 1
print(id(one))  # 4444580144
print(f"関数呼び出し前の{one}")  # 関数呼び出し前の 1
add_one(one)
print(f"関数呼び出し後の{one}")  # 関数呼び出し後の 1