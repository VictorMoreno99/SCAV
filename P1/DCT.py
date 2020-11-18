from scipy.fftpack import dct, idct
import numpy as np
import matplotlib.pylab as plt
import cv2


# implement 2D DCT
def dct2(a):
    return dct(dct(a.T, norm='ortho').T, norm='ortho')


# implement 2D IDCT
def idct2(a):
    return idct(idct(a.T, norm='ortho').T, norm='ortho')


# read lena RGB image and convert to grayscale
path = '/home/worca/PycharmProjects/SCAV/P1/lena.png'
img = cv2.imread(path)  # We load the image
img_grey = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)  # We convert it from RGB to grayscale
imF = dct2(img_grey)  # We compute the dct of that image
im1 = idct2(imF)  # We compute the inverse dct to recover the image

# We check if the reconstructed image is nearly equal to the original image
np.allclose(img_grey, im1)
# True

# We plot the original and reconstructed images
plt.gray()
plt.subplot(121), plt.imshow(img_grey), plt.axis('off'), plt.title('original', size=20)
plt.subplot(122), plt.imshow(im1), plt.axis('off'), plt.title('reconstructed', size=20)
plt.show()
