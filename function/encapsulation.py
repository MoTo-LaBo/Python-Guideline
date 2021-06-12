# encapsulation (カプセル化): 外からアクセルができないようにする(情報隠蔽)
# nested function もカプセル化の一種

def casino_entrance(age, min_age=21):
    if age < min_age:
        print(f"{min_age}歳未満の為入場できません")
        return

    def inner_casino_entrance():
        print("ようこそカジノへ")

    return inner_casino_entrance()


casino_entrance(28)
# inner_casino_entrance (main program)には、casino_entrance を通さないと access できない
# 外側の program (if) を通らないと中の情報は取ってこれないので、安全に program 実行できる
# 上記のような記述をする事により機能を分担できる。 それぞれの program に専念できるメリットがある(responsibilityの分離)
# responsibilityの分離 が nested function の基本的な考え方
