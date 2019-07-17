#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# encoding:utf-8

import os
from PIL import Image

def cut(w,h):
    #图片的路径
    name1 = "C:\\Users\\Administrator\\Desktop\\jb\\tt1.png"
	#切割后的存储位置
    name2 = "C:\\Users\\Administrator\\Desktop\\jb\\tt\\tt_"
	
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
	
	#横向
    while y2 <= 40:
        #横向切
        while x2 <= 560:
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

'''
    #纵向
    while x2 <= 560:
        #横向切
        while y2 <= 300:
            name3 = name2 + str(n) + ".png"
            #print n,x1,y1,x2,y2
            im2 = im.crop((y1, x1, y2, x2))
			
			#save file
            im2.save(name3)
            y1 = y1 + dy
            y2 = y1 + vy
            n = n + 1
        x1 = x1 + dx
        x2 = x1 + vx
        y1 = 0
        y2 = vy
'''

if __name__=="__main__":
    #设定切割的宽和高
    res = cut(14,20)
    print res