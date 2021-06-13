# biult in module
# time

from functools import lru_cache
import time

# .time(): 1970/1/1 から、今現在までの秒数が表示(Unix 時間)
print(time.time())
print(time.time()/(60*60*24*365))  # 年

@lru_cache
def fib(n):
    print(f"fibonacci with {n} is running...")
    if n < 2:
        return n
    else:
        return fib(n-1)+fib(n-2)


before = time.time()
print(fib(30))
after = time.time()
print(f"recursive fibonacci took {after - before:.2f} sec.")


# .ctime() 今のローカル時間を文字列で返す
print(time.ctime())

# .localtime() 構造化データで返す ※ 時刻は構造化データで扱うと扱いやすい
locatime = time.localtime()
print(locatime)
print(locatime.tm_year)
print(f"今の時刻は{locatime.tm_year}年{locatime.tm_mon}月{locatime.tm_mday}日{locatime.tm_hour}時{locatime.tm_min}分です")
print("今の時刻は{0.tm_year}年{0.tm_mon}月{0.tm_mday}日{0.tm_hour}時{0.tm_min}分です".format(locatime))

# .sleep(secs) secs 秒だけプログラムが待機する
sec = 5
print(f"{sec}秒待って下さい")
# time.sleep(sec)


# challenge1

def timer(func):
    def inner(*args, **kwargs):
        before = time.time()
        func(*args, *kwargs)
        after = time.time()
        print(f"{func.__name__} took {after - before:.2f}sec")
    return inner

@timer
def lazy_func(sec):
    print(f"I'm working so hard...")
    time.sleep(sec)
    print(f"I'm finally done!!")


lazy_func(4)




