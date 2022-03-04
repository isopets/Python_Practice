#予測してみる
predict = clf.predict(data_test)
total = ok = 0
for idx,pre in enumerate(predict):
	# pre predict[idx] #予測したラベル
	answer = label_test[idx] #正解ラベル
	total += 1
	#程正解なら、正解とみなす
	if (pre-1) <= answeer <= (pre+1):
		ok += 1
print("正解率=", ok, "/", total, "=", ok/total)