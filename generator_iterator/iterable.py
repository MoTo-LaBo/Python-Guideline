fruits = ['appel', 'lemon', 'peach']

# print(next(fruits))  # 'list' object is not an iterator
# print(iter(fruits))  # <list_iterator object at 0x109043850
fruits_iterator =  iter(fruits)
# print(next(fruits_iterator))  # appel
# print(next(fruits_iterator))  # lemon
# print(next(fruits_iterator))  # peach

# print(iter(fruits_iterator))  # <list_iterator object at 0x106fa0850>
print(id(fruits_iterator))  # 4384217168
print(id(iter(fruits_iterator)))  # 4384217168

print("=" * 50)
print(next(fruits_iterator))
print(fruits_iterator.__next__())


# print("=" * 30)
#
#
# def even(num):
#     while num != 0:
#         if num % 2 == 0:
#             yield num
#         num -= 1
#
#
# even_gen = even(10)
# print(next(even_gen))
# print(next(even_gen))
