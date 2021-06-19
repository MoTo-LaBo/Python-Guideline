# mode ='a' (append): ファイルの最後尾に内容を追加
# with open("writing_file.txt", mode='a') as f:
#     f.write("mode=a appends text")


# mode='r+': 読み書きどちらも可能 ※ open の中でポジションが変更するので注意する
# with open("writing_file.txt", mode='r+') as f:
#     f.write("You can write and read with r+ mode!!")
#     print(f.read())
#     f.write("This should be the last sentence.")
#     print(f.read())


# mode='w+' : 読み書きどちらも可能. Truncate されるので注意する。一度fileの中身が無くなって上書きされる
# with open("writing_file.txt", mode='w+') as f:
#     print(f.read())  # file の中身全てが削除されて position が一番最初にくる
#     f.write("You can write and read with w+ mode!!")
#     f.seek(0)  # position を先頭に持ってくることができる。上記で記述した文字列を表示できるようになる
#     print(f.read())  # f.seek() の記述がないと、position が初期のままなので何も表示されない


# modee= 'a+' : 読み書きどちらも可能で、position が最後尾
with open("writing_file.txt", 'a+') as f:
    print(f.read())  # mode= 'a+' の場合は position が最後尾から始まる為に表示されない
    f.write("\nYou add sentences to last of the file content with a+ mode")
    f.seek(0)
    print(f.read())