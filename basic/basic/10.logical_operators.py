# 論理演算子 (logical operators)

# and , or , not
a = 1
b = 1
c = 10
d = 100
print(a == b and c > d)  # False : and (かつ)
print(a == b or c > d)  # True : or (もしくは)
print(not a == b)  # False : not (ではない)

# practice
# age = 10
# stature = 110
# print(age <= 10 and stature <= 110)

# answer
age = 13
height = 140
print(age > 10 and height > 110)

# practice
# master = "retention"
# visa = "retention"
# experience = 5
# print(master == visa or experience <= 5)

# answer
master = False
job_experience = 6
print(master or job_experience > 5)
