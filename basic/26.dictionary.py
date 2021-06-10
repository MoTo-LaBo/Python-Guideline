# dictionary: キーと値の組み合わせを複数保持するデータ型
# python では、dictionary は必須。かなり使用頻度が高い

fruits_colors = {'apple': 'red', 'lemon': 'yellow', 'grapes': 'purple'}
#               |  key  : value | |  key  : value | |  key  : value |
# : (コロン)の後ろは、" "(スペース)１つ開けることが良いとされている


# list や tuple は index を指定していたが…
# dictionary は、key('apple')を指定する事によってvalue('red')をとってくる事ができる
# dictionary は、順番を保持しない。書かれた順番は関係ないので注意
print(fruits_colors['apple'])

fruits_colors['peach'] = 'pink'
print(fruits_colors)


# どんな object も入れることができる。(integer,string,float,list,dictionary,etc...)
dict_sample = {1: 'one', 'two': 2, 'three': [1, 2, 3], 'four': {'inner': 'dict'}}
print(dict_sample)
# key として使用するものは、値をとってくるものなので文字列になる事がほとんど
# value は現場でも色々な object を入れる事が多い

print(dict_sample['four']['inner'])
colors = {}
colors[1] = 'blue'
colors[0] = 'red'
colors[2] = 'green'
print(colors)


# .keys() .value() ※ default では、key が取得される
# for x in fruits_colors:
#     print(x)

# .items() ※ この .items がよく使用される！！
# key と value を tuple で返して、unpack する
for fruit, color in fruits_colors.items():
    print(f"{fruit} is {color}")







