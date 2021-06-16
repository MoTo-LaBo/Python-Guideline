# join 各文字列を”〇〇”指定したもので繋いでくれる
txet = " ".join(["Hi", "My", "name", "is", "John"])
print(txet)


# split join の逆をしてくれる
text2 = "Hi My name is John".split()
print(text2)

filename = "sample.py"
print(filename.split(".")[0])