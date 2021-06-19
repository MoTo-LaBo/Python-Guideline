import csv

# csv.reader
# with open("example.csv") as f:
#     reader = csv.reader(f)
#     for line in reader:
#         print(line[1])

# csv.DictReader : DictReader が使用できるフォーマットであれば使用した方が効率的
# with open("example.csv") as f:
#     reader = csv.DictReader(f)
#     for line in  reader:
#         print(line['Country'])

# index を指定して data を取得してくるより、column で取得してきた方が扱いやすい


# csv.writer(f)
# sample.csv がなければ open function は新たに file を作成する
# with open("sample.csv", mode='w') as f:
#     writer = csv.writer(f)  # csv.writer が返す object を使用して (writer に入れる)
#     writer.writerow(['value1', 'value2'])
#     writer.writerow(['value3', 'value4'])
# list なのでどうしても…扱いにくい. dictionary の方が扱いやすい


# csv.DictWriter
with open("sample.csv", mode='w') as f:
    writer = csv.DictWriter(f, ['col1', 'col2'])  # class なので、class のインスタンスを作ることになる。writer 変数に入れる
    writer.writeheader()
    writer.writerow({'col1': 'value1', 'col2': 'value2'})
    writer.writerow({'col1': 'value3', 'col2': 'value4'})


# 基本的に csv は dictionary 形式で扱った方が作業効率が良い
