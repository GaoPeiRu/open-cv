import cv2
import numpy as np
from matplotlib import pyplot as plt 

img = cv2.imread('14545645.jpg',0)
img = cv2.imread('14545645.jpg',1)

img1 = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

print(img)
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic') 
plt.imshow(img1) 
plt.xticks([]), plt.yticks([]) 
plt.show()