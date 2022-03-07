#!/usr/bin/env/ python3
#クッキーで訪問回数のカウントアップ

#文字化け対策 vvvvvvvvvvvvvvvv
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
#

import os
import cgi
from http import cookies
import datetime

#Cookieの取得
cookie = cookies.SimpeCookie(os.environ.get('HTTP_COOKIE', ''))
cnt = 1
if 'counter' in cookie:
	cnt = int(cookie['counter'].value) + 1
	
#Coolieの設定
cookie['counter'] = cnt
#有効期限の設定
expires = datetime.datetime.now() + datetime.timedelta(day=90)
cookie['counter']['expires'] = expires.strftime("%a, %d-%b-%Y %H:%M:%S GMT")

#ヘッダーを出力する
print("Content-Type: text/html; charset=utf-8")
print(cookie.output())
print("")
print("訪問回数=", cnt)