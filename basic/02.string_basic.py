# 文字列(strings)
# print 関数 : ()の中に入った文字列の情報をそのまま出力する
print('hello world!!')

# ' (シングルコーテーション) " (ダブルコーテーション)は時と場合で使い分ける
print("I'm file")

# '''(シングルコーテーション * 3) """ (ダブルコーテーション * 3)
# 文字列を複数行定義出来る
print("""
Hello world!!
How are you doing?
""")

print('''
Hello world!!
How are you doing?
''')

# \n (改行)　\t (tab挿入) ※ バックスラッシュ
print("hello \nworld")
print("hello \tworld")

# \n を文字列として扱いたい場合 \\バックスラッシュ*2
# \(バックスラッシュ) を使用すればesc してくれる
print("bash slash n:\\n")
print('I\'m file')

# + で文字列の連結 (演算子)
# ※ spaceは入力しなくても出力されるが…
# 基本的に演算子の周りには space を記述する一般的な規則がある
print("hello" + "world +　"!!")


# データ型
print(1)