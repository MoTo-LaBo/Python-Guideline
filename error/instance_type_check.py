class Animal:
    def __init__(self, name):
        self.name = name

    def walk(self):
        print(f"{self.name} is walking!!")


class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking!!")


def walk_with_me(animal: Animal) -> None:
    # if type(animal) is Animal:
    # if isinstance(animal, Animal):  # isinstance 関数は、sub class の場合でもTrue で返ってくる
    method = getattr(animal, 'walk', None)
    if callable(method):
        animal.walk()
    else:
        raise TypeError(f"{type(animal).__name__}は散歩（walk）できません")


if __name__ == "__main__":
    pchi = Dog("pochi")
    walk_with_me(pchi)

