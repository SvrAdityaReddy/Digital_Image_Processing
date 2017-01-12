import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread("/home/aditya/DIP/PRACTICE/DIP17_1_Images/redball.jpg")
# img = img.astype(int)
# img_grey=cv2.cvtColor(img,cv2.COLOR_BGR2YUV)
(height,width,column) = img.shape
for h in range(height):
    for w in range(width):
        b = img[h][w][0]
        g = img[h][w][1]
        r = img[h][w][2]
        # c = (255*((int(g) + int(b)) & 255)) & 255
        # m = (255*((int(r) + int(b)) & 255)) & 255
        # y = (255*((int(g) + int(r)) & 255)) & 255
        c = 255 - r
        m = 255 - g
        y = 255 - b
        # c = (int(255 - r) * (255*(int(g) + int(b)))) & 255
        # m = (int(255 - g) * (255*(int(r) + int(b)))) & 255
        # y = (int(255 - b) * (255*(int(g) + int(r)))) & 255
        img[h,w,0] = y
        img[h,w,1] = m
        img[h,w,2] = c
# img.astype(uint8)
        # print img[h,w,:]
# cv2.imshow("Image",img)
# cv2.waitKey()         
cv2.imwrite("/home/aditya/DIP/PRACTICE/DIP17_1_Images/redball_cmy.jpg",img)

