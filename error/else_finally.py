def split_bill(price):
    num = input("何人で割り勘しますか？")
    try:
        each = price / int(num)
    except ZeroDivisionError as e:
        print("0で割ることはできません。正しい値を入力して下さい")
        print(e)
    except ValueError:
        print("数値を入力して下さい")
    else:
        print(f"一人{each}円です")
    finally:
        print("ご利用有難うございます")
# finally のタイミングは複雑なので、必ず簡単な code で試すこと。挙動を理解できないと bug の元になる！！


if __name__ == "__main__":
    split_bill(10000)