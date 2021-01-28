import cv2
import numpy as np
from matplotlib import pyplot as plt 

img = cv2.imread('14545645.jpg',1)
b = cv2.imread('14545645.jpg',1)
img1 = b[60:70,10:30]
img2 = b[10:20,70:90]
print(img1)
print(img2)
dst=cv2.addWeighted(img1,0.3,img2,0.7,0)
b[10:20,70:90]=dst
cv2.namedWindow('14545645',cv2.WINDOW_NORMAL)
cv2.imshow('14545645',img)
cv2.imshow('b',b)


cv2.waitKey(0)
cv2.destroyAllWindows()