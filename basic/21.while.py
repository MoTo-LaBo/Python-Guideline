# while ループ: ~の間
# while ループは、何か条件を設定してその条件がTrueのずっと処理を続ける
# count = 0
# while  count < 10:
#     print(count)
#     count +=1


# break と continue
# continue: をつけると False の場合また同じ input を聞いてくれる
# 正しい値が入力されるまで無限にループされる
# break はループを終了させる
# 注意する場所は無限ループを作らないという事。どこかで False を作るか break で終了させる条件分岐を作る事
# continue を記述しなくてもループは回るが、continue を付けた方が親切で分かりやすい
# while True:
#     age = int(input("あなたは何歳ですか?"))
#     if not 0 <= age < 120:
#         print("入力された値は正しくありません")
#         continue
#     else:
#         print(f"あなたは{age}歳です")
#         break


# code を改善したり修正したりする事を refactoring(リファクタリング)という
# challenge1
# casino_age = 18
# game_text = """プレイするゲームを選択してください
# 1: ルーレット
# 2: ブラックジャック
# 3: ポーカー
#  """
#
# age = int(input("何歳ですか？"))
# if age >= casino_age:
#     print("どうぞお入りください")
#     while True:
#         game = input(game_text)
#         if not game:
#             print("そのようなゲームはございません")
#             continue
#         elif game == "1":
#             print("あなたはルーレットを選びました")
#             break
#         elif game == "2":
#             print("あなたはブラックジャックを選びました")
#             break
#         elif game == "3":
#             print("あなたはポーカーを選びました")
#             break
#         else:
#             print("1~3を選んでください")
# else:
#     print(f"{casino_age}歳未満の為カジノに入場はできません")

# answer
casino_age = 18
game_text = """プレイするゲームを選択してください
1: ルーレット
2: ブラックジャック
3: ポーカー
 """
age = int(input("何歳ですか？"))
if age >= casino_age:
    print("どうぞお入りください")
    while True:
        game = input(game_text)
        if game == "1":
            print("あなたはルーレットを選びました")
            break
        elif game == "2":
            print("あなたはブラックジャックを選びました")
            break
        elif game == "3":
            print("あなたはポーカーを選びました")
            break
        else:
            print("1~3を選んでください")
else:
    print(f"{casino_age}歳未満の為カジノに入場はできません")