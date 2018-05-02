#-*- coding:utf-8 -*-
__author__ = 'Administrator'

import cv2

video = '9.avi' #u'放炮.mp4'
videoCapture = cv2.VideoCapture(video.encode('gb18030')) #('MyInputVid.avi')
fps = videoCapture.get(cv2.CAP_PROP_FPS)
size = (int(videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(videoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
videoWriter = cv2.VideoWriter('MyOutputVid.avi', cv2.VideoWriter_fourcc('F', 'L', 'V', '1'), fps, size)

success, frame = videoCapture.read()
while success :
    videoWriter.write(frame)
    success, frame = videoCapture.read()
