#旧暦の月名を返すクラスを定義
class Tukimei:
	tuki = ["睦月", "如月", "弥生", "卯月", "皐月", "水無月",
		"文月", "葉月", "長月", "神無月", "霜月", "師走"]
	def __getitem__(self, key):
		i = int(key)
		return self.tuki[i-1] #インデックス番号に「-1」を指定して、月と一致させる。
		
#添え字アクセスしてみる
t = Tukimei()
print(t[3])
print(t[6])