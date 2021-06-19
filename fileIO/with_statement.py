f = open("pep8_introduction.txt")
# open の戻り値は f(file object)
# f は for 文で回せる iterable (イテラブル)
# for ループで回す事を iteration（イテレーション）とい言う
# iterationできる object を iterable (イテラブル)と言う

# for文で回して一行一行とってくる
# 巨大なfileを一行一行とってきてメモリを節約する事ができる

# try:
#     for line in f:
#         print(line, end="")  # print() は default で文字の最後で改行を入れている
# finally:
#     f.close()  # 基本的に file object で作業し終えた close する

# with statement を使用することにより上記を簡潔に記述できる
# 基本的に open を使用する時には with を使用する事！！
# with statement を使用する事により、code 実行が終了すると自動で close をしてくれる
with open("pep8_introduction.txt") as f:
    for line in f:
        print(line, end="")




# default 改行プラス改行
print("hello\n")
print("world\n")

# default の改行
print("hello")
print("world")

# default で改行を無くす
print("hello", end="")
print("world", end="")
