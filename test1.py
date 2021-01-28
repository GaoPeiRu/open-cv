import cv2
import numpy as np
cap = cv2.VideoCapture(0)
#Import only if not previously imported
if cap.isOpened()==False:
    print("Error in opening video stream or file")
fourcc=cv.VideoWriter_fourcc("Fourcc Codec Eg-XVID")
writer = cv2.VideoWriter('14545645.avi',fourcc,30,int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))
while cap.isOpened():
    ret,frame=cap.read()
    if ret:
        writer.write(frame)
        cv2.imshow("Frame",frame)
        if cv2.waitKey(20) & 0xFF==27:
            break
    else:
        break
cap.release()
writer.release()
cv2.