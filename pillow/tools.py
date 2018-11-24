# coding: utf-8

from PIL import ImageDraw, Image, ImageColor, ImageFont
from utils.utils import get_img, save_img
from config import basedir


def convert_img(dst, src):
    dst_suffix = dst.split('.')[-1]
    new_filename = src.split('.')[0] + '.' + dst_suffix
    im = get_img(src)
    im = im.convert('RGB')
    return save_img(im, new_filename)


# 打马赛克
def mosaic(filename: str, sp: list, ep: list, granularity: int) -> tuple:
    olddata = '#'.join(sp + ep) + '#' + str(granularity)
    # 获取图像
    im = get_img(filename)
    width, height = im.size
    # 创建Draw对象
    draw = ImageDraw.ImageDraw(im=im)
    sp[0] = int(sp[0])
    sp[1] = int(sp[1])
    # 区域起点大于图像的尺寸
    if sp[0] > width or sp[1] > height or granularity < 1:
        return filename, olddata
    # 处理终点
    ep[0] = width if int(ep[0]) > width else int(ep[0])
    ep[1] = height if int(ep[1]) > height else int(ep[1])

    # 正式打马赛克
    for x in range(int(sp[0]), ep[0], granularity):
        for y in range(int(sp[1]), ep[1], granularity):
            # 选取小方块中心的像素点填充整个小方块
            r, g, b = im.getpixel((x, y))
            draw.rectangle([(x, y), (x + granularity - 1, y + granularity - 1)], fill=(r, g, b))
    # 保存并返回文件名
    return save_img(im, filename), olddata


# 图像部分旋转
def rotate(filename: str, sp: list, size: int, degree: int):
    if degree == 90:
        angle = Image.ROTATE_90
    elif degree == 180:
        angle = Image.ROTATE_180
    else:
        angle = Image.ROTATE_270
    # 获取图像
    im = get_img(filename)
    width, height = im.size

    sp[0] = int(sp[0])
    sp[1] = int(sp[1])
    # 区域起点大于图像的尺寸
    if sp[0] > width or sp[1] > height:
        return filename
    # 设置窗口大小
    size_x = width - sp[0] if sp[0] + size > width else size
    size_y = height - sp[1] if sp[1] + size > height else size
    size = size_x if size_x < size_x else size_y
    # 创建矩形窗,左-上-右-下
    box = (sp[0], sp[1], sp[0] + size, sp[1] + size)
    # 裁剪窗口
    region = im.crop(box)
    region = region.transpose(angle)
    im.paste(region, box)
    return save_img(im, filename)


# 图片水印
def water_mask(filename: str, mask_filename: str):
    # 获取图像
    im = get_img(filename)
    width, height = im.size

    # 获取水印图片
    mask_filename = convert_img(filename, mask_filename)
    mask_im = get_img(mask_filename)
    mw, mh = mask_im.size
    mw, mh = 250, int(mh * 250 / mw)
    mask_im = mask_im.resize((mw, mh))

    # 裁剪原来的图像区域并混叠
    region = im.crop((width - mw, height - mh, width, height))
    new = Image.blend(mask_im, region, 0.5)

    im.paste(new, (width - mw, height - mh))

    return save_img(im, filename)


# 文字水印
def text_mask(filename, text, color, font_size, start_point):
    olddata = text + '#' + color + '#' + font_size + '#' + start_point[0] + '#' + start_point[1]
    im = get_img(filename)
    draw = ImageDraw.ImageDraw(im)
    font = ImageFont.truetype(font=basedir + '/static/font/STHeiti-Light-3.ttc', size=int(font_size), encoding='utf-8')
    if color in ImageColor.colormap:
        color = ImageColor.getrgb(color)
    else:
        color = ImageColor.getrgb('red')
    draw.text((int(start_point[0]), int(start_point[1])), text, fill=color, font=font)
    return save_img(im, filename), olddata


# 图像叠加
def overlay(filename1, filename2, alpha: float):
    im1 = get_img(filename1)
    im2 = get_img(filename2)
    w = im1.size[0] if im1.size[0] > im2.size[0] else im2.size[0]
    h = im1.size[1] if im1.size[1] > im2.size[1] else im2.size[1]
    size = (w, h)
    base1 = Image.new('RGB', size, ImageColor.getrgb('white'))
    base2 = Image.new('RGB', size, ImageColor.getrgb('white'))
    base1.paste(im1, (0, 0))
    base2.paste(im2, (0, 0))
    base1.show()
    base2.show()

    res = Image.blend(base1, base2, alpha)
    res.show()
    return save_img(res, filename1)


if __name__ == '__main__':
    overlay('jjy.jpg', 'jjy2.jpg', 0.5)
