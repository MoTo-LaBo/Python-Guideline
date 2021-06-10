# range(start, stop. step)
# for i in [1, 2, 3, 4, 5, 6]:
#     print(i)
# for i in range(1, 7, 1):
#     print(i)
# 数字だけループで回すときは i という変数をよく使用する

# step の default は 1
# start と step は省略できる
# for i in range(7):
#      print(i)

# program は ”0” から始まる事が多いので注意
# 0 ~ 9 (10)

# hello が10かい繰り返される
# i を使用しない場合は、＿（アンダースコア）にしておく
# _　で示すことによって、この変数はどこにも使用されないと言う事が理解できる
# for _ in range(10):
#     print("hello")

# challenge FizzBuzz game

# for i in range(1, 51):
#     if i % 3 == 0:
#         print(f"{i}Fizz")
#     if i % 5 == 0:
#         print(f"{i}Buzz")
#     if i % 15 == 0:
#         print(f"{i}FizzBuzz")

# answer
for i in range(1, 51):
    if i % 15 == 0:
        print(f"{i}FizzBuzz")
    elif i % 3 == 0:
        print(f"{i}Fizz")
    elif i % 5 == 0:
        print(f"{i}Buzz")
    else:
        print(i)
