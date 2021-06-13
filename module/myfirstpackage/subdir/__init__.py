from .module2 import *
__all__ = ['myfunc2']

# Relative import: 相対インポート
# from.<package/module>import xxx
# 「.」: カレントディレクトリ
# 「..」: 親ディレクトリ
# relative imoprt の場合は、import <> の形ではなくて、from <> import <>の形をとる