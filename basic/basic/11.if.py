# if 文 条件文

# if (条件文) :
# 〇〇〇〇(処理内容) 条件がTrueの時実行される
# else :
# 〇〇〇〇(処理内容) 条件がFalseの時実行される

# アルコールの摂取年齢を用いた if 文
age = -20
age_alcohol = 21
if age >= age_alcohol:  # もし〜であれば実行
    print("You can drink beer!")
else:  # さもなければ〜（上記がFalseであれば）
    print("You are too young to drink beer")

age_drive = 18
if age >= age_alcohol:  # もし〜であれば実行
    print("You can drink beer!")
elif age <= age_drive:  # そうではないんだけれど、もし〜だったら
    print("You cannot even drive!")
else:
    print("You are not allowed to drink beer but you can drive only if you have a driver's license")

if not 0 < age < 120:
    print("The value is invalid!!")

# challenge1.もし残高(balance)が引き出し額(withdraw)より大きければ、balanceを更新し、そうでなければ引き出せないATMを作る
# balance = 1000
# withdraw = 1000000
#
# if balance >= withdraw:
#     print("balance update")
# else:
#     print("not withdraw")
# answer
balance = 3000000
withdrawal = 1200000
# if balance > withdrawal:
#     # balance = balance - withdrawal
#     balance -= withdrawal
#     print("You new balance is {}".format(balance))
# else:
#     print("You don't have money")

# challenge2.上記1に加えて、引き出し額(withdraw)の上限を１００万円に設定し、上限を超えて引き出そうとすると引き出せないATM
# upper_limit = 1000000
#
# if balance > withdrawal:
#     balance -= withdrawal
#     print("You new balance is {}".format(balance))
# elif withdrawal >= upper_limit:
#     print("You don't ")
# else:
#     print("You don't have money")

# answer
withdrawal_limit = 1000000

if withdrawal > withdrawal_limit:
    print("The withdrawal limit is {}".format(withdrawal_limit))
elif balance > withdrawal:
    balance -= withdrawal
    print("You new balance is {}".format(balance))
else:
    print("You don't have money")
