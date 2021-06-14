# Person class (パーソンクラス)
# 変数・関数は snake_case: 全て小文字またはアンダースコア
# class名は、(CamelCase:キャメルケース)を使用する。頭文字を大文字
class Person(object):  # (object)は記述してもしなくてもいい。記述しなくても default で(object)がつく
    # constructor :実際は __init__ が (__new__)を呼んでいて、__new__ = constructor という
    # インスタンスを生成する = constructor = __init__ と今は言われている
    def __init__(self, name, age, gender):  # Person (人) , self = instance(インスタンス自身)
        self.name = name
        self.age = age
        self.gender = gender

# python では class名( )とすると __init__ が呼ばれる
# 関数みたいに（引数）を渡しているわけではないので、そこの違いを理解する
john = Person("John", 28, 'male')
taro = Person("Taro", 18, 'male')
emma = Person("Emma", 40, 'female')

print(john.name)
print(john.age)
print(john.gender)