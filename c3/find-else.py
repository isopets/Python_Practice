#for公文で elseを記述する場合
#食材一覧
foodstuff = ["Banana", "Mango", "Fish", "Carrot", "cabbage"]

#マンゴーがないか確認する
for food in foodstuff:

	if food =="Mango":
		print("マンゴーが入っています")
		break
else:
	print("ありません。")
	