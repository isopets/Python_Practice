#非公開属性にアクセスできないことを確かめるプログラム
#そのためエラーが出ます
#---クラス定義
class Game:
	def __goal(self):
		print("非公開のメソッド")
		
	def play(self):
		print("公開メソッド")

#---クラスの利用
game = Game()
game.play()
game.__goal() #ここでエラー