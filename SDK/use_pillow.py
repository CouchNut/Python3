#!/usr/local/bin python3

# -*- coding: utf-8 -*-

from PIL import Image, ImageFilter, ImageFont, ImageDraw

# 打开一个jpg图像文件， 注意是当前路径：
img = Image.open('test.png')
# 获得图像尺寸
imgW, imgH = img.size
print('Original image size : %s x %s' % (imgW, imgH))
# 缩放到 50%
img.thumbnail((imgW//2, imgH // 2))
print('Resize image to: %s x %s' % (imgW//2, imgH // 2))
# 把缩放后的图像用jpeg格式保存
img.save('thumbnail.jpg', 'png')

# 模糊效果
img2 = img.filter(ImageFilter.BLUR)
img2.save('blur.jpg', 'png')

# 绘图方法
import random

# 随机字符
def rndChar():
	return chr(random.randint(65, 90))

# 随机颜色1
def rndColor():
	return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

def rndColor2():
	return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

# 240 x 60:
width = 60 * 4
height = 60

image = Image.new('RGB', (width, height), (255, 255, 255))
# 创建Font对象
font = ImageFont.truetype('Arial.ttf', 36)
# 创建Draw对象
draw = ImageDraw.Draw(image)
# 填充每个像素
for x in range(width):
	for y in range(height):
		draw.point((x, y), fill=rndColor())

# 输出文字
for t in range(4):
	draw.text((60 * t + 10, 10), rndChar(), font=font, fill = rndColor2())

# 模糊
image = image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg')





