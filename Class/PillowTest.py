from PIL import Image

im = Image.open('abc.jpg')
print(im.format, im.size, im.mode)

im.thumbnail((192, 120))
im.save('thumb.jpg', 'JPEG')
