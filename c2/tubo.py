#繰り返し坪数を調べるうろグラム

while True:
	tubo = int(input("坪数は？"))
	m2 = tubo * 3.31
	s = "{0}坪は{1}平方メートルです".format(tubo, m2)
	print(s)