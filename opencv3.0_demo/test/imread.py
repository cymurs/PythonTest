import cv2

image = cv2.imread('pic/edgeDetection/littleDog.jpg')
cv2.imwrite('pic/==outputImage/dog.jpg', image)
raw_input()
