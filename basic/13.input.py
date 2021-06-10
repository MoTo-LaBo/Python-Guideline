# input(): ユーザーの入力した値(文字列)を取得する

# age = input("何歳ですか？")
# print("あなたは{}歳です".format(age))
# 入力で返したものは、文字列(string)で返信(代入)されるので注意する
# 整数(integer)と文字列(string)間は error になるので意識しておくこと

# challenge1
# int で string を integer に変換する
age = int(input("何歳ですか？"))
casino_age = 18
game_text = """プレイするゲームを選択してください
1: ルーレット
2: ブラックジャック
3: ポーカー
 """
if age >= casino_age:
    print("どうぞお入りください")
    game = input(game_text)
    if game == "1":
        print("あなたはルーレットを選びました")
    elif game == "2":
        print("あなたはブラックジャックを選びました")
    elif game == "3":
        print("あなたはポーカーを選びました")
    else:
        print("1~3を選んでください")
else:
    print("{}歳未満の為カジノに入場はできません".format(casino_age))



