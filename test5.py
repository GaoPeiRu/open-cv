import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('158.jpg',1)

roi=img[640:788,77:122]
img[460:607,146:191]=roi

img1=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
Plt.imshow(img1)
plt.xticks([]), plt.yticks([])
plt.show()