#関数を定義
def mul_func(a, b): return a * b
def add_func(a, b): return a * b

#引数に関数を要求する関数を定義
def calc_5_3(func):
	return func(5, 3)

#
引数に関数を指定する
result = calc_5_3(mul_func)
print(result) # 表示結果→15

#引数にほかの関数を指定する
result = calc_5_3(add_func)
print(result) # 表示結果→8