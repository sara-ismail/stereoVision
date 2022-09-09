import numpy as np
import cv2
import time
import camera_stream
 

cap = camera_stream.CameraVideoStream("thetauvcsrc ! decodebin ! autovideoconvert ! video/x-raw,format=BGRx ! videoconvert ! video/x-raw,format=BGR ! appsink", cv2.CAP_GSTREAMER)
cap2 = camera_stream.CameraVideoStream("thetauvcsrc ! decodebin ! autovideoconvert ! video/x-raw,format=BGRx ! videoconvert ! video/x-raw,format=BGR ! appsink", cv2.CAP_GSTREAMER)

cv2.namedWindow("Stream 1", cv2.WINDOW_NORMAL)
cv2.namedWindow("Stream 2", cv2.WINDOW_NORMAL)

prev_frame_time = 0
new_frame_time = 0

font = cv2.FONT_HERSHEY_SIMPLEX

while(cap.isOpened() and cap2.isOpened()):
 
    ret, frame = cap.read()
    frame = cv2.flip(framef, -1)

    ret2, frame2 = cap2.read()

    if not (ret or ret2):
        break
 
    new_frame_time = time.time()

    fps = 1/(new_frame_time-prev_frame_time)
    prev_frame_time = new_frame_time
 
    fps = int(fps)
    fps = str(fps)

    cv2.putText(frame, fps, (7, 70), font, 3, (100, 255, 0), 3, cv2.LINE_AA)
    cv2.putText(frame2, fps, (7, 70), font, 3, (100, 255, 0), 3, cv2.LINE_AA)

    cv2.imshow('Stream 1', frame)
    cv2.imshow('Stream 2', frame2)

    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

cap.release()
cap2.release()

cv2.destroyAllWindows()