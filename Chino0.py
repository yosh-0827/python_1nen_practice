#!/usr/bin/env python
# coding: utf-8

# In[6]:


import tkinter as tk
import tkinter.filedialog as fd
import PIL.Image
import PIL.ImageTk
# 機械学習で使うモジュール
import sklearn.datasets
import sklearn.svm
import numpy

# 画像ファイルを数値リストに変換する
def imageToData(filename):
    # 画像を８ｘ８のグレースケールに変換
    greyImage = PIL.Image.open(filename).convert("L")
    greyImage = greyImage.resize((8,8), PIL.Image.ANTIALIAS)
    # その画像を表示する
    dispImage = PIL.ImageTk.PhotoImage(greyImage.resize((300,300)))
    imageLabel.configure(image = dispImage)
    imageLabel.image = dispImage
    # 数値リストに変換
    numImage = numpy.asarray(greyImage, dtype = float)
    numImage = numpy.floor(16 - 16 * (numImage / 256))
    numImage = numImage.flatten()
    return numImage

# 数字を予測する
def predictDigits(data):
    # 学習用データを読み込み
    digits = sklearn.datasets.load_digits()
    # 機械学習する
    clf = sklearn.svm.SVC(gamma = 0.001)
    clf.fit(digits.data, digits.target)
    # 予測を表示する
    n = clf.predict([data])
    textLabel.configure(text = "この画像は"+str(n)+"です")

# ファイルダイアログを開く
def openFile():
    fpath = fd.askopenfilename()
    if fpath:
        # 画像ファイルを数値リストに変換する
        data = imageToData(fpath)
        # 数字を予測する
        predictDigits(data)

# アプリのウィンドウを作る
root = tk.Tk()
root.geometry("400x400")

btn = tk.Button(root, text="ファイルを開く", command = openFile)
imageLabel = tk.Label()

btn.pack()
imageLabel.pack()

# 予測結果を表示するラベル
textLabel = tk.Label(text="手書きの数字を認識します")
textLabel.pack()

tk.mainloop()


# In[ ]:




