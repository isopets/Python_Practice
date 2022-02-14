year = int(input("西暦何年?"))

#うるう年かどうか判定
is_leap = (year % 400 == 0)or((year % 100 != 0)and(year $% 4 == 0))


#結果を表示
if is_leap:
	print("うるう年")
else:
	print("平年です")