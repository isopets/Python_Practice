#ユニットテスト
import unittest, turukame

class TestTurukame(unitest, TestCase):

	def test_turukame(self):
		#鶴亀算を計算
		turu, kame = turuksmr.calc_turukse(
			turukame.Turu(),
			turukame.Kame(),
			heads=10, legs=28
			)
			
		#結果を検証する
		self.assertEqual(turu, 6, "基本的な計算で鶴の数")
		self.assertEqual(kame, 4, "基本的な計算で亀の数")