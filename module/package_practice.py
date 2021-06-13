# これが一番安全で推奨されている import の記述の仕方
# よほど、import 後の名前が長く無いければこれを使用した方が安全

# import myfirstpackage.module1
# import myfirstpackage.subdir.module2
#
# myfirstpackage.module1.myfunc()
# myfirstpackage.module2.myfunc()


# from myfirstpackage.subdir.module2 import myfunc
# myfunc()

# 関数名を直接してして import する事はほとんどない ※ よほど他の関数名がかぶらない自信が無い限り使わない
# from myfirstpackage.module1 import myfunc
# myfunc()
# import myfirstpackage
#
# myfirstpackage.myfunc()

# from myfirstpackage.subdir import *
# myfunc()
# myfunc2()

import myfirstpackage.subdir.module2

myfirstpackage.subdir.module2.myfunc2()