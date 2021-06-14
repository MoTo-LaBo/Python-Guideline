# これが一番安全で推奨されている import の記述の仕方
# よほど、import 後の名前が長く無いければこれを使用した方が安全

# import myfirstpackage.module1
# import myfirstpackage.module2
#
# myfirstpackage.module1.myfunc()
# myfirstpackage.module2.myfunc()


# from myfirstpackage import module1, module2
# module1.myfunc()
# module2.myfunc()


# 関数名を直接してして import する事はほとんどない ※ よほど他の関数名がかぶらない自信が無い限り使わない
# from myfirstpackage.subdir.module2 import myfunc
# myfunc()

# __init__.py が有っても無くても、package_practice の scriptは何も影響は受けない

# import myfirstpackage
# myfirstpackage.myfunc()


# from myfirstpackage.subdir import *
# myfunc()
# myfunc2()

# 基本的のは、絶対インポートを使用する(absolute import)
# 相対インポート(relative import)は分かりにくいので
import myfirstpackage.subdir.module2

myfirstpackage.subdir.module2.myfunc2()
