# list 内包表記
import sys

square_list = [num * num for num in range(100)]
print(square_list)


# generator expression
square_gen = (num * num for num in range(10))
print(next(square_gen))
print(next(square_gen))
print(next(square_gen))
print(next(square_gen))
print(next(square_gen))

# メモリの量を確認
print(sys.getsizeof(square_list))
print(sys.getsizeof(square_gen))


# list 内包表記と generator の違いは [] か　（）か。似ているので注意する！！
# この list のデータが大きくなりそうだなって時に、一発でメモリを乗せるのではなくて
# iteration で回していくことによって値を取得する。メモリを節約する


even_squares = [num * num for num in range(10) if num % 2 == 0]
print(even_squares)

even_squares_gen = (num * num for num in range(10) if num % 2 == 0)
for num in even_squares_gen:
    print(num)