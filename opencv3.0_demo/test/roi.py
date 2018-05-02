# coding:utf-8
import cv2
import numpy as np
img = cv2.imread('pic/imgROI/face.jpg')
print img.shape
print img.size
print img.dtype
myRoi = img[0:100, 0:100]
img[300:400, 300:400] = myRoi

imgcopy = img.copy()
imgcopy = cv2.cvtColor(imgcopy, cv2.COLOR_BGR2GRAY)
print imgcopy.shape

wname = u'补丁'
cv2.imshow(wname.encode('gb18030'), img)
cv2.waitKey()
cv2.destroyAllWindows()