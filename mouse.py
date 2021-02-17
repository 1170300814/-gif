#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import time
import pyautogui as pag
import tkinter
from  PIL import  ImageGrab
import  imageio
import  numpy as np
mytime = 2


# 判断时间是否合法
def safe():
    text = getmytime.get();
    # 小数点个数
    point = 0
    if (text == ""):
        return False
    for i in text:
        if (i >= '0' and i <= '9' and point < 2):
            continue
        elif (i == '.'):
            point = point + 1
        else:
            return False
    return True


def get():
    global mytime
    if (True):
        mytime = float(2)

        # 不知道为何下面的这个if没用
        if (mytime > 7.0):
            showpos.delete(0, tkinter.END)
            showpos.insert(0, "请耐心等候")

        time.sleep(mytime)  # 几秒后返回位置
        x, y = pag.position()
        return x,y
    else:
        showpos.delete(0, tkinter.END)
        showpos.insert(0, "输入非法哟~")

def sleep():
    global  mytime
    time.sleep(mytime)
    showpos.delete(0, tkinter.END)
    print("fuck")

imgs = []
frames = []
root = tkinter.Tk()
root.resizable(0, 0)

tip1 = tkinter.Label(root, text="点击按钮获取")
tip1.place(relx=0.1, rely=0.1)
getmytime = tkinter.Entry(root, width=3)
getmytime.place(relx=0.6, rely=0.1)
getmytime.insert(0, str(mytime))
tip2 = tkinter.Label(root, text="s后的")
tip2.place(relx=0.8, rely=0.1)

tip3 = tkinter.Label(root, text="光标位置:")
tip3.place(relx=0.1, rely=0.3)
showpos = tkinter.Entry(root, width=10)
showpos.place(relx=0.5, rely=0.3)
left,top=get()
do = tkinter.Button(root, text="按钮", command=sleep)
do.place(relx=0.8, rely=0.6)

root.mainloop()
right,bottom=get()
rect = (left, top, right, bottom)
print(left,top,right,bottom)



for i in range(20):
    time.sleep(0.1)
    imgs.append(ImageGrab.grab(rect))  # 屏幕截图
    print("Catch  IMG_" + str(i + 1) + " OK")  # 显示进度

for i, img in enumerate(imgs):
    img = img.convert("RGB")  # 通过convert将RGBA格式转化为RGB格式，以便后续处理
    img = np.array(img)  # im还不是数组格式，通过此方法将img转化为数组
    frames.append(img)  # 批量化
    print(str(i) + " OK")

imageio.mimsave("150%.gif", frames, 'GIF', duration=0.1)  # 转为GIF
print("-----------------DONE!-----------------")

