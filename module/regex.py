# build in module
# Regular expression (re:正規表現 通称RegEx)
# ある文字列が特定のパターンにマッチするかどうか?を判定することができる

import  re

email = "myemail@mail.com"
print("@" in email)

# このemailの文字列に' @ 'があって、@マークの後に１文字以上のアルファベットがあって' . (ドット)'がある
matched = re.search('@\w+\.', email)   # mach したら object を返して
match = re.search('@\w+\.', 'myemail@gmailecom')   # mach しなかったら None が返ってくる

print(matched)
print(match)

if matched:
    print(matched)
    print("Matchde")
else:
    print("Not found!")


# 正規表現パターン　（基本的なパターン)

# metacharacter (メタキャラクター)
# [] スクエアーブラケット
# '[abc]', ' 文字列 ' 文字列の中にabcのどれか含まれていれば match する

print(re.search('[abc]', 'apple'))
print(re.search('[abc]', 'good luck'))
print(re.search('[abc]', 'moto labo'))

# '[a-c]', ' 文字列 ' 文字列の中にabcのどれか含まれていれば match する
print(re.search('[a-c]', 'apple'))

# '[0-9]', ' 文字列 ' 文字列の中に0~9のどれか含まれていれば match する
print(re.search('[0-9]', 'apple 1'))

# ^ (ハット) 最初の文字が[ ]パターンに match する
print(re.search('^[0-9]', 'test9'))

# {n} n回リピートする ※ 最初の４文字が [ ]パターンに match するかどうか
print(re.search('^[0-9]{4}', '2021/3/31'))  # <re.Match object; span=(0, 4), match='2021'>
print(re.search('^[0-9]{4}', '20/3/31'))    # None

# {n,m} 最低 n回、 最高 m回リピートする ※ 最初の２文字 または ４文字が [ ]パターンに match するかどうか
print(re.search('^[0-9]{2,4}', '2021/3/31'))  # match
print(re.search('^[0-9]{4}', '20/3/31'))      # match

# $ 最後の文字
print(re.search('^[0-9]{2}$', '2021/3/31'))  # match 最後の２文字が数字かどうか
print(re.search('^[0-9]{4}', '20/3/3'))      # None

# * 左のパターンを0回以上繰り返す　b の前に aがあっても無くても b が存在すれば当てはまる
print(re.search('a*b', 'b'))  # match
print(re.search('a*b', 'ab'))  # match
print(re.search('a*b', 'a'))  # None : b がないのでマッチしない

# + 左のパターンを1回以上繰り返す
print(re.search('a+b', 'b'))  # None : aが無いのでマッチしない
print(re.search('a+b', 'ab')) # match
print(re.search('a+b', 'a'))  # None : b がないのでマッチしない

# ? 左のパターンを 0回か1回繰り返す
print(re.search('ab?c', 'abc'))  # match
print(re.search('ab?c', 'ac'))   # match
print(re.search('ab?c', 'ab'))   # None : c がないのでマッチしない
print(re.search('ab?c', 'bc'))   # None : a がないのでマッチしない
print(re.search('ab?c', 'abbc'))   # None : b が2以上繰り返しているのでマッチしない

# | (パイプ)　or を意味する
print(re.search('abc|012', '012'))  # match
print(re.search('abc|012', '01'))  # None

# () グループ
print(re.search('te(s|x)t', 'test'))  # match
print(re.search('te(s|x)t', 'text'))  # match

# .(ピリオド)　任意の一文字 ※ ◯（一文字）◯
print(re.search('h.t', 'hat'))  # match
print(re.search('h.t', 'hint'))  # None : 一文字ではないから

# \ (バックスラッシュ)　esc : エスケープ .(ドットはmetacharacterではない普通の文字ですよという司令)
print(re.search('h\.t', 'h.t'))  # match

# \w [a-zA-Z0-9_] : 全てのアルファベット、数字及びアンダースコア
print(re.search('h\wt', 'h_t'))  # match
print(re.search('h\wt', 'h9t'))  # match
print(re.search('h\wt', 'hit'))  # match
print(re.search('h\wt', 'h.t'))  # None
print(re.search('h\wt', 'hint'))  # None


# challenge1
pattern_dob = "^(19|20)[0-9]{2}/([1-9]|1[0-2])/([0-9]|1[0-9]|2[0-9]|3[01])$"

while True:
    dob = input("生年月日を入力して下さい(yyyy/mm/dd)")
    result = re.search(pattern_dob, dob)
    if result:
        print(f"{dob}は正しいフォーマットです")
        break
    else:
        print(f"{dob}は正しくないフォーマットです")

# challenge2
pattern_email = "^(\w|-|.)+@(\w|-|.)+\.[a-zA-Z]{2,3}$"

while True:
    email_add = input("アドレスを入力してください")
    check = re.search(pattern_email, email_add)
    if check:
        print(f"{email_add}は正しいフォーマットです")
        break
    else:
        print(f"{email_add}は正しく無いフォーマットです")