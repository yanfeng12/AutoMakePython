

from PIL import Image


catIm = Image.open('zophie.png')
catCopyIm = catIm.copy()

faceIm = catIm.crop((335, 345, 565, 560))

#catIm.paste(faceIm, (400, 500))
#catIm.save('pasted.png')


catCopyIm.paste(faceIm, (400, 500))
catCopyIm.save('pasted2.png')
