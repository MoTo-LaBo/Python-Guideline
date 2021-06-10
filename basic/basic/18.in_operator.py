# in 演算子
# fruits = ['apple', 'peach', 'grapes', 'banana']
# print('apple' in fruits)
# #     object  in  list　英語の表記そのまま
#
# print('lemon' not in fruits)
#
# print('h' in  'hello')

# challenge
fruits = ['apple', 'peach', 'grapes', 'banana']

favorite = input("好きなフルーツはなんですか？")
if favorite in fruits:
    print("{}ですね。さしあげますよ".format(favorite))
    fruits.remove(favorite)
else:
    print("{}ですね。仕入れました!".format(favorite))
    fruits.append(favorite)
print("今あるフルーツは{}こちらです".format(fruits))
