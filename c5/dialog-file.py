#ダイアログを表示するために必要なモジュール
import tkinter. filedialog as fd

#ファイル選択ダイアログを表示する
path = fd.askopenfilename(
	title="処理対象のファイルを指定してください", #ダイアログ上部のタイトルを設定
	filetypes=[('HTML', '.html')]) #「HTML」または「.html」形式のファイルだけを表示
print(path)