from PIL import Image
from resizeimage import resizeimge
fd_img = open('image1.jpeg','r')
img=Image.open(fd_img)
img = resizeimage.resize_crop(img,[200,200])
img.save('image1.jpeg',img.format)
fd_img.close()
