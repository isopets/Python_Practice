import unittest, turukame

#あえて間違った値を指定する例
class TesttTUrukame2(unittest.TestCase):

	def test_turukame_ng(self):
		#鶴亀算を計算
		turu, kame = turukame.calc_turukame(
			turukame.Turu(),
			turukame.Kame(),
			heads=10, legs=28
			)
			
		
		#結果を検証する
		self.assertEqual(turu, 8, "基本的な計算で鶴の数")
		self.assertEqual(kame, 12, "基本的な計算で亀の数")
		