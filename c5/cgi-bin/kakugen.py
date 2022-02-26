#!/usr/bin/env python3

#文字化け対策 vvvvvvvvvvvvvvvv
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
#

#ヘッダ情報を出力
print("Content-Type: text/html; charset=utf-8")
1
#ヘッダと本体データを区切る空行
print("")

#本体のデータを出力
print("<html><head><meta charset='utf-8'></head><body>")
print("聞くことに早く語ることに遅くあるべき")
print("</body></html>")