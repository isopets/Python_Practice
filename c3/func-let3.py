#引数に関数を要求する関数を定義
def calc_5_3(func):
	return func(5, 3)

#引数に足し算を行う無名関数を指定する
result = calc_5_3(lambda a, b: a + b)
print(result) #表示結果→8

#引数に引き算を行う無名関数を指定する
result = calc_5_3(lambda a, b: a - b)
print(result) #表示結果→2

#引数に掛け算を行う無名関数を指定する
result = calc_5_3(lambda a, b: a * b)
print(result) #表示結果→15

#引数に割り算を行う無名関数を指定する
result = calc_5_3(lambda a, b: a / b)
print(result) #表示結果→1.666...