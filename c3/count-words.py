#単語の出現回数をカウント
text = """
keep on asking, and it will be given you;
keep on seeking, and you will find;
keep on knocking, and it willbe opend to you;
for everyone asking receives, and everyone seeking finds,
and to everyone knocking, it will be opened.
"""

#単語を区切る
text = text.replace(";", "") #;を削除
text = text.replace(",", "") #,を削除
text = text.replace(".", "") #.を削除
words = text.split() #空白で区切ってリスト型を作成

#単語を数える
counter = { } #counterという空の辞書型を作成
for w in words:
	ws = w.lower() #小文字に変換
	if ws in counter:
		counter[ws] += 1
	else:
		counter[ws] = 1

#結果を表示
for k, v in sorted(counter.items()):
	if v >= 3:
		print(k, v)