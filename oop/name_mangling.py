class Account:

    def __init__(self, balance):
        self.__balance = balance  # 外からアクセスして欲しくなければ _ (アンダースコア)は付ける
                                 # 実際は python 自体にはそのような機能はない。変更しようと思えばできてしまう
    def deposit(self, amount):
        self.__balance += amount
        self.show_balance()

    def withdraw(self, amount):
        if self.__balance < amount:
            print("残高が足りません")
        else:
            self.__balance -= amount
            self.show_balance()

    def show_balance(self):
        print(f"残高は{self.__balance}円です")


myaccount = Account(10000)
print(dir(myaccount))  # '_Account__balance' 名前修飾されてしまう。__balance ではアクセスできなくなる
myaccount.deposit(1000)
myaccount.withdraw(3000)
myaccount.__balance = -10000  # 新たな balance が作成される：基本的にはこのような作成の仕方はしない！！
print(myaccount.__balance)  #　-10000：基本的にはこのような作成の仕方はしない！！
myaccount.show_balance()  # 残高は8000円です と表示される。_Account__balance' 名前修飾の balance だから
print(dir(myaccount))  # '__balance',が追加された：基本的にはこのような作成の仕方はしない！！
# 上記のような記述はしない。python にはそのような事を防ぐアクセス制御はないので、作成しようと思えば作成できてしまうので注意するように！

