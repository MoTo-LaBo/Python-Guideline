# EAFP (easier of ask for forgiveness than permission)
# 「 許可をもらうより許してもらう方が楽 」
# 有効であると仮定して code を書いていて、その仮定が誤っていたら外例を出す
# これにより手早く code を書く事が可能
# try except を多く書くことになるが、それ自体は悪い事ではない
# try execpt を入子上に記述していく事になるが…　できれば避けるべき code だが…　
# それぞれの関数で try except をしていたらしょうがない現象（こうならざるおえない）
# 何処で error が出たか分かりずらいのでその時に traceback module を使用する

import traceback  # 元々入っている built in module

bill = {'burger': 500, 'pasta': 1400, 'fries': 300, 'egg': 200}


def split_bill(price):
    num = input("割り勘する人数を入力して下さい")
    try:
        each = price / int(num)
    except ZeroDivisionError:
        print("0以外の数字を入力して下さい")
    else:
        print(f"一人{each}円です")


def check(bill):
    total_bill = sum(bill.values())
    try:
        split_bill(total_bill)
    except ValueError:
        traceback.print_exc()  # あくまでも traceback を表示してくれているだけで、program は問題なく動いている
        print("エラーが出ました。やり直して下さい")


if __name__ == "__main__":
    bill = {'burger': 500, 'pasta': 1400, 'fries': 300, 'egg': 200}
    check(bill)
    print("プログラムは問題なく実行されました")  # デバッグが楽になる.
# デバッグが楽になるが、あくまでも開発中のデバックの時に使用するモノ。最後はコメントアウトしておく
# error は programing していく上ではうまく付き合っていかないといけないモノ。悪いものではない！！
# error のおかげで、改善できるし、間違いに気づける。 traceback を上手く活用していく
# 最終的に世の中に出す code はクラッシュさせるわけにはいかないので、あらゆる例外を含めハンドリングしていく必要がある
# 基本的には、あらゆる例外が出ないようにUI(user interface)か他の所で制御していく
# どうしても例外は出てきてしまうので、そういう場合は code （try except）でキャッチしてクラッシュしないように対応する事
# まずは error が出たらしっかりと error の内容を理解できるようにしておく事。そこが一番大切
