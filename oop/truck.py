# challenge : Car class の継承
# from car import Car
#
# class Truck(Car):
#     def __init__(self, model_name, mileage, manufacturer, maximum, load_capacity):
#         super().__init__(model_name, mileage, manufacturer)
#         self.maximum = maximum
#         self.load_capacity = load_capacity
#
#     def load(self, loading):
#         new_load_capacity = self.load_capacity + loading
#         if self.maximum < new_load_capacity:
#             print(f"最大積載量{self.maximum}をオーバーしました。現在の積載量{new_load_capacity}")
#         else:
#             print(f"現在の積載量{new_load_capacity}")
#
#
# jimny = Car("jimny", 20, 'suzuki')
# elf = Truck("ELF", 12, 'isuzu', 4000, 2000)
#
#
# if __name__ == "__main__":  # 他の script から import された時に、下記が実行されないようにする為
#     print(jimny.model_name)
#     print(elf.model_name)
#     print(elf.manufacturer)
#     elf.load(1000)
#     elf.load(1000)

# answer
from car import Car


class Truck(Car):
    def __init__(self, model_name, mileage, manufacturer, max_loading):
        super().__init__(model_name, mileage, manufacturer)
        self._maximum = max_loading
        self._loadings = 0  # 最初は何も積載していない前提

    def load(self, weight):
        if weight > 0:
            # 荷物をつむ
            print(f"{weight}tの荷物を積みました")
            self._loadings += weight
        else:
            # 荷物をおろす
            if self._loadings <= -weight:
                print(f"{self._loadings}t全ての荷物を降ろしました")
                self._loadings = 0
            else:
                print(f"{-weight}tの荷物を降ろしました")
                # weight は負の値なので、+=で足し算をする
                self._loadings += weight
        print(f"現在の積載量は{self._loadings}tです")

        if self._loadings > self._maximum:
            print(f"最大積載量{self._maximum}tを超えました")


jimny = Car("jimny", 20, 'suzuki')
elf = Truck("ELF", 12, 'isuzu', 10)

if __name__ == "__main__":
    elf.gas()
    elf.load(5)
    elf.load(-3)
    elf.load(10)
    elf.load(-30)
# _ (アンダースコア)忘れ。nonpublic なインスタンス変数である事を明示する