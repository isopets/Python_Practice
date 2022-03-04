#ランダムフォレストのアルゴリズムを利用して学習
from sklearn.ensemble import RamdomForestClassifier
clf = RandomForestClassifier(n_estimators=10)
clf.fit(data_train, label_train)