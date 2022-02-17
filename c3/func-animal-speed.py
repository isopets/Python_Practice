#動物の最高時速を辞書型で定義
animal_speed_dict = {
	"チーター":110, "トナカイ":80,
	"シマウマ":60, "ライオン":58,
	"キリン":50, "ラクダ":30
}

#東京から各都市までの距離を辞書型で定義
distance_dict = {
	"静岡":183.7,
	"名古屋":350.6,
	"大阪":507.5
}

#時間を計算する関数を定義
def calc_time(dist, speed):
	t = dist/speed #距離÷速度を計算
	t = round(t, 1) #四捨五入
	return t
	
#動物の各都市までの時間を計測する関数を定義
def calc_animal(animal, speed):
	res = "|" + animal
	for city in sorted(distance_dict.keys()):
		dist =distance_dict[city] #都市までの距離を代入
		t = calc_time(dist, speed) #calc_time()を、距離とスピードを指定して呼び出す
		res += "|{0:>6}".format(t) #calc_time()の戻り値の時間を埋め込んで代入
	return res + "|" #票の各行の最後に|を追加
	
#表のヘッダを表示
print("+--------+--------+--------+--------+")
print("|動物名前", end = "") #end=""は開業しないという指定
for city in sorted(distance_dict.keys()): #各都市の名前をソートして範囲に指定
	print("|" + city, end="") #順番に都市の名前を出力
print("|")
print("+--------+--------+--------+--------+")
#各動物ごとに結果を求めて表示
	
for animal, speed in animal_speed_dict.items(): #animal_speed_dictのキーと値を繰り返し取得
	s = calc_animal(animal, speed) #calc_animal()を、動物名とスピードを指定して呼び出す
	print(s)
print("+--------+--------+--------+--------+")