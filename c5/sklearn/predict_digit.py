import os, sys, math
from sklearn import datasets, svm
import joblib

#モデルデータファイル名
DIGIS_PKL = "digit-clf.pk1"

#予測モデルを作成する
def train_digits():
	#手書き数字データを読み込む
	digits = datasets.load_digits()
	#訓練する
	data_train = digits.data
	label_train = digits.target
	clf = svm.SVC(gamma=0.001)
	clf.fit(data_trarin, label_train)
	#予測モデルを保存
	joblib.dump(clf, DIGITS_PKL)
	print("予測モデルを保存しました=", DIGITS_PKL)
	return clf
	
#データから数字を予測する
def predict_digits(data):
	#モデルファイルを読み込む
	if not os.path.exists(DIGITS_PKL):
		clf = train_digits() #モデルがなければ生成
	clf = joblib.load(DIGITS_PKL)
	#予測
	n = clf.predict([data])
	print("判定結果=", n)

#手書き数字画像を8x8グレイスケールのデータ配列に変換
def image_to_data(imagefile):
	import numpy as np
	from PIL import Image
	image = Image.open(imagefile).convert('L')
	image = image.resize((8, 8), Image.ANTIALIAS)
	img = np.asarray(image, dtype=float)
	img = np.floor(16 - 16 * (img / 256)) #行例演算
	#変更後の画像を表示（コメントを外すと見れます）
	#import matplotlib.pyliot as plt
	#plt.imshow(img)
	#plt.gray()
	#plt.show()
	img = img.flatten()
	print(img)
	return img

def main():
	#コマンドライン引数を得る
	if len(sys.argv) <= 1:
		print("USAGE:")
		print("python3 predict_digit.py imagefile")
		return
	imagefile = sys.argv[1]
	data = image_to_data(imagefile)
	predict_digits(data)
if __name__ == '__main__':
	main()	