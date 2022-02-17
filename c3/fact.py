#階乗を求める
def fact(n):
	if n == 0:
		return 1
	else: #それ以外の場合は再帰的にfact()関数を呼ぶ
		return n * fact(n -1)

print(fact(3))
print(fact(5))


