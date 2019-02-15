# coding=utf-8
from __future__ import print_function
from utls import *
import cv2

if __name__ == '__main__':
    INPUT_PATH = "../img/xie.jpg"
    OUTPUT_PATH = "../generateImg/xie.png"
    img = cv2.imread(INPUT_PATH)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 如果运行时间太长了，可以将图像进行缩小
    # h, w = img.shape
    # img = cv2.resize(img, (w/6, h/6))

    img = reImg(img)  # 变成十值图像（将将灰度图像的色彩空间转换为0-9的值）
    lists = to2dList(img)  # 生成01的字符串数组
    img = toCharImg(img, lists)  # 生成字符图片

    cv2.imwrite(OUTPUT_PATH, img)  # 保存生成的图片
