class Animal(object):
    def __init__(self, name):
        self.name = name
        print("Animal init is called")

    def breath(self):
        print(f"{self.name} is breathing")


class Dog(Animal):
    pass


class Cat(Animal):
    pass


class Bird(Animal):
    pass


pochi = Dog("pochi")
tama = Cat("tama")
print(pochi.name)
print(tama.name)
pochi.breath()
tama.breath()
# Animal の方で constructor とインスタンス変数を定義しているので、Dog と Cat はそれを継承できる
# インスタンスを生成する = constructor = __init__ と今は言われている
# Animal の方で method も定義しているので、Dog と Cat はそれを継承できる
# Dog と Cat で共有して持てる事は、superclass(Animal class)で定義して継承する事で
# Dog class Cat class でわざわざ constructor や インスタンス変数、method を定義しなくてもよくなる
