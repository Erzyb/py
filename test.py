# -*- coding:utf-8 -*-
# __author__ = 'zhouyibo'

'''
在图像右上角添加红色数字
导入pil失败
使用终端导入失败  使用终端搜索 pillow ->Python Imaging Library
错误记录：
draw.text 参数中  text 必须为string
truetype方法中 第一个参数不可为空
try except 程序健壮
'''

from PIL import Image, ImageDraw, ImageFont

original_image = 'weChat_avatar.png'
new_image ='new_avatar.png'
color = (255,0,0)

def draw_text(text,color):
    im = Image.open(original_image)
    x,y = im.size
    im.show()

    draw = ImageDraw.Draw(im)
    fonts = ImageFont.truetype('Arial.ttf',35)
    draw.text((x-20,7),text,color,fonts)

    im.save(new_image)
    im.show()

if __name__ == '__main__':
    draw_text('4',color)

# from PIL import Image, ImageDraw, ImageFont
#
# original_avatar = 'weChat_avatar.png'
# saved_avatar = 'new_avatar.png'
# windows_font = 'Arial.ttf'
# color = (255, 0, 0)
#
#
# def draw_text(text, fill_color, windows_font):
#     try:
#         im = Image.open(original_avatar)
#         x, y = im.size
#         print "The size of the Image is: "
#         print(im.format, im.size, im.mode)
#         im.show()
#
#         draw = ImageDraw.Draw(im)
#         font = ImageFont.truetype(windows_font, 35)
#         draw.text((x - 20, 7), text, fill_color, font)
#
#         im.save(saved_avatar)
#         im.show()
#
#     except:
#         print "Unable to load image"
#
#
# if __name__ == "__main__":
#     # number = str(raw_input('please input number: '))
#     number = str(4)
#     draw_text(number, color, windows_font)