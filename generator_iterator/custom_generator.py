# range(10)
# def myrange(stop):
#     start = 0
#     while start < stop:
#         yield start  # yield を使用すると、yield が入った関数が generator になる
#         # return start  # yield を使用すると、yield が入った関数が generator になる
#         start += 1
# yield は return と同じ役割をしている


# mr = myrange(10)
# print(type(mr))
# print(mr)
# print(next(mr))
# print(next(mr))
# print(next(mr))
# print(next(mr))
# print(next(mr))
# print("end of next()")
# print(next(mr))
# print(next(mr))
# print(next(mr))
# print(next(mr))
# print(next(mr))
# print(next(mr))
# print("beginning of for loop")
#
# for i in mr:
#     print(i)

# print(next(mr))


# challenge
def even(num):
    while num != 0:
        if num % 2 == 0:
            yield num
        num -= 1


print("=" * 30)
for i in even(10):
    print(i)