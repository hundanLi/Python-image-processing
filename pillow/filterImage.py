from PIL import ImageFilter, ImageEnhance
from exception import NotExistEnhanceError
from utils.utils import get_img, get_filter, save_img


def img_filter(form, filename, **kwargs):
    mode = kwargs.get('mode', None)

    img = get_img(filename)

    # 读取滤波方式
    im_filter, olddata = get_filter(mode, form)

    # 滤波处理
    res = img.filter(im_filter)
    # 返回处理后文件名称和原始参数
    return save_img(res, filename), olddata


def img_enhance(filename, enhance_type, factor):
    im = get_img(filename)
    if enhance_type == 'Color':
        enhancer = ImageEnhance.Color(im)
    elif enhance_type == 'Contrast':
        enhancer = ImageEnhance.Contrast(im)
    elif enhance_type == 'Brightness':
        enhancer = ImageEnhance.Brightness(im)
    elif enhance_type == 'Sharpness':
        enhancer = ImageEnhance.Sharpness(im)
    else:
        raise NotExistEnhanceError()
    res = enhancer.enhance(factor)
    return save_img(res, filename)


def img_kernel(filename, size, kernel, scale=None, offset=None):
    im = get_img(filename)
    if scale is not None and scale.strip() != '':
        scale = float(scale)
    else:
        scale = None
    if offset is not None and offset.strip() != '':
        offset = float(offset)
    else:
        offset = 0
    im_filter = ImageFilter.Kernel(size, kernel, scale, offset)
    res = im.filter(im_filter)
    return save_img(res, filename)


if __name__ == '__main__':
    pass
    # i = get_img('jpg')
    # filter_type = ImageFilter.GaussianBlur(radius=-1)
    # res = i.pillow(filter_type)
    # i.show()
    # res.show()
