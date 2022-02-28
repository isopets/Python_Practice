#Scilit learnのサンプル学習データを取り込む
from sklearn import datasets

#描画のためにmatplotlibモジュールを取り込み
from matplotlib import pyplot as plt, cm #asについてはP.158を参照

#手書き数字データを読み込む
digits  =datasets.load_digits()
data  = digits.images[8]

#描画
plt.imshow(data.reshape(8, 8), cmap=cm.gray_r, interpolation='nearest')
plt.show()
