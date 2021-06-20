import csv
import sys

# range 自体がgenerator

# range_nums = range(10)  # 48
range_nums = range(20)  # 48
# for i in range_nums:
#     print(i)

# list_nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  # 152
# list_nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,  14, 15, 16, 17, 18, 19]  # 216
list_nums = list(range_nums)
print(list_nums)
# for i in list_nums:
#     print(i)


# sys.getsizeof : メモリの消費量を見ることができる
print(sys.getsizeof(range_nums))  # 48
print(sys.getsizeof(list_nums))  # 152 , 216


with open("example.csv") as f:
    reader = csv.DictReader(f)
    print(sys.getsizeof(reader))
    for line in reader:
        print(line)


# generator は itreator でもある。generator は itreator の特別な形
# generatpr は大きな data を扱う時に有用。メリットが大きい
