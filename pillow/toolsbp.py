from time import time

from flask import Blueprint, request, redirect, url_for, render_template

from utils.utils import save_file, resize

from pillow.tools import mosaic, overlay, water_mask, text_mask

tools_bp = Blueprint('tools_bp', __name__, url_prefix='/tools')


@tools_bp.route('/tools_result')
def tools_result():
    back = request.args.get('back')
    filename = request.args.get('filename')
    res_filename = request.args.get('res_filename')
    olddata = request.args.get('olddata')
    data = {
        'time': time(),
        'back': back,
        'filename': filename,
        'res_filename': res_filename,
        'olddata': olddata
    }
    return render_template('tools/result.html', **data)


@tools_bp.route('/resize', methods=['GET', 'POST'])
def resize_img():
    if request.method == 'POST':
        filename = request.form.get('filename')
        if filename is None:
            img = request.files['image']
            filename = save_file(img)

        prop = float(request.form.get('proportion'))
        if prop < 0.1:
            raise Exception('比例系数不合法!')
        res_filename = resize(filename, proportion=prop)
        args = {
            'back': 'tools_bp.resize_img',
            'filename': filename,
            'res_filename': res_filename,
            'olddata': prop
        }
        return redirect(url_for('tools_bp.tools_result', **args))
    else:
        return render_template('tools/resize.html')


@tools_bp.route('/mosaic', methods=['GET', 'POST'])
def mosaic_img():
    if request.method == 'POST':
        # 获取文件名
        filename = request.form.get('filename')
        if filename is None:
            im = request.files['image']
            filename = save_file(im)
        # 获取参数
        startx = request.form.get('startx')
        starty = request.form.get('starty')
        endx = request.form.get('endx')
        endy = request.form.get('endy')
        granularity = int(request.form.get('g'))
        res_filename, olddata = mosaic(filename, [startx, starty], [endx, endy], granularity)
        args = {
            'back': 'tools_bp.mosaic_img',
            'filename': filename,
            'res_filename': res_filename,
            'olddata': olddata
        }
        return redirect(url_for('tools_bp.tools_result', **args))
    else:
        return render_template('tools/mosaic.html')


@tools_bp.route('/blend', methods=['GET', 'POST'])
def blend_img():
    if request.method == "POST":
        file1 = request.form.get('file1', None)
        file2 = request.form.get('file2', None)
        if file1 is None or file2 is None:
            # 获取图像并保存
            im1 = request.files['image1']
            im2 = request.files['image2']
            file1 = save_file(im1)
            file2 = save_file(im2)
        # 获取alpha
        alpha = request.form['alpha']
        res_filename = overlay(file1, file2, float(alpha))
        args = {
            'back': 'tools_bp.blend_img',
            'file1': file1,
            'file2': file2,
            'res_filename': res_filename,
            'time': time(),
            'olddata': alpha
        }
        return redirect(url_for('tools_bp.blend_result', **args))
    else:
        return render_template('tools/blend.html')


@tools_bp.route('/blend_result')
def blend_result():
    back = request.args.get('back')
    file1 = request.args.get('file1')
    file2 = request.args.get('file2')
    res_filename = request.args.get('res_filename')
    current_time = request.args.get('time')
    olddata = request.args.get('olddata')
    return render_template(
        'tools/blend_result.html',
        back=back,
        file1=file1,
        file2=file2,
        res_filename=res_filename,
        time=current_time,
        olddata=olddata
    )


@tools_bp.route('/water_mask', methods=['GET', 'POST'])
def water_mask_img():
    if request.method == 'POST':
        mask_type = request.form.get('type')
        file1 = request.form.get('file1')
        file2 = request.form.get("file2")
        if file1 is None:
            # 获取原始图像数据
            im1 = request.files['image1']
            file1 = save_file(im1)

        olddata = ''

        if mask_type == 'logo':
            if file2 is None:
                # Logo水印
                logo = request.files['image2']
                file2 = save_file(logo)
            res_filename = water_mask(file1, file2)

        else:
            # 获取文字水印内容
            text = request.form.get('text')
            color = request.form.get('color')
            font_size = request.form.get('font_size')
            x = request.form.get('x')
            y = request.form.get('y')
            res_filename, olddata = text_mask(file1, text, color, font_size, (x, y))

        args = {
            'back': 'tools_bp.water_mask_img',
            'res_filename': res_filename,
            'file1': file1,
            'file2': file2,
            'time': time(),
            'olddata': olddata
        }
        return redirect(url_for('tools_bp.water_mask_result', **args))

    else:
        return render_template('tools/water_mask.html')


@tools_bp.route('/water_mask_result')
def water_mask_result():
    back = request.args.get('back')
    file1 = request.args.get('file1')
    file2 = request.args.get('file2')
    res_filename = request.args.get('res_filename')
    current_time = request.args.get('time')
    olddata = request.args.get('olddata')
    return render_template(
        'tools/water_mask_result.html',
        back=back,
        file1=file1,
        file2=file2,
        res_filename=res_filename,
        time=current_time,
        olddata=olddata
    )
