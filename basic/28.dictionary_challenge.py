# なるべく code を記述するときは、後々メンテナンスがしやすいように hard coding はしない
# データを最適なデータ型で保持しておいて、それを上手く使用する

# casino_age = 18
# game_text = """プレイするゲームを選択してください
# 1: ルーレット
# 2: ブラックジャック
# 3: ポーカー
#  """
# age = int(input("何歳ですか？"))
# if age >= casino_age:
#     print("どうぞお入りください")
#     while True:
#         game = input(game_text)
#         if game == "1":
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

# 上記の while文 を最適化する
game_dict = {'1': 'ルーレット', '2': 'ブラックジャック', '3': 'ポーカー'}
casino_age = 18

age = int(input("何歳ですか？"))
if age >= casino_age:
    print("どうぞお入りください")
    while True:
        print("プレイするゲームを選択してください")
        for num, game_name in game_dict.items():
            print(f"{num}:{game_name}")
        game = input(":")
        if game in game_dict:
         print(f"あなたは{game_dict[game]}を選びました")
         break
        else:
            print("正しい選択肢を選んでください")
else:
    print(f"{casino_age}歳未満の為カジノに入場はできません")
