import cv2
import numpy as np

img=np.zeros(512,512,3), np.uint8)
cv2.line(img,(0,0),(500,500),(255,0,255),5)
cv2.rectangle(img,(100,100),(300,300),(0,255,0),5)

cv2.imshow("Window Name",img)
cv2.waitKey(0)
cv2.destroyAllWindows()