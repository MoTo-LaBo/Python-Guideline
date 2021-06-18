import os, sys
x = 1
y = 2
print(x, y, z)


# 基本的には、flake8 を通しておけばOK
# あとはチームによって臨機応変に対応する
# style guide にそって記述することによって code の共有、アルゴリズムの理解などメリットがたくさんある
# 読むこと前提で code は、記述すること！！！


# pycodestyle
# style check をしてくれるターミナルで操作
# $ pip install pycodestyle

# $ pycodestyle <file名>
# check_tool.py:1:10: E401 multiple imports on one line

# $ pycodestyle --show-source <file名>
#　import os, sys　　問題の場所を表示してくれる
         # ^

# $ pycodestyle --show-source --show-pep8 <file名>
# $ こういう記述の仕方はOKですよ！という例を表示してくれる
# import os, sys
#          ^
#     Place imports on separate lines.
#
#     Okay: import os\nimport sys
#     E401: import sys, os
#
#     Okay: from subprocess import Popen, PIPE
#     Okay: from myclas import MyClass
#     Okay: from foo.bar.yourclass import YourClass
#     Okay: import myclass
#     Okay: import foo.bar.yourclass

# $ pycodestyle --statistics -qq check_tool.py
# 問題点が何個あるのか表示してくれる ※ -qq (クワイエット): 無駄な表示をなくしてくれる


# Python の Linter
# Lojical Lint -> pyflakes : 使用されていないモノを指摘してくれる

# $ pip install pyflakes

# $ pyflakes check_tool.py
# check_tool.py:1:1 'os' imported but unused
# check_tool.py:1:1 'sys' imported but unused
# check_tool.py:4:13 undefined name 'z'


# pycodestyle と pyflakes の機能が合わさったのが flake8
# $ pip install flake8

# $ flake8 check_tool.py
# check_tool.py:1:1: F401 'os' imported but unused
# check_tool.py:1:1: F401 'sys' imported but unused
# check_tool.py:1:10: E401 multiple imports on one line
# check_tool.py:4:13: F821 undefined name 'z'
# check_tool.py:15:1: E265 block comment should start with '# '
# check_tool.py:16:10: E114 indentation is not a multiple of 4 (comment)
# check_tool.py:16:10: E116 unexpected indentation (comment)
# check_tool.py:54:1: W391 blank line at end of file


# flake8 より厳しい linter: pylint
# $ pip install pylint

# $ pylint check_tool.py
