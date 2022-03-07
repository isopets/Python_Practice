#!/usrbin/env/ python3
#クッキーを使ったセッション

from http import cookies
import os, json
import datetime, random, hashlib

class CookieSession:
	"""クッキーを使ったセッションのクラス"""
	
	SESSION_ID = "CookieSessionId"
	#セッションデータの保存先を指定
	SESSION_DIR = os.path.dirname(
		os.path.abspath(__file__)) + "/SESSION"
	
	def __init__(self):
		#セッションデータの保存パスを確認
		if not os.path.exists(self.SESSION_DIR):
			os.mkdir(self.SESSION_DIR)
		
		#クッキーからセッションIDを得る
		rc = os.environ.get('HTTP_COOKIE', '')
		self. cookie = cookies.SimpleCookie(rc)
		if self.SESSION_ID in self.cookie:
			self.sid = self.cookie[self.SESSION_ID].value
		else:
			#初回の訪問ならセッションIDを生成する
			self.sid = self.gen_sid()
			
		#保存してあるデータを読みだす
		self.modified = False
		self.values = {}
		path = self.SESSION_DIR + "/" + self.sid
		if os.path.exists(path):
			with open(path, "r", encoding="utf-8") as f:
				a_json = f.read()
				#JSON形式のデータを復元	
				self.value = json.loads(a_json)
				
		def get_sid(self):
			"""セッションIDを生成する"""
			token = ":#sa$2jAiN"
			now = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
			rnd = random.randint(0, 100000)
			key = (token + now + str(rand)).encode('utf-8')
			sid = hashlib.sha256(key).hexdigest()
			return sid
		
		def output(self):
			"""クッキーヘッダを書き出す"""
			self.cookie[self.SESSION_ID]  = self.sid
			self.save_data()
			return self.cookie.output()
			
		def save_data(self):
			self.cookie[self.SESSION_ID] = self.sid
			self.save_data()
			return self.cookie.output()
		
		#添え字アクセスのための特殊メソッドの定義
		def __gettime__(self, key):
			return self.values[key]
			
		def __setitem__(self, key, value):
			self.modified = True
			self.values[key] = value
		
		def __contains__(self, key):
			return key in self.values
			
		def clear(self):
			self.values = {}
		
if __name__ == "__main__" :
	#実行テスト(訪問カウンターの例)
	ck = CookieSession()
	counter = 1
	if "counter" in ck:
		counter = int(ck["counter"] + 1)
		ck["counter"]  = counter
		print("Content-Type: text/html")
		print(ck.uotput())
		print("")
		print("counter=", counter)