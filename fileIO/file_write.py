# write : 書き込みでファイルを開く
with open("writing_file.txt", mode='w') as f:
    # file が上書きされる事を = truncated（トランケイテイッド）される: bute = 0 -> 切り詰める(上書きされる)
    f.write("You can write contents here\nuse 'backslash' to break the row")
    f.write("new write() doesn't break row")  # 改行されないで次に続いてしまうので注意する

# print 文を使用することで、わざわざ一行一行改行を入れる必要はない
# default で end="\n" が入っていて、実行されるから
    print("You can add a new row using 'file' parameter", file=f)
    print("You can add a new row using 'file' parameter", file=f)

# mode='w' 書き込みでは、読み込みができないので注意する
    print(f.read())  # io.UnsupportedOperation: not readable