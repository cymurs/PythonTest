import cv2
import numpy as np

img = cv2.imread('pic/imgROI/face.jpg')
print img.item(150, 120, 0)
img.itemset( (150, 120, 0), 255)
print img.item(150, 120, 0)
cv2.imwrite('pic/imgROI/fakeFace.jpg', img)