class MyClass:

    def myethod(self):
        print("This is normal method! from{}".format(self))

    @staticmethod
    def mystaticemethod():
        print("This is staticmethod")



c = MyClass()
c.myethod()
MyClass.mystaticemethod()