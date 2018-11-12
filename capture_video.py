#!/usr/bin/python3
import cv2
import numpy as np

# time.txt中行数
n = 10
for i in range(0,n):
    # name="4_4"+str(i)+".mp4"
    name=str(i)+".mp4" 
    videoCapture=cv2.VideoCapture(name)

    if (videoCapture.isOpened()):
        print('Open')
    else:
        print('Fail to open!')

    fps = videoCapture.get(cv2.CAP_PROP_FPS)  # 获取原视频的帧率

    size1 = (int(114), int(144))
    size2 = (int(577),int(450))# 自定义需要截取的画面的大小
    #size = (int(videoCapture.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)),int(videoCapture.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)))#获取原视频帧的大小
    videoWriter1 = cv2.VideoWriter("hand"+str(i)+".avi", cv2.VideoWriter_fourcc(*'MJPG'), fps, size1)
    videoWriter2 = cv2.VideoWriter("video"+str(i)+".avi", cv2.VideoWriter_fourcc(*'MJPG'), fps, size2)

    success,frame = videoCapture.read()

    while success:
        frame1= frame[374:518, 29:143]
        frame2 = frame[:450,143:]# 截取画面
        videoWriter1.write(frame1)
        videoWriter2.write(frame2)# 将截取到的画面写入“新视频”
        success, frame = videoCapture.read() # 循环读取下一帧
    videoCapture.release()
    print("Close")
