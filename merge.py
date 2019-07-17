#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# encoding:utf-8

import os
from PIL import Image

# 图片集地址
IMAGES_PATH = 'C:\\Users\\Administrator\\Desktop\\jb\\p1\\'
# 图片格式
IMAGES_FORMAT = ['.jpg', '.JPG',".png",".PNG"]
# 每张小图片的宽
IMAGE_WIDTH = 78
# 每张小图片的高
IMAGE_HEIGHT = 140
# 图片间隔，也就是合并成一张图后，一共有几行
IMAGE_ROW = 4
# 图片间隔，也就是合并成一张图后，一共有几列
IMAGE_COLUMN = 4
# 图片合成后的地址
IMAGE_SAVE_PATH = 'C:\\Users\\Administrator\\Desktop\\jb\\p1\\result.jpg'

# 获取图片集地址下的所有图片名称
image_names = [name for name in os.listdir(IMAGES_PATH) for item in IMAGES_FORMAT if
               os.path.splitext(name)[1] == item]
print(u'图片的个数:'.encode('gbk') + '  %d' % len(image_names))

def start_merge():
    to_image = Image.new('RGB', (IMAGE_COLUMN * IMAGE_WIDTH, IMAGE_ROW * IMAGE_HEIGHT)) #创建一个新图
    # 循环遍历，把每张图片按顺序粘贴到对应位置上
    for y in range(1, IMAGE_ROW + 1):
        for x in range(1, IMAGE_COLUMN + 1):
            from_image = Image.open(IMAGES_PATH + image_names[IMAGE_COLUMN * (y - 1) + x - 1]).resize(
                (IMAGE_WIDTH, IMAGE_HEIGHT),Image.ANTIALIAS)
            to_image.paste(from_image, ((x - 1) * IMAGE_WIDTH, (y - 1) * IMAGE_HEIGHT))
    return to_image.save(IMAGE_SAVE_PATH) # 保存新图
#执行
start_merge()