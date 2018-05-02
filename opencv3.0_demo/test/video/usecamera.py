#-*- coding:utf-8 -*-
__author__ = 'Administrator'


import cv2

cameraCapture = cv2.VideoCapture(0)
fps = 30
size = (int(cameraCapture.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(cameraCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
videoWriter = cv2.VideoWriter(
    'MyCameraVid.avi', cv2.VideoWriter_fourcc('I', '4', '2', '0'), fps, size
)

success, frame = cameraCapture.read()
numFramesRemaining = 5 * fps - 1
while success and numFramesRemaining > 0:
    videoWriter.write(frame)
    success, frame = cameraCapture.read()
    numFramesRemaining -= 1
cameraCapture.release()