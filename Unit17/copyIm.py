

from PIL import Image
im1 = Image.open("zophie.png")
box = [335, 345, 565, 560]
im_crop = im1.crop(box)
im1.paste(im_crop,(200,200))  #等价于im1.paste(im_crop,(200,200))
im1.save("he.jpg")
