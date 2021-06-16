class MyClass:

    classmethod_count = 0

    def myethod(self):
        print("This is normal method! from{}".format(self))

    @staticmethod
    def mystaticemethod():
        print("This is staticmethod")

    @classmethod
    def myclassmethod(cls):  # 第一引数に cls が入る。class の情報が cls として入る　　　　
        cls.classmethod_count += 1
        print(f"This is classmethod now the count is {cls.classmethod_count}")


c = MyClass()
c.myethod()
MyClass.mystaticemethod()
MyClass.myclassmethod()  # classmethod も第一引数に自動で cls が入る ※ default で入っているので何も記述しないくていい
c.myclassmethod()

# staticmetod や classmethod は外から使用される事を想定していない method である
# staticmetod や classmethod は method名に ＿（アンダースコア）をつけることが多くなる
# class 内で使用する便利関数の場合は、_(アンダースコア)を付けた方が分かりやすい

