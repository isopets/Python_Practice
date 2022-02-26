#テキストからキーワードを探す
key = "find"
with open("mt7_7.txt", encoding="utf-8") as tf:
	#1行ずつファイルを読む
	for i, line in enumerate(tf): #enumerate()関数(P.093)を使う
		#文字列 key が行に含まれるか？
		if line.find(key) >= 0: #find()メソッド(P.115)を使う
			print(i+1, ":", line)