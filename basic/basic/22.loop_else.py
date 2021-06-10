# loop else

# for文の else
# for で list のループを実行していって、回りきったら最後 else の print() が表示される
# fruits = ['apple', 'peach', 'grapes', 'banana']
#
# for fruit in fruits:
#     choice = input(f"あなたが探しているフルーツは {fruit} ですか？ y/n:")
#     if choice == "y":
#         print("見つかってよかったですね")
#         break
#     else:
#         print("そうですか…")
# else:
#     print("お探しのフルーツは見つかりませんでした")


# while else
# count = 0
# while count < 10:
#     print(count)
#     count += 1
# else:
#     print("countは10未満ではなくなりました")

# challenge
balance = 1000
game_price = 200

while balance >= game_price:
    choice = input(f"１回{game_price}円のゲームに参加しますか？(残高:{balance}円)y/n:")
    if choice == "y":
        balance -= game_price
        print(f"あなたの残高{balance}円です")
    elif choice == "n":
        print("また遊びましょう!")
        break
    else:
        print("yかnで回答してください")
else:
    print(f"残高が足りません{balance}円です")











