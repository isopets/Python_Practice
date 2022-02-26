import time

def time_log(func):
	def wrapper(*args, **kwargs):
		#前処理
		import datetime
		start = datetime.datetime.today()
		print("--- start", func.__name__)
		#関数の実行
		result = func(*args, **kwargs)
		#後処理
		end = datetime.datetime.today()
		delta = end - start
		print("---end", func.__name__, delta, "sec")
	return wrapper


@time_log
def test1():
	print("sleep 1sec")
	time.sleep(1)

@time_log
def test2():
	print("sleep 2sec")
	time.sleep(2)
	
test1()
test2()	