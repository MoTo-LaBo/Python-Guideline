# getter setter
# なんでそのうような事をするのか？
# age は歳で - の値は入らない。入れようとすれば入ってしまうので、それを防ぐ為
# 裏で method を動かして、〜であったら値をいれないというようなバリデーションを持たせる事ができる
# getter setter を使用しているという事は、直接値を取ってくる事を想定していない
# なので age 変数は _age として nonpublic と他の開発者にわかるように明示する
# 気おつけなければいけないことは、 変数は _age 外からアクセスできないわけではない
# 変数は _age には、どんな値でも入れることができるし、外からアクセスもできる

class Person(object):

    def __init__(self, name, age):
        self.name = name
        self._age = age  # age 変数は nonpublic

    @property
    def age(self):
        print("get_age called!!")
        return self._age

    @age.setter
    def age(self, age):
        print("set_age called!!")
        if age < 0:
            print("0以上の値を入れて下さい")
        else:
            self._age = age

    # 基本は上記の書き方が実務でも使用さている。pythonic 「 Python らしい、シンプルで読みやすいコードの書き方 」
    # age = property(get_age, set_age)  # built in 関数: property object

john = Person("john", 10)
print(john.age)



# print(john.name)
# print(john.age)
# print(john.get_age())  # やっている事は、　print(john.age) と変わらない
# john.age = -10  # 値を set する方を setter
# john.set_age(-20)
# print(john._age)  # 値を読み取る方を getter
