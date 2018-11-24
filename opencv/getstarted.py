import cv2
from matplotlib import pyplot
from config import basedir

image_dir = basedir + '/static/images/'


def read_img():
    filename = image_dir + '1542529099348001-660010168986109.jpg'
    im = cv2.imread(filename, 0)
    cv2.imshow('image', im)
    k = cv2.waitKey(0)
    if k == 27:
        cv2.destroyAllWindows()
    elif k == ord('s'):
        cv2.imwrite('res.jpg', im)
        cv2.destroyAllWindows()


def plot_show():
    from matplotlib import pyplot as plt, image
    im = image.imread('res.jpg')
    plt.imshow(im)
    plt.show()


# 调用摄像头
def capture_video():
    # 打开摄像头
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        cap.open(0)
    while True:
        cap.set(3, 320)
        # 捕获栈帧
        ret, frame = cap.read()

        # 将真彩色转换成黑白
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', gray)

        # 显示栈帧
        cv2.imshow('frame', frame)
        # 按q退出q
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # 释放摄像头
    cap.release()
    # 关闭窗口
    cv2.destroyAllWindows()


# 保存video
def save_video():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        cap.open(0)
    # 指定编解码器和视频写对象
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    # 文件名, 编解码器, 每秒保存多少帧图片,是否彩色
    out = cv2.VideoWriter('output.avi', fourcc, 10, (640, 480), isColor=True)

    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            # frame = cv2.flip(frame, 0)
            out.write(frame)

            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
    cap.release()
    out.release()
    cv2.destroyAllWindows()


def play_video():
    cap = cv2.VideoCapture('output.avi')

    while cap.isOpened():
        ret, frame = cap.read()
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()


def blend_image():
    im1 = cv2.imread('jjy.jpg')
    im2 = cv2.imread('jjy3.jpg')
    res = cv2.addWeighted(im1, 0.4, im2, 0.6, 0)
    cv2.imwrite('res.jpg', res)


def object_tracking():
    import numpy as np
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        lower_blue = np.array([110, 50, 50])
        upper_blue = np.array([130, 255, 255])

        mask = cv2.inRange(hsv, lower_blue, upper_blue)

        res = cv2.bitwise_and(frame, frame, mask=mask)

        cv2.imshow('frame', frame)
        cv2.imshow('mask', mask)
        cv2.imshow('res', res)

        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break

    cv2.destroyAllWindows()


if __name__ == '__main__':
    img = cv2.imread('jjy2.jpg')
    laplacian = cv2.Laplacian(img, cv2.CV_64F)
    pyplot.imshow(laplacian)
    pyplot.show()


# 特征匹配

# 前景提取

# 图像混叠 done !

# 图像水印 done !

# 文字水印 done !

# 图像去水印

# 图像打马赛克 done !

# 图像去马赛克

# 拼接长图
