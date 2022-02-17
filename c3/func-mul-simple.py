
#たし算を行うだけの関数を定義
def add(a, b):
	return a + b

#引き算を行うだけの関数を定義
def sub(a, b):
	return a - b

#掛け算を行うだけの関数を定義
def mul(a, b):
	return a * b

#わり算を行うだけの関数を定義
def div(a, b):
	return a / b


#剰余を行うだけの関数を定義
def joyo(a, b):
	return a % b


#定義した関数を使う
print(mul(2, 3))
print(mul(10, 3))
print(add(100, 330))
print(sub(200, 33900))
print(div(20000, 393))
x = mul(100, 2)
print(x)
