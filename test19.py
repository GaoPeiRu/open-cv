import cv2
import numpy as np
def nothing(x):
    pass

img = cv2.imread('test13.jpg', 0)
cv2.imshow('image13', img)
edges = cv2.Canny(img, 50, 100)
cv2.namedWindow('image')
cv2.createTrackbar('minval', 'image', 0, 255, nothing)
cv2.createTrackbar('maxval', 'image', 0, 255, nothing)

while(1):
    cv2.imshow('image', edges)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    minval = cv2.getTrackbarPos('minval', 'image')
    maxval = cv2.getTrackbarPos('maxval', 'image')
    edges = cv2.Canny(img, minval, maxval)

cv2.destroyAllWindows()


import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('test6.jpg', 0)
edges = cv2.Canny(img, 50, 100)
edges2 = cv2.Canny(img, 50, 150)
edges3 = cv2.Canny(img, 50, 200)
edges4 = cv2.Canny(img, 100, 150)
edges5 = cv2.Canny(img, 200, 250)