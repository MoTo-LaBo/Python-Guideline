fruits_colors = {'apple': 'red', 'lemon': 'yellow', 'grapes': 'purple'}

# print(fruits_colors['peach'])
# dictionary にない key の場合 error になってしまう
if 'peach' in fruits_colors:
    print(fruits_colors['peach'])
else:
    print('the key is not found')

# .get() ※ dictionary には .get() という method がある。安全に簡単に value(値)取得できる
# value(値)をとってくる時が、ユーザーからの場合はよく使用する。errorになる事を防ぐため
# 安全な code を書くことができる

# fruit = input("フルーツの名前を指定してください")
# print(fruits_colors.get(fruit, 'Nothing'))

# .update()
# dictionary どうしを結合する事ができる
fruits_colors2 = {'peach': 'pink', 'kiwi': 'green'}
fruits_colors.update(fruits_colors2)
print(fruits_colors)

