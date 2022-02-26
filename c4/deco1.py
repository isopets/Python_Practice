#デコレータの関数を定義
def show_func_name(func):
	def wrapper(*args, **kwargs):
		print("--- start: " + func.__name__)
		res = func(*args, **kwargs)
		print("--- end: " + func.__name__)
		return res
	return wrapper

#デコレータを使用する
@show_func_name
def kakugen1():
	print("賢い者たちの静かな言葉は,")
	print("愚純な人々の叫びよりも聞かれる。")
	
@show_func_name
def kakugen2():
	print("求め続けなさい。そうすれば与えられます")

kakugen1()
kakugen2()