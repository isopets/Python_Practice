import sys
import os
import fnmatch
import datetime
import math

#引数の確認と使い方を表示
if len(sys.argv) <= 1:
	print("[USAGE] findfile [--name][--wild][--desc] nae")
	sys.exit(0)
	
#オプションの初期値
searth_mode = "name"
serch_func = lambda target, name : (target == name) #targetとnameが一致したらTrueを返す。(target == name)のかっこは読みやすくするためのもの
name = ""
desc_mode = False

#オプションを解析
for v in sys.argv:
	if v == "--name":
		search_mode = "name"
		serach_func = lambda target, name : (target == name)
	elif v == "--wild":
		search_mode = "wild"
		search_func = lambda target, pat : fnmatch.fnmatch(target, pat)
	elif v == "--desc": desc_mode = True
	else:
		name = v #コマンドライン引数として指定したファイル名またはワイルドカードを取得
		
#オプションの解析結果を表示
print("+option")
print("| search_mode=", search_mode, name)
print("| desc_mode=", desc_mode)

#ファイルの検索を開始
for root, dirs, files in os.walk("."):
	for fname in files:
		path = os.path.join(root, fname)
		b = search_func(fname, name)
		if b == False: continue #Falseなら37行目に戻って繰り返し
		if desc_mode:
			info = os.stat(path)
			kb = math.ceil(info.st_size / 1024)
			mt = datetime.datetime.fromtimestamp(info.st_mtime)
			s = "{0}, {1}KB,{2}".format(path, kb, mt.strftime("%Y-%m-%d"))
			print(s)
		else:
			print(path)