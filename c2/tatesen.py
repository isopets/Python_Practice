#画面に300本の縦線を引く

#グラフィックライブラリを取り込む
from tkinter import *
#画面の初期化
w = Canvas(Tk(), width = 900, height = 400)
w.pack()

#線をたくさん引く
for i in range(300):
	x = i * 3
	w.create_line(x, 0, x, 400, fill="#FF0000")
	
mainloop()