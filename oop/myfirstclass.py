# Person class (パーソンクラス)
# 変数・関数は snake_case: 全て小文字またはアンダースコア
# class名は、(CamelCase:キャメルケース)を使用する。頭文字を大文字
# (object)は記述してもしなくてもいい。記述しなくても default で(object)がつく
# constructor :実際は __init__ が (__new__)を呼んでいて、__new__ = constructor という
# インスタンスを生成する = constructor = __init__ と今は言われている

class Person(object):

    num_legs = 2  # class 変数: class に紐付いている変数
    count = 0

    def __init__(self, name, age, gender):  # Person (人) , self = instance(インスタンス自身)
        self.name = name
        self.age = age
        self.gender = gender
        Person.count += 1
    # メソッド間は一行開ける
    def walk(self):
        print(f"{self.name} is walking...with {Person.num_legs} legs!!")

    def run(self):
        print(f"{self.name} is running...with {Person.num_legs} legs!!")


# python では class名( )とすると __init__ が呼ばれる
# 関数みたいに（引数）を渡しているわけではないので、そこの違いを理解する
# name, age, gender は、属性
john = Person("John", 28, 'male')
print(Person.count)
taro = Person("Taro", 18, 'male')
print(Person.count)
emma = Person("Emma", 40, 'female')
print(Person.count)
# emma = Person((slef:emma),"Emma", 40, 'female') image はこんな感じ


# インスタンス変数
# インスタンス名から「.」に続けてアクセスできる
print(john.name)
print(f"変更前のjohn{john.age}")
print(john.gender)
john.age = 29  # 上書き
print(f"変更後のjohn{john.age}")

# インスタンスメソッド
john.walk()  # default で第一引数に self (john)が入っている
emma.walk()
john.run()
emma.run()

# class 変数：class 変数はインスタンス間で共有可能
print(john.num_legs)
print(taro.num_legs)

print(Person.num_legs)
print("Person.num_legs = 3 を実行")  # class名.<値> 変数はインスタンス間で共有可能
Person.num_legs = 3
print(john.num_legs)
print(taro.num_legs)
print(emma.num_legs)
print("joho.num_legs = 4 を実行")  # インスタンス名.<値>　だと、インスタンス名しか更新されない
john.num_legs = 4                 # bug の元になるのでこのような事はしない
print(john.num_legs)              # そもそも class 変数を インスタンス変数で更新する事自体がおかしい　
print(taro.num_legs)
print(emma.num_legs)