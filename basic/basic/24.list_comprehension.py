# リスト内包表記 (list comprehension)

# for loop 記述 (0, 1, 4, 9, 16, 25, ... 二乗)
# square_list = []
# for i in range(10):
#     square_list.append(i ** 2)
#
# print(square_list)

# list comprehension ※ リスト内包表記でかける codeは結構ある
square_list = [i ** 2 for i in range(10)]
print(square_list)

# i が偶数の時だけ計算をする（2で割ってあまりが0の時）
even_square_list = [i ** 2 for i in range(10) if i % 2 == 0]
print(even_square_list)