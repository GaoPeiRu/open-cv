import cv2
import numpy as np
img = cv2.imread('14545645.jpg',1)
print(img)
cv2.namedWindow('14545645',cv2.WINDOW_NORMAL)
cv2.imshow('test',img)
cv2.imwrite('158.jpg',img)
cv2.waitKey(0)
cv2.destroyAllWindows()