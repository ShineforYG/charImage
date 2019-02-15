# coding=utf-8
import cv2
import numpy as np

chars = ['8', '6', '9', '5', '0', '2', '3', '4', '7', '1']


def reImg(img):
    h, w = img.shape
    min_value = np.min(img)
    max_value = np.max(img)
    x = (max_value - min_value) / (len(chars) - 1)
    for i in range(h):
        for j in range(w):
            img[i][j] = (img[i][j] - min_value) / x
    return img


def toString(img):
    lists = []
    h, w = img.shape
    for i in range(h):
        string = ""
        for j in range(w):
            string = string + chars[img[i][j]]
        lists.append(string)
    return lists


def to2dList(img):
    lists = []
    h, w = img.shape
    for i in range(h):
        string = []
        for j in range(w):
            string.append(chars[img[i][j]])
        lists.append(string)
    return lists


def toCharImg(img, lists):
    # 将字符串画到图像上面
    h, w = img.shape
    img = np.full((8 * h, 8 * w), 255)

    for i in range(h):
        # def putText(img, text, org, fontFace, fontScale, color, thickness=None, lineType=None, bottomLeftOrigin=None):
        for j in range(len(lists[i])):
            cv2.putText(img, lists[i][j], (j * 8, i * 8 + 7), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 0.3, (0, 0, 0))
    return img
