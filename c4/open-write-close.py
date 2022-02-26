#(1)ファイルを開く
a_file = open("test.txt", mode ="w", encoding="utf-8")

#(2)ファイルに書き込む
a_file.write("私は失敗したことがない。\n")
a_file.write("ただ、一通りの方法を\n見つけただけだ。\n")
a_file.write("- トーマス・エジソン\n")

#(3)ファイルを閉じる
a_file.close()
