import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread("/home/aditya/DIP/PRACTICE/DIP17_1_Images/redball.jpg")
(height,width,column) = img.shape
color = ('b','g','r')
for i,col in enumerate(color):
    histr = cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
plt.show()
for h in range(height):
    for w in range(width):
        if (img[h,w,0] >=160 and img[h,w,1] >= 160 and img[h,w,2] >= 160):
            img[h][w][0] = 0
            img[h][w][1] = 0
            img[h][w][2] = 0

cv2.imwrite("/home/aditya/DIP/PRACTICE/DIP17_1_Images/redball_background_removed.jpg",img)

