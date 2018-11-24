import os
from PIL import ImageFilter

# 项目根目录
BASE_DIR = basedir = os.path.abspath(os.path.dirname(__file__))

FIlTER_DICT = {
    'RankFilter': ImageFilter.RankFilter,
    'MedianFilter': ImageFilter.MedianFilter,
    'MinFilter': ImageFilter.MinFilter,
    'MaxFilter': ImageFilter.MaxFilter,
    'ModeFilter': ImageFilter.ModeFilter,
    'GaussianBlur': ImageFilter.GaussianBlur,
    'BoxBlur': ImageFilter.BoxBlur,
    'UnsharpMask': ImageFilter.UnsharpMask,
    'BLUR': ImageFilter.BLUR,
    'CONTOUR': ImageFilter.CONTOUR,
    'DETAIL': ImageFilter.DETAIL,
    'EDGE_ENHANCE': ImageFilter.EDGE_ENHANCE,
    'EDGE_ENHANCE_MORE': ImageFilter.EDGE_ENHANCE_MORE,
    'EMBOSS': ImageFilter.EMBOSS,
    'FIND_EDGES': ImageFilter.FIND_EDGES,
    'SHARPEN': ImageFilter.SHARPEN,
    'SMOOTH': ImageFilter.SMOOTH,
    'SMOOTH_MORE': ImageFilter.SMOOTH_MORE
}

SECRET_KEY = b'_\xd5.\x15D6\xbd\xfe\xd8\x9c}\x97\x18K>9K\xe6\xf0\x7f)\xc7\x00\xf3'

img_dir = BASE_DIR + '/static/images/'

upload_dir = BASE_DIR + '/static/images/'

ALLOW_FILE = ['jpg', 'jpeg', 'png', 'gif', 'ico', 'bmp', 'tif', 'pcx', 'tga', 'exif', 'fpx', 'svg', 'psd', 'cdr', 'pcd',
              'dxf', 'ufo', 'eps', 'ai', 'raw', 'wmf', 'webp']
