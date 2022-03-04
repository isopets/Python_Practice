from sklearn import datasets, svm, metrics
from sklearn.model_selection import train_test_split

#ワインデータ（CSV)を読み込む
wine_csv= []
with open("winequality-white.csv", "r", encoding="utf-8") as fp:
	no = 0
	for line in fp:
		line = line.strip()
		cols = line.split(";")
		wine_csv.append(cols)

#1行目はヘッダ行なので削除
wine_csv = wine_csv[1:]

#CSVのかくデータを数値に変換
labels = []
data = []
for cols in wine_csv:
	cols = list(map(lambda n: float(n), cols)) #
	#ワインのグレードを調整
	grade = int(cols[11]) #末尾のデータがワインのグレード
	if grade == 9: grade = 8 #少なすぎるサンプルを調整
	if grade < 4 : grade= 5
	labels.append(grade)
	data.append( cols[0:11] ) #ワインの成分データ

#訓練用データとテスト用データに分ける
data_train, data_test, label_train, label_test = train_test_split(data, labels)

#SVMのアルゴリズムを利用して学習
clf = svm.SVC(gamma="auto")
clf.fit(data_train, label_train)

#予測してみる
predict = clf.predict(data_test)

#結果を表示する
ac_score = metrics.accuracy_score(label_test, predict)
cl_report = metrics.classification_report(label_test, predict)
print("正解率=", ac_score)
print("レポート=\n", cl_report)
