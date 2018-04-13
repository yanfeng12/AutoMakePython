from PIL import Image


LOGO_FILENAME = 'catlogo.png'


logoIm = Image.open(LOGO_FILENAME)
logoWidth, logoHeight = logoIm.size
resizelogoIm = logoIm.resize((int(logoWidth/25), int(logoHeight/25)))
resizelogoIm.save('resizelogo.png')
