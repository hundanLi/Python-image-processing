import cv2
import numpy as np
from config import img_dir


def read_img(filename):
    return cv2.imread(img_dir + filename)


def de_mask(filename):
    im = read_img(filename)
    # 图像二值化处理
    thresh = cv2.inRange(im, np.array([240, 240, 240]), np.array([255, 255, 255]))

    # 创建形状和尺寸的结构元素
    kernel = np.ones((3, 3), np.uint8)

    # 扩张修复区域
    hi_mask = cv2.dilate(thresh, kernel, iterations=1)
    specular = cv2.inpaint(im, hi_mask, 1, flags=cv2.INPAINT_TELEA)

    cv2.imshow('Image', specular)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def match_img():
    pass


if __name__ == '__main__':
    de_mask('jjy_mask_white.jpg')
