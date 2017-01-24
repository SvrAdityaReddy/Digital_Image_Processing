import numpy as np
import cv2

img = cv2.imread("/home/aditya/DIP/DIP17_1_Images/1944.jpg")
img_B=cv2.imwrite("/home/aditya/DIP/DIP17_1_Images/1944_B.jpg",img[:,:,0])
img_G=cv2.imwrite("/home/aditya/DIP/DIP17_1_Images/1944_G.jpg",img[:,:,1])
img_R=cv2.imwrite("/home/aditya/DIP/DIP17_1_Images/1944_R.jpg",img[:,:,2])
# img_grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# cv2.imshow('image',img_grey)
# cv2.waitKey()
# print img_grey
#print img
#cv2.imshow('image',img)
img_grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imwrite("/home/aditya/DIP/DIP17_1_Images/194_GREY.jpg",img_grey)
#cv2.waitKey()
#print img[:,:,0]
# print len(img)
# print len(img[:,:,0])