#関数の外側でvalueに１００を代入
value = 100

def changeValue():
	#関数の内側でvalueを代入
	value = 20

changeValue()
print("value=", value) #<---- 果たしてこの値は？
