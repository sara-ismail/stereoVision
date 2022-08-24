import cv2
import camera_stream

cap = camera_stream.CameraVideoStream()
cap2 = camera_stream.CameraVideoStream()

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

