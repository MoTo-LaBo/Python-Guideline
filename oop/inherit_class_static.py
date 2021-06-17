import time

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def create_from_dob(cls, name, year, month, date):  # ファクトリーmethod: classmethod を定義してインスタンスを作成する
        today = time.localtime()
        age = today.tm_year - year - ((today.tm_mon, today.tm_mday) < (month, date))
        return cls(name=name, age=age)
        # tuple の比較演算とブーリアンを上手く組み合わせる
        # (today.tm_mon, today.tm_mday) = True = 1, (month, date) = False = 0

        # if (today.tm_mon, today.tm_mday) < (month, date):  # tuple の比較演算を使用すると月日の比較がしやすくなる: (2, 3) < (2, 2) = True
        #     age = today.tm_year - year - 1
        # else:
        #     age = today.tm_year - year  # 上記の記述の仕方で一行に code をまとめることができる

    @staticmethod
    def create_from_dob2(name, year, month, date):
        today = time.localtime()
        age = today.tm_year - year - ((today.tm_mon, today.tm_mday) < (month, date))
        return Person(name=name, age=age)


class Baby(Person):
    pass



john = Baby('john', 20)
emma = Baby.create_from_dob('Emma', 1989, 4, 3)
emily = Baby.create_from_dob2('Emily', 1999, 12, 3)
print(john.name)
print(emma.name)
print(emma.age)
print(emily.age)
print(type(john))  # <class '__main__.Baby'> class から作成されたインスタンス
print(type(emma))  # <class '__main__.Baby'> class から作成されたインスタンス
print(type(emily))  # <class '__main__.Person'> @staticmethod は、Baby classで継承しても Person のまま返してしまう
# bug の元になってしまうので、# ファクトリーmethod: classmethod を定義してインスタンスを作成する時には
# @staticmethod は使用しない事
