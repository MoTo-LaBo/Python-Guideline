# 変数へ代入 : assignment

# 変数の命名規則 (naming convention)
# 一文字目は文字から始まる
# 文字、数字、＿（アンダースコア）を使う
# Case sensitive (大文字と小文字を区別する事)
# hello と Hello は、＝ にはならない

# snake_case (スネークケース)
# 小文字の英単語を(アンダースコアでつなぐ)
# 変数名で使用される

# Camel Case (キャメルケース)
# 各単語の１文字目が大文字になっている（ラクダのコブのみたいだから）
# class で使用される

# hard codeing (ハードコーディング)
# 変数を使用しないで、codeing する事。良いとはされていない
hello = 'hello'
world = 'world'

# format 関数 : (文字列に使用可能)

print("{} {}".format(hello, world))

name ="John"
print("Hey, {}!! How are you doing?".format(name))

balance = 100
print("balance: {}".format(balance))

# fstring 関数 : (format の別のやり方。こちらの方が処理が早いので推奨されている)
print(f"{hello} {world}")

name ="John"
print(f"Hey, {name}!! How are you doing?")

balance = 100
print(f"balance: {balance}")

# 開発環境でのコメントの記述
# code の補完として使用する
# なぜそのような Code なのか？ どういった処理をしているか？
# 他の人、未来の自分が思い出し安いように記述
# なるべくコメントを使用しない code をかく
# 変数名を分かりやすくする事で何を記述しているか、理解しやすい