# for ループ
# ある要素（list）に対して１回１回とってきて回して list の中身が無くなったら終了

# fruits = ['apple', 'peach', 'grapes', 'banana']

# for fruit in fruits:
#     print(f"I love {fruit}!!")

# for char in "hello world!!":
#     print(f"char: {char}")

# iteration と iterable
# list と 文字列を for で回す事ができる
# for ループで回す事を iteration（イテレーション）とい言う
# iterationできる object を iterable (イテラブル)と言う

# challenge1
# fruits = ['apple', 'peach', 'grapes', 'banana']

# favorite = input('好きなフルーツはなんですか？')
#
# for fruit in fruits:
#     if fruit == favorite:
#         print(f"I love {fruit}!!")
#     else:
#         print(f"{fruit}は別に普通です。")

# challenge2
# apple = """りんごは好きですか？
# y: yes
# n: no
# """
# peach = """peachは好きですか？
# y: yes
# n: no
# """
# grapes = """grapesは好きですか？
# y: yes
# n: no
# """
# banana = """bananaは好きですか？
# y: yes
# n: no
# """
# favorite = []
# least_favorite = []
#
#
# question = input(apple)
# if question == "y":
#     apple = "apple"
#     favorite.append(apple)
#     print(f"好きなフルーツ{favorite}")
#     print(f"嫌いなフルーツ{least_favorite}")
# if question == "n":
#     apple = "apple"
#     least_favorite.append(apple)
#     print(f"嫌いなフルーツ{least_favorite}")
#     print(f"好きなフルーツ{favorite}")
# question = input(peach)
# if question == "y":
#     peach = "peach"
#     favorite.append(peach)
#     print(f"好きなフルーツ{favorite}")
#     print(f"嫌いなフルーツ{least_favorite}")
# if question == "n":
#     peach = "peach"
#     least_favorite.append(peach)
#     print(f"嫌いなフルーツ{least_favorite}")
#     print(f"好きなフルーツ{favorite}")
# question = input(grapes)
# if question == "y":
#     grapes = "grapes"
#     favorite.append(grapes)
#     print(f"好きなフルーツ{favorite}")
#     print(f"嫌いなフルーツ{least_favorite}")
# if question == "n":
#     grapes = "grapes"
#     least_favorite.append(grapes)
#     print(f"嫌いなフルーツ{least_favorite}")
#     print(f"好きなフルーツ{favorite}")
# question = input(banana)
# if question == "y":
#     banana = "banana"
#     favorite.append(banana)
#     print(f"好きなフルーツ{favorite}")
#     print(f"嫌いなフルーツ{least_favorite}")
# if question == "n":
#     banana = "banana"
#     least_favorite.append(banana)
#     print(f"嫌いなフルーツ{least_favorite}")
#     print(f"好きなフルーツ{favorite}")

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