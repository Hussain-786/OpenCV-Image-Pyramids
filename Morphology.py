import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('smarties.png', 0)
_,mask = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY_INV)
kernal = np.ones((2,2), np.uint8)
dilation = cv2.dilate(mask,  kernal, iterations=2)
erosion = cv2.erode(mask, kernal, iterations=2)
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernal)
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernal)
gradient = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernal)
blackhat = cv2.morphologyEx(mask, cv2.MORPH_BLACKHAT, kernal)
titles = ['original image', 'mask', 'dilation','erosion', 'opening','closing','gradient', 'blackhat']
images = [img, mask, dilation,erosion,opening,closing,gradient,blackhat]
for i in range(8):
    plt.subplot(2,4,i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])
plt.show()