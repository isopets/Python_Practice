#ダイアログを表示するために必要なモジュール
import tkinter.messagebox as md #asについてはP.１５８を参照

#ダイアログを表示
ans = md.askyesno("質問", "ラーメンは好きですか？")
if ans == True:
	#OKボタンがあるだけのダイアログを表示
	md.showinfo("同意", "僕も好きです。")
else:
	md.showinfo("本当？", "まさか、ラーメンが嫌いだなんて！")
	