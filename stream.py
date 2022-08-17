import cv2

cap = cv2.VideoCapture("thetauvcsrc ! decodebin ! autovideoconvert ! video/x-raw,format=BGRx ! videoconvert ! video/x-raw,format=BGR ! appsink")
cap2 = cv2.VideoCapture("thetauvcsrc ! decodebin ! autovideoconvert ! video/x-raw,format=BGRx ! videoconvert ! video/x-raw,format=BGR ! appsink")

cv2.namedWindow("Stream 1", cv2.WINDOW_NORMAL)
cv2.namedWindow("Stream 2", cv2.WINDOW_NORMAL)


while True:
    ret, frame = cap.read()
    ret2, frame2 = cap2.read()

    if (ret and ret2):
        cv2.imshow('Stream 1', frame)
        cv2.imshow('Stream 2', frame2)
        if cv2.waitKey(20) & 0xFF==ord('q'):
            break
    else:
        break

cap.release()
cap2.release()

cv2.destroyAllWindows()

