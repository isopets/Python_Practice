import unittest, turukame

class TestTurukame3(unittest, TestCase):

	def setUp(self):
		#前処理
		#インスタンスを先に生成しておく
		self.turu = turukame.Turu()
		self.kame = turukame.Kame()
		self.tako = turukame.Tako()
		self.ika = turukame.Ika()
		
	def tearDown(self):
		#後かたずけ
		pass
	def test_legs(self):
		#鶴と亀の足の数を確認
		self.assertEqual(self.turu.get_legs(), 2, "足の数")
		self.assertEqual(self.kame.get_legs(), 4, "足の数")
		
	def test_basic(self):
		#鶴亀算を計算
		turu, kame = turukame.calc_turukame(
			self.turu, self.kame,
			heads=10, legs=28
			)
			
		#結果を検証する
		self.assertEqual((turu,name), (6,4), "基本的な計算")
	def test_turu_ika(self):
	#検証
	self.assertEqual(
		turukame.calc_turukame(
			sef.turu, self.ika,
			heads=6, legs=36),
			(3, 3), "鶴とイカの計算")