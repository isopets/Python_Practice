#素数を列挙するイテレータクラス
class PrimeIter:
	def __init__(self, max):
		"""最大値を指定"""
		self.max = max
		
	def __iter__(self):
		"""値を初期化する"""
		self.n = 1
		return self
		
	def __next__(self):
		"""つぎの素数を探して返す"""
		is_prime = False
		self.n += 1
		#素数を探す
		while not is_prime:
			is_prime = True
			for i in range(2, self.n):
				if self.n % i == 0:
					is_prime = False
					break
			if is_prime: break
			self.n += 1
			#最大値に達したら例外を出す
			if self.n >= self.max:
				raise StopIteration
			return self.n
#100以下の素数を列挙する
it = PrimeIter(100)
for no in it:
	print(no, end=",")