# from .module3 import myfunc3
# もっとも使用される記述のされ方

# from ..subdir import module3
# from ..subdir.module3 import myfunc3
# 上記のような記述の仕方もできるが、..subdir にする意味がない例として

# module2 から module1 を import したい時
# from .. module1 import myfunc as module1_func
from .. import module1
def myfunc():
    print("This is myfunc from module2")


def myfunc2():
    print("This is myfunc2 from module2")
    # myfunc3()
    # module3.myfunc3()
    # myfunc3()
    # module1_func()
    module1.myfunc()