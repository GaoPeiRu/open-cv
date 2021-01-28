import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('14545645.jpg' ,1)

roi=img[77:122,640:788]
img[149:194,460:608]=roi

img1=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.imshow(img1)
plt.xticks([]), plt.yticks([])
plt.show()