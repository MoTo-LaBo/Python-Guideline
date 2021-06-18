# raise
# 特定の例外を発生させる事ができる
# raise <例外クラス>もしくは raise <例外インスタンス> の形を取る
# raise ValueError / raise ValueError()
# 例えば try except をテストする際に使用する

try:
    # TODO 後で削除する
    raise ValueError()
except ValueError:
    print("Do something")
    raise

# 実際の開発では、いちいち code を打ち込むのは手間なので raise を使用して test する
