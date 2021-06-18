def split_bill(price):
    num = input("何人で割り勘しますか？")
    try:
        each = price / int(num)
    except ZeroDivisionError as e:
        print("0で割ることはできません。正しい値を入力して下さい")
        each = price
        print(e)
    except ValueError:
        print("数値を入力して下さい")
        each = price
    print(f"一人{each}円です")


if __name__ == "__main__":
    split_bill(10000)