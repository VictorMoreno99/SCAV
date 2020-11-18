import numpy as np
import cv2

path = path = '/home/worca/PycharmProjects/SCAV/P1/lena.png'
img = cv2.imread(path)  # We load the image
r1, g1, b1 = cv2.split(img)  # We get each channel of the RGB image
img_yuv = cv2.cvtColor(img, cv2.COLOR_RGB2YUV)  # We convert the RGB image into a YUV image
y, u, v = cv2.split(img_yuv)  # We get each channel of the YUV image
img_rgb = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2RGB)  # We reconvert the YUV image into an RGB image
r2, g2, b2 = cv2.split(img_rgb)  # We get the channels of the reconverted RBG image

result = np.vstack([img, img_yuv, img_rgb])  # We stack the 3 images: Original RGB, YUV, Reconverted RGB

cv2.imwrite('lena_rgb_yuv_rgb.png', result)  # We put them in an image
