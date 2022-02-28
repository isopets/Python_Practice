#!/usr/bin/env python3

import cgi

#文字化け対策
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

#ヘッダの出力
print("Content-Type: text/html; charset=utf-8")
print("")

#送信されたフォームデータを取得
form = cgi.FieldStorage()

#フォームにv1とv2のデータが含まれるか?
if(not 'v1' in form) or (not 'v2' in form):
	#含まれないのでフォームを表示
	print("""
		<form>
		<input type="text" name="v1"> +
		<input type="text" name="v2">
		<input type="submit" value="計算">
		</form>
	""")
else:
	#フォームの値を取得して計算結果を表示
	v1 = form.getvalue("v1", "0")
	v2 = form.getvalue("v2", "0")
	try:
		ans = int(v1) + int(v2)
	except:
		ans = 0
	print("<h1>", ans, "</h1>")
