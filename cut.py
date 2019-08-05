#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# encoding:utf-8

import os
from PIL import Image
#图片的名字
picName = "di"
#子文件名称
picZName = "di_"
#图片和脚本所在的目录
baseDir = "C:\\Users\\Administrator\\Desktop\\cutpics\\" + picName

#横向切割  需要指定切割后保存的目录以及图片名称
def cutHorizontal(w,h,maxW,maxH):
    #图片的路径
    name1 = baseDir + ".png"
    #切割后的存储位置
    name2 = baseDir + "\\" + picZName
    im =Image.open(name1)

    #偏移量
    dx = w
    dy = h
    n = 1

    #左上角切割
    x1 = 0
    y1 = 0
    x2 = dx
    y2 = dy

    while y2 <= maxH:
        while x2 <= maxW:
            name3 = name2 + str(n) + ".png"
            #print n,x1,y1,x2,y2
            im2 = im.crop((x1, y1, x2, y2))
			#save file
            im2.save(name3)
            x1 = x1 + dx
            x2 = x1 + dx
            y1 = 0
            y2 = dy
            n = n + 1
        y1 = y1 + dy
        y2 = y1 + dy
    print u"图片切割成功，切割得到的子图片数为".encode('gbk')
    return n-1

#纵向切割
def cutPortrait(w,h,maxW,maxH):
    #图片的路径
    name1 = baseDir + ".png"
    #切割后的存储位置
    name2 = baseDir + "\\" + picZName
    im =Image.open(name1)
    #偏移量
    dx = w
    dy = h
    n = 1

    #左上角切割
    x1 = 0
    y1 = 0
    x2 = dx
    y2 = dy

    while x1 <= maxW:
        while y1 <= maxH:
            name3 = name2 + str(n) + ".png"
            #print n,x1,y1,x2,y2
            im2 = im.crop((x1, y1, x2, y2))
            #save file
            im2.save(name3)
            y1 = y1 + dy
            y2 = y1 + dy
            n = n + 1
        x1 = x1 + dx
        x2 = x1 + dx
        y1 = 0
        y2 = dy
    print u"图片切割成功，切割得到的子图片数为".encode('gbk')
    return n-1

#单独切割一张图片
def cut(x,y,w,h):
    #图片的路径
    name1 = baseDir + ".png"
    #切割后的存储位置
    name2 = baseDir + "\\" + picZName
    im =Image.open(name1)
    name3 = name2 + "0.png"
    #print n,x1,y1,x2,y2
    im2 = im.crop((x, y, w, h))
    im2.save(name3)
    print u"图片切割成功".encode('gbk')

if __name__=="__main__":
    #设定切割的宽和高 最大的宽和高
    #横向切割
    #res = cutHorizontal(14,20,560,40)
    #纵向切割
	res = cutPortrait(337,144,337,438)
    #res = cutPortrait(337,51,337,144)
    print res
    #cut(0,10,337,144)