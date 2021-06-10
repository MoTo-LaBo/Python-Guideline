# set(セット): sets 重複しないリスト

# 重複しているので、勝手に apple が削除される
# list と違って、オーダーを持たない。index を指定できない
fruits = {'apple', 'peach', 'lemon', 'grapes', 'apple'}
print(len(fruits))