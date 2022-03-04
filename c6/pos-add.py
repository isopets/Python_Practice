class Pos:
	"""座標を表すクラス"""
	def __init__(self, x, y):
		self.x = x
		self.y = y
		
	def __add__(self, other):
		"""「+」演算子のふるまいを定義
			selfとotherの要素を足した
			新しいインスタンスを返す"""
		x2 =self.x + other.x
		y2 = self.y + other.y
		return Pos(x2, y2)
	
	def __str__(self):
		"""文字列として取得する際のふるまいを定義"""
		return "({0}, {1})".format(self.x, self.y)

#座標p1とp2を作成
p1 = Pos(10, 20)
p2 = Pos(30, 40)

#演算子「＋」を使ってみる
p3 = p1 + p2
print(p3)