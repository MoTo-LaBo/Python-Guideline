# for文でループを回す：メモリを減らす
# with open("pep8_introduction.txt") as f:
#     for line in f:
#         print(line, end="")


# .read() : ファイルの中身の全てを一つの string として返す事ができる
# 大きなファイルの場合は使用しない事、全てがメモリに乗ってしまう
# with open("pep8_introduction.txt") as f:
#     print(f.read())

# .readline() : 一行ずつ取得し string で返す
# with open("pep8_introduction.txt") as f:
#     line = f.readline()  # 1行目を取得
#     line = f.readline()  # 2行目を取得
#     # print(line)
#     while line:
#         print(line, end="")
#         line = f.readline()

# .readlines() : 全ての行を list の形で返す
with open("pep8_introduction.txt") as f:
    lines = f.readlines()
    print(lines)