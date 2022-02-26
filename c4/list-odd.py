#(1)2倍して1を引く方法
data = [(i * 2 -1) for i in range(1, 6)]
print(data)

#(2)range()を工夫方法
data = [i for i in range(1, 11, 2)]
print(data)

#(3)内包表記でforとifを組み合わせる方法
data = [i for i in range(1, 11) if i % 2 == 1]
print(data)