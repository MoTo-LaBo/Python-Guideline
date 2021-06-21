import sqlite3

con = sqlite3.connect("sample.db")
cursor = con.cursor()

# for row in cursor.execute("SELECT * FROM User"):
#     print(row)


# cursor 自体が iterator になっている。イテレータの働きをする
# cursor object を irerator として扱っていく


cursor.execute("SELECT * FROM User")
# print(next(cursor))
# print(next(cursor))

# .fetchall : 現在の cursor 以下全てを tuple list で返す
# cursor.fetchall()
# print(cursor.fetchall())  # [(3, 'Taro', 'taro@gmail.com', 25)]
# .fetchall をすると全ての data がメモリに乗るので注意する

# .fetcone : 現在の cursor のレコードを tuple で返す,next と同じ
print(cursor.fetchone())  # (1, 'John', 'john@gmail.com', 30)
print(cursor.fetchone())  #　(2, 'Emily', 'emily@gmail.com', 28)