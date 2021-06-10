# リスト(list): 複数のオブジェクトを順序づけて保存するデータ型
# []で括って、,(カンマ)で各オブジェクトを区切る
# fruis = ['apple', 'peach', 'melon', 'grapes']
# index　　　0　　 |　　1　　|　　2　　　|　  3　 |
# index    -4　　 |　 -3   |   -2    |   -1   |

# hetro_list = ['string', 1, 3.4, True, fruis]
#
# print(hetro_list)
# print(fruis[0])
# print(fruis[-1])
#
# print(hetro_list[-1][-1])
# #    |   fruis      | grapes |
#
# print("hello world"[3])

fruis = ['apple', 'peach', 'melon', 'grapes']
# index　　　0　　 |　　1　　|　　2　　　|　  3　 |
# index    -4　　 |　 -3   |   -2    |   -1   |

hetro_list = ['string', 1, 3.4, True, fruis]

# .append: 新しいオブジェクトを追加できる(list で一番使用するメソッド)
print(fruis)
fruis.append("banana")
print(fruis)

# .insert: 指定したindexに指定したオブジェクトを追加する
print(fruis)
fruis.insert(3, "lemon")
print(fruis)

# .remove: マッチした最初のオブジェクトを除く
print(fruis)
fruis.remove('peach')
print(fruis)

# .sort:   昇順に並び替える(abc順)
fruis.sort()
print(fruis)

# .sort: 降順に並び替える(cba順)
fruis.sort(reverse=True)
print(fruis)

# len():  リストの要素数を取得する (length:長さ)
# 引数に含まれる、要素数を表示
print(len(fruis))
print(len("hello world"))








