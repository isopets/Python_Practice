#畳を平米に変換
def convert_jou(jou, unit="江戸間"):
	if unit =="江戸間":
		base = 0.88 * 1.76
	elif unit == "京間":
		base = 0.955 * 1.91
	elif unit == "中京間":
		base = 0.91 * 1.82
	m2 = jou * base
	s = "{0}で{1}畳は{2}㎡".format(unit, jou, m2)
	print(s)
	
#関数を実行
convert_jou(6, "江戸間")# ---
convert_jou(6, "京間")# ---
convert_jou(6, "中京間")# ---
