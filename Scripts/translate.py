'''
tkinter+PIL+googletrans
对剪贴板上图片进行翻译
'''

# 安装PIL依赖
# 从剪贴板读取图片
import tkinter.messagebox
import tkinter as tki
import pytesseract
from PIL import Image
from PIL import ImageGrab
from googletrans import Translator

img = ImageGrab.grabclipboard()

if img and isinstance(img, Image.Image):
	# 保存到本地
	imgage_result = './temp.png'
	img.save(imgage_result)

	# OCR 识别
	# 识别图片中的英文

	content_eng = pytesseract.image_to_string(Image.open(imgage_result), lang='eng')

	# 翻译
	# Google翻译
	translator = Translator(service_urls=['translate.google.cn'])

	# 翻译成中文
	content_chinese = translator.translate(content_eng, src='en', dest='zh-cn').text

	# 初始化
	root = tki.Tk()
	root.withdraw()

	# 显示翻译后的结果， 以对话框的形式
	tkinter.messagebox.showinfo('翻译结果', content_chinese)
else:
	tkinter.messagebox.showinfo('翻译结果','剪贴板无数据')