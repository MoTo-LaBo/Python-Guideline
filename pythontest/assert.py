# assert
a = 1
b = 1
# a + b == 2
print(a + b)

assert a + b == 2, "a + b is equal to 2!"


def power(base, exp):
    return base ** exp


assert power(3, 2) == 9, "3 ** 2 must be 9"
# どういった testケース にするのかは、事前にチームで話し合って test ケース一覧を作成しておく
# 一般的には関数と test ケースは別々のfileに記述する。 test script という file を作成して test code を記述していく

