# coding=utf-8
import cv2
import numpy as np
img = cv2.imread('pic/imgROI/face.jpg')

# erase green
tmp = img.copy()
tmp[:, :, 0] = 0
b = '没有蓝色'  # str格式字符串
cv2.imshow(b.decode('utf-8').encode('gb18030'), tmp)
cv2.imwrite('pic\\imgROI\\noBlueFace.jpg', tmp)


# erase green
tmp = img.copy()
tmp[:, :, 1] = 0
g = u'没有绿色' # unicode格式字符串
cv2.imshow(g.encode('gb18030'), tmp)
cv2.imwrite('pic/imgROI/noGreenFace.jpg', tmp)
# cv2.waitKey()


# erase red
tmp = img.copy()
tmp[:, :, 2] = 0
r = '没有红色'  # str格式字符串
cv2.imshow(r.decode('utf-8').encode('gb18030'), tmp)
cv2.imwrite('pic\\imgROI\\noRedFace.jpg', tmp)
cv2.waitKey()
cv2.destroyAllWindows()


