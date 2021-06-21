import sqlite3

con = sqlite3.connect("sample.db")
cursor = con.cursor()
create_history_table_query = """
CREATE TABLE IF NOT EXISTS History(
    Name TXET,
    Age INTEGER 
)
"""
cursor.execute(create_history_table_query)
target_name = input("whose 'age' do you want to update?")
new_age = input("Tell me new age:")
update_user_query = 'UPDATE User SET Age = ? WHERE Name = ?'
insert_history_query = 'INSERT INTO History VALUES (?, ?)'

try:
    cursor.execute(insert_history_query, (target_name, new_age))
    cursor.execute(update_user_query, (new_age, target_name))
except sqlite3.Error:
    print("sqlite3 error occurred")
    con.rollback()
else:
    con.commit()

# else: con.commit() があるならば、 con.rollback()はいらないじゃないか？となるが…
# rollback がないと、 error の時点では commite されず pending(ペンディング)の状態：保留という意味
# error がなくなって commite できる状態になった場合に、pending(保留)されていたものも commite されてしまう
# 必ず rollback を付ける事
