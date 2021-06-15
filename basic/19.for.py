# for ループ
# ある要素（list）に対して１回１回とってきて回して list の中身が無くなったら終了

# fruits = ['apple', 'peach', 'grapes', 'banana']
#
# for fruit in fruits:
#     print(f"I love {fruit}!!")
#
# for char in "hello world!!":
#     print(f"char: {char}")

# iteration(イテレーション) と iterable(イテラブル)
# list と 文字列を for で回す事ができる
# for ループで回す事を iteration（イテレーション）とい言う
# iterationできる object を iterable (イテラブル)と言う

# challenge1
# fruits = ['apple', 'peach', 'grapes', 'banana']
#
# favorite = input("好きなフルーツは？")
#
# for fruit in  fruits:
#     if fruit == favorite:
#         print("I love {}".format(fruit))
#     else:
#         print("{}は別に普通…".format(fruit))


# challenge2
# favorite_fruits = []
# normal_fruits = []
# fruits = ['apple', 'peach', 'grapes', 'banana']
#
# for fruit in  fruits:
#     choice = input(f"{fruit}は好きですか？: y/n")
#     if choice == "y":
#         favorite_fruits.append(fruit)
#     else:
#         normal_fruits.append(fruit)
#
# print(f"favorite fruits: {favorite_fruits}")
# print(f"normal fruits: {normal_fruits}")



# answer
favorite_fruits = []
normal_fruits = []
fruits = ['apple', 'peach', 'grapes', 'banana']

for fruit in fruits:
    choice = input(f"{fruit}は好き？y/n")
    if choice == "y":
        favorite_fruits.append(fruit)
    else:
        normal_fruits.append(fruit)

print(f"favorite_fruits: {favorite_fruits}")
print(f"normal_fruits: {normal_fruits}")