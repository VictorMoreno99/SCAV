import cv2

path = path = '/home/worca/PycharmProjects/SCAV/P1/lena.png'
img = cv2.imread(path)  # We load the image
img_bw = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)  # We convert the image from RGB to Grayscale
th, im_th = cv2.threshold(img_bw, 128, 255, cv2.THRESH_BINARY)  # We binarize the image
cv2.imwrite('lena_bw.png', im_th)  # We put the result into an image
