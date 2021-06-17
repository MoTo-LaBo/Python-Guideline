class Person:
    def __init__(self, name):
        self.name = name
        self.__mymethod()

    def mymethod(self):  # Baby class にオーバーライドされる事を想定していないケース
        print("Person method is called")

    __mymethod = mymethod

# def mymethod の方が呼ばれのではなく、__init__ の self.mymethod()が呼ばれてしまう。おかしなことが起こっている
class Baby(Person):
    def mymethod(self):  # 間違えてオーバーライドしてしまう。同じ名前を使用してしまう = name クラッシュ
        print("Baby method is called")
# name クラッシュ ようなことが起こらないように名前修飾を使用する __mymethod = mymethod こう記述することで
# super class でも sub class でも　mymethod を使用できる

taro_baby = Baby("Taro")
taro_person = Person("Taro")
taro_person.mymethod()
print(taro_baby.name)
taro_baby.mymethod()
print(dir(taro_baby))