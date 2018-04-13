from PIL import Image


catIm = Image.open('zophie.png')
catImWidth, catImHeight = catIm.size
faceIm = catIm.crop((335, 345, 565, 560))
faceImWidth, faceImHeight = faceIm.size
catCopyTwo = catIm.copy()


for left in range(0, catImWidth, faceImWidth):
    for top in range(0, catImHeight, faceImHeight):
        print(left, top)
        catCopyTwo.paste(faceIm, (left, top))
catCopyTwo.save('tiled.png')
