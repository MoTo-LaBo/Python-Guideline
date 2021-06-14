# challenge
# class Acconunt(object):
#
#     count = 0
#
#     def __init__(self, balance, name):
#         self.balance = balance
#         self.name = name
#         Acconunt.count += 1
#
#     def withdraw(self, debit):
#         while True:
#             if self.balance < debit:
#                 print(f"引き落とし額{debit}円 :残高が足りません :残高{self.balance}円です")
#                 break
#             else:
#                 self.balance -= debit
#                 print(f"{self.name}さんの口座番号は[{self.count}] :引き落とし額{debit}円 :残高は{self.balance}円です")
#                 break
#
#     def deposit(self, payment):
#         self.balance += payment
#         print(f"{self.name}さんの口座番号は[{self.count}] :入金額{payment}円 :残高は{self.balance}円です")
#
#
# john = Acconunt(1000, 'john')
# print(john.name)
# print(Acconunt.count)
# print(john.balance)
# john.deposit(1100)
#
# taro = Acconunt(3000, 'taro')
# print(taro.name)
# print(Acconunt.count)
# print(taro.balance)
# taro.withdraw(3500)
#
# emma = Acconunt(2000, 'emma')
# print(emma.name)
# print(Acconunt.count)
# print(emma.balance)
# emma.deposit(2000)
# emma.withdraw(3000)

# answer
# class Account:
#
#     count = 0
#
#     def __init__(self, balance, name):
#         self.name = name
#         self.balance = balance
#         self.account_number = Account.count
#         self.show_balance()
#         Account.count += 1
#
#     def withdraw(self, price):
#         if price <= self.balance:
#             self.balance -= price
#             self.show_balance()
#         else:
#             print(f"残高({self.balance}円)が足りません")
#
#     def deposit(self, price):
#         self.balance += price
#         self.show_balance()
#
#     def show_balance(self):
#         # print(f"{self.name}の残高は、{self.balance}円です")
#         print("{0.name}(口座番号:{0.account_number})の残高は、{0.balance}円です".format(self))
#
#
# myaccount = Account(name="my account", balance=1000)
# print(myaccount.name)
# print(myaccount.balance)
# myaccount.withdraw(200)
# myaccount.deposit(1000)
# myaccount.withdraw(2000)
#
# youraccount = Account(name="your acconut", balance=2000)
# youraccount.deposit(8000)


# After correction
class Acconunt(object):

    count = 0

    def __init__(self, balance, name):
        self.balance = balance
        self.name = name
        self.acconunt_number = Acconunt.count
        self.show_balance()
        Acconunt.count += 1

    def withdraw(self, price):
        if self.balance < price:
            print(f"引き落とし額{price}円 :残高が足りません :残高{self.balance}円です")
        else:
            self.balance -= price
            print(f":引き落とし額{price}円")
            self.show_balance()

    def deposit(self, price):
        self.balance += price
        print(f":入金額は{price}円です")
        self.show_balance()

    def show_balance(self):
        print(f"{self.name}さんの口座番号は[{self.acconunt_number}] :残高は{self.balance}円です")


john = Acconunt(1000, 'john')
john.withdraw(500)

taro = Acconunt(3000, 'taro')
taro.withdraw(1700)
taro.withdraw(2000)

emma = Acconunt(2000, 'emma')
emma.deposit(3000)
emma.withdraw(3000)