import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('14545645.jpg' ,1)
b=cv2.imread('14545645.jpg' ,1)
b[90:100,90:100,0]=0
b[100:50,60:80,1]=0
b[50:60,30:50,2]=0
print(b)

#roi=img[77:122,640:788]
#img[149:194,460:608]=roi

#img1=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.imshow(b)
#plt.xticks([]), plt.yticks([])
plt.show()

 #cv2.namedWindow('14545645',cv2.WINDOW_NORMAL)
 #cv2.imshow('14545645',img)
 #cv2.imwrite('14545645.jpg',img)
 #cv2.waitKey(0)
 #cv2.destroyAllWindows()