# mutable(ミュータブル): 変更可能なオブジェクト list,dict,set
# fruits = ['apple', 'peach', 'banana']
# print(f"fruitsのIDは{id(fruits)}です")
# fruits.append('lemon')
# print(fruits)
# print(f"fruitsのIDは{id(fruits)}です")

# immutable(イミュータブル): 変更不可能なオブジェクト int,float,str,bool,tuple
# fruit = 'apple'
# print(f"fruitのIDは{id(fruit)}です")
# fruit += ', lemon'
# print(fruit)
# print(f"fruitのIDは{id(fruit)}です")

# メモリーを取る効率の悪い coding
# immutable なので、毎回違う変数を作っている
text = ""  ## 1-2-3-4-5-6-7-...
for i in range(1, 11):
    if i == 1:
        text += str(i)
    else:
        text += '-' + str(i)
print(text)

# 効率の良いcoding
# list に .append する形で使用している
# list は mutable なので上書き保存のような事ができる。メモリの効率がよくなる
text_list = []
for i in range(1, 11):
    text_list.append(str(i))
text = "-".join(text_list)
print(text)

# より良い code を書くことを 「 Pythonic code　」 という。 Python らしい、シンプルで読みやすい良いコードの書き方
