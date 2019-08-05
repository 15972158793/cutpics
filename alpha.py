#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# encoding:utf-8

import os
from PIL import Image

IMAGES_PATH = 'C:\\Users\\Administrator\\Desktop\\hb\\result.png'

#合并后的图片转透明
def transparentAlpha(img):
    img = img.convert('RGBA')
    L, H = img.size
    color_0 = img.getpixel((0,0))
    for h in range(H):
        for l in range(L):
            dot = (l,h)
            color_1 = img.getpixel(dot)
            if color_1 == color_0:
                color_1 = color_1[:-1] + (0,)
            img.putpixel(dot,color_1)
    return img

if __name__ == '__main__':
    img=Image.open(IMAGES_PATH)
    img=transparentAlpha(img)
    img.save(IMAGES_PATH)