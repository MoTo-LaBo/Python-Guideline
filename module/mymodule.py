myvariable ="This is global variable"


def myfunc():
    print("This is myfunction!!")


def anotherfunc():
    print("This is another function!!")


def _func():
    print("This is function!!")
# _ (アンダースコア)から始まる関数は、この file の中でしか使用できないという意思表示である
# python で access 制限をしてくれるわけではない
# 開発者の中ではこの _が接頭辞にあるものは、外から使うようにデザインされたものではないと共通認識される
# private function と言われるが、python program 的な観点から言うと現実的には access も import もできてしまう

if __name__ == "__main__":
    myfunc()
    anotherfunc()
    print(myvariable)
    print("This is mymodule!!")
