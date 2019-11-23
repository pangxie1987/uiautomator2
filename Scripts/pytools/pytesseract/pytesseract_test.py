# -*- coding:utf-8 -*-
'''
识别图片中的文字
https://www.cnblogs.com/yeayee/p/4955506.html
https://blog.csdn.net/u013401853/article/details/78998206
'''
import pytesseract
import requests
import os
from PIL import Image

imagepath = os.path.join(os.path.dirname(__file__),'2470773-44c5687231501a36.jpg')
print(imagepath)


def get_image():
    '下载图片'
    r = requests.get(url='https://d1h3p5fzmizjvp.cloudfront.net/themes/katalon_4/images/katalon_template_1809/logo@2x.png')
    with open(imagepath,'wb') as f:
        f.write(r.content)

def get_code():
    '识别文字'
    image = Image.open(imagepath)
    code = pytesseract.image_to_string(image)
    print('The Code is:',code)

def removeLine(imgName):
    (img, pixdata) = open_img(imgName)
    for x in range(img.size[0]):  # x坐标
        for y in range(img.size[1]):  # y坐标
            if pixdata[x, y][0] < 8 or pixdata[x, y][1] < 6 or pixdata[x, y][2] < 8 or (
                    pixdata[x, y][0] + pixdata[x, y][1] + pixdata[x, y][2]) <= 30:  # 确定颜色阈值
                if y == 0:
                    pixdata[x, y] = (255, 255, 255)
                if y > 0:
                    if pixdata[x, y - 1][0] > 120 or pixdata[x, y - 1][1] > 136 or pixdata[x, y - 1][2] > 120:
                        pixdata[x, y] = (255, 255, 255)  # ?

    # 二值化处理
    for y in range(img.size[1]):  # 二值化处理，这个阈值为R=95，G=95，B=95
        for x in range(img.size[0]):
            if pixdata[x, y][0] < 160 and pixdata[x, y][1] < 160 and pixdata[x, y][2] < 160:
                pixdata[x, y] = (0, 0, 0)
            else:
                pixdata[x, y] = (255, 255, 255)
    img.filter(ImageFilter.EDGE_ENHANCE_MORE)  # 深度边缘增强滤波，会使得图像中边缘部分更加明显（阈值更大），相当于锐化滤波
    img.resize(((img.size[0]) * 2, (img.size[1]) * 2), Image.BILINEAR)  # Image.BILINEAR指定采用双线性法对像素点插值#?
    img.save('remove-' + imgName)
    print("除线成功！")

if __name__ == '__main__':
    #get_image()
    get_code()