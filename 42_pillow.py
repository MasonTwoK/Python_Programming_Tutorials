from PIL import Image
from PIL import ImageFilter

img1 = Image.open('images.jpg')
blur = img1.filter(ImageFilter.BLUR)
contour = img1.filter(ImageFilter.CONTOUR)
ditail = img1.filter(ImageFilter.DETAIL)

blur.show()
contour.show()
ditail.show()