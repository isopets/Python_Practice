#BMIを計算するクラス
class BMI:
	def __init(self, weight, height):
	 	'''初期化'''
	 	self.weight = weight
	 	self.height = height
	 	self.calcBMI()
	 
	def calcBMI(self):
		'''BMIを計算する'''
		h= self.height / 100
		self.bmi = self.weight / (h ** 2)
		
	def printJudge(self):
		'''結果を表示する'''	
		print("---")
		print("BMI=", self.bmi)
		b = self.bmi
		if (b < 18.5): print("やせ型")
		elif (b < 25): print("標準")
		elif (b < 30): print("肥満(重)")
		else: print("肥満(軽)")
	 
#１人目
preson1 = BMI(weight=65, height=170)
preson1.printJudge()

#２人目
preson2 = BMI(weight=76, height=165)
preson2.printJudge()

#3人目
preson3 = BMI(weight=50, height=180)
preson3.printJudge()
 
 	