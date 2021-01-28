import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('14545645.jpg',1)
#Import only if not previously imported
import cv2

img1 = cv2.cvtColor(imag,cv2.COLOR_BGR2RGB)
print(img)
plt.imshow(img1)
plt.xticks([]),plt.yticks([])
plt.show()
#cv2.namedWindow('14545645',cv2.WINDOW_NORMAL)
#cv2.imshow('test',img)
#cv2.imwrite('158.jpg',img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()