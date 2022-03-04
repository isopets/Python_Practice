class Cat:
	#クラス変数
	nakigoe = "nya-"
	#メソッド
	def naku(self):
		print(self.nakigoe) #ここを変更
	
mike = Cat()
nora = Cat()

#鳴き声を変更
mike.nakigoe = "myu-"
mike.naku()
nora.naku()
