# challenge
class Car(object):

    def __init__(self, model_name, mileage, manufacturer):
        self.model_name = model_name
        self.mileage = mileage
        self.manufacturer = manufacturer

    def gas(self):
        # print(f"{self.manufacturer}の{self.model_name}(燃費:{self.mileage}/km)アクセル全開！！")
        print("{0.manufacturer}の{0.model_name}(燃費:{0.mileage}/km)アクセル全開！！".format(self))

    def brakes(self):
        # print(f"{self.manufacturer}の{self.model_name}(燃費:{self.mileage}/km)アクセル全開！！")
        print("{0.manufacturer}の{0.model_name}(燃費:{0.mileage}/km)ブレーキ".format(self))


jimny = Car("jimny", 20, 'suzuki')
wrangler = Car("WRANGLER", 18, 'jeep')
model10 = Car("model10", 30, 'tesla')


if __name__ == "__main__":  # 他の script から import された時に、下記が実行されないようにする為
    print(jimny.mileage)
    wrangler.gas()
    model10.brakes()