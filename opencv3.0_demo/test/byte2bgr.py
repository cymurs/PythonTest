import cv2
import numpy
import os

# Make an array of 120000 random bytes.
randomByteArray = bytearray(os.urandom(120000))
flatNumpyArray = numpy.array(randomByteArray)

# Convert the array to make a 400 * 300 grayscale image.
grayImage = flatNumpyArray.reshape(300, 400)
cv2.imwrite('img/RandomGray.png', grayImage)

# Convert the array to make a 400 * 100 color image
bgrImage = flatNumpyArray.reshape(100, 400, 3)
cv2.imwrite('img/RandomColor.png', bgrImage)

