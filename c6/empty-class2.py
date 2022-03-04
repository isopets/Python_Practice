#空のクラス
class Empty : pass

#空のクラスのインスタンスを生成
calc = Empty()
#動的にメソッドを追加
calc.x2 = lambda x : x * 2
calc.x3 = lambda x : x * 3

#追加したメソッドを使ってみる
print(calc.x2(8))
print(cac.x3(5))
