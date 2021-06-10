# 数値型（Numeric）: integer(整数),float(小数),complex(複素数)

# int (integer:整数)-3,-2,-1,0,1,2,3,100
print(type(1))

# float (浮動小数点)
# ピッタリ 0.1 は作れない。少し大きくなってしまう
print(type(0.1))
print(0.1 + 0.1 + 0.1)  # 0.3 より少し大きい

# Numeric Operator (数値演算子)
# 四則演算
print(1 + 0.4)
print(1 - 0.4)
print(2 * 3)
print(1 / 2)
print(5*6 - 3/6)

result = 1 + 1.0
print(type(result))
print(f"type of result:{result} is {type(result)}")

# その他の演算
# floor division
print(14 // 3)
# modulo (剰余、あまり)
print(14 % 3)
# exponentiation (冪乗)
print(2 ** 3) # 2の3乗

hit_point = 100
attack_point = 40.3
print(100 - 40.3)
remain = hit_point - attack_point
print(f"remain hit point is {remain}")

# augmented assignment +=,-=,*=,/=
a = 1
# a = a + 1
a += 1 # a = a + 1　と同じ
print(a)