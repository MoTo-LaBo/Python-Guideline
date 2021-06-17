class Animal(object):
    def __init__(self, name):
        self.name = name
        print("Animal init is called")

    def breath(self):
        print(f"{self.name} is breathing")


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name=name)  # sub class では、super class の init を１行で呼べる
        print("Dog init is called")
# Dog class に init がある場合は、superclass(親クラス)の init は呼ばれない


pochi = Dog("pochi")
print(pochi.name)
pochi.breath()
# Animal の方で constructor とインスタンス変数を定義しているので、Dog と Cat はそれを継承できる
# インスタンスを生成する = constructor = __init__ と今は言われている
# Animal の方で method も定義しているので、Dog と Cat はそれを継承できる
# Dog と Cat で共有して持てる事は、superclass(Animal class)で定義して継承する事で
# Dog class Cat class でわざわざ constructor や インスタンス変数、method を定義しなくてもよくなる