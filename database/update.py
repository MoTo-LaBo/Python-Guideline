import sqlite3

con =sqlite3.connect("sample.db")
cursor = con.cursor()

# User名を指定して、Aeg （年齢）を更新するprogram

# ユーザーに何をしてもらいたいか？
target_name = input("whose 'age' do you want to update?")
new_age = input("Tell me new age:")
print(target_name, new_age)


# SQL 文を作成
# 文字列を使って SQL を作成するという事は脆弱性があるので注意する
# SQL ingection という攻撃方法 : new age の後にセミコロン「; DROP TABLE User;」 で User table data を消されてしまう
# update_query = f"UPDATE User SET age = {new_age} WHERE name = '{target_name}'"
# cursor.executescript(update_query)

# User の input で update する。ほとんどそのような場合だが…
# 上記のような攻撃を防ぐ為に必ず、 execute method を使って プレイスフォルダーを使って値を tuple で渡す
update_query = 'UPDATE User SET age = ? WHERE name = ?'
cursor.execute(update_query, (new_age, target_name))
con.commit()
