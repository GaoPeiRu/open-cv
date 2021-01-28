import numpy as np
from matplotlib import pyplot as plt 

img = cv2.imread('test.jpg',0)
img = cv2.imread('test.jpg',1)

img1 = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

print(img)
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic') 
plt.imshow(img1) 
plt.xticks([]), plt.yticks([]) 
plt.show()