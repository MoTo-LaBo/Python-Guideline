class Duck: # docstring は必ず書きましょう！！！　見た時にわかるようにする。英語で記述する事
    """
    This a class for Duck

    Attributes:
        name (str): the name of duck

    Method:
        walk: print ***
        quack: print ***
        fly: print ***
    """
    def __init__(self, name):
        """
        The constructor for Duck clask
        :param name: the name of the duck
        """
        self.name = name

    def walk(self):
        print("walking,,,")

    def quack(self):
        print("quack quack...!")

    def fly(self):
        print("Whee!!")


class Penguin:
    def __init__(self, name):
        self.name = name

    def walk(self):
        print("walking,,,")

    def quack(self):
        print("quack quack...??")

    def swim(self):
        print("Swimming!")


def walk_and_quack(duck):
    print(f"I'm {duck.name}")
    duck.walk()
    duck.quack()


if __name__ == "__main__":
    print(help(Duck))
    donald = Duck("Donald")
    scrooge = Duck("Scrooge")
    daisy = Duck("Daisy")
    pingu = Penguin("Ping")
    # donald.walk()
    # donald.quack()
    # pingu.walk()
    # pingu.quack()
    # walk_and_quack(donald)
    # walk_and_quack(pingu)
    duck_list = [donald, pingu, scrooge, daisy]
    for duck in duck_list:
        walk_and_quack(duck)