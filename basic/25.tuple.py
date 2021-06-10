# tuple (タプル): 変更できない list []ではく()を使う
# 色々な object を順序立てて保持する事ができる
# 変更させたくないから、tuple を使用するではなく、変更する必要がないから tuple を使用する

date_of_birth = (1990, 2, 3)
# date_of_birth = [1990, 2, 3]
# date_of_birth[0] = 1999
print(date_of_birth)

# list で変数に unpack 処理をしたい場合は list ではなく tuple を使用する
# list は、要素の数が可変する。append,remove,insert したりするから
# tuple で、指定したものは変更できないから
year, month, date = date_of_birth

print(year)
print(month)
print(date)
