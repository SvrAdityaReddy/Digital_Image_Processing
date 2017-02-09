import numpy as np
import cv2
from matplotlib import pyplot as plt



img1 = cv2.imread("/home/aditya/diptemp/cameraman_grey.png")
img1 = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
# print img1.shape
img2 = cv2.imread("/home/aditya/diptemp/lena.jpg")
img2_grey=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
# print img1_grey.shape
# cv2.imwrite("/home/aditya/diptemp/nature_grey.jpg",img2_grey)
small = cv2.resize(img1, (0,0), fx=0.5, fy=0.5)
interpolated = cv2.resize(small,(0,0) ,fx=2,fy=2,interpolation=cv2.INTER_NEAREST) 
small2 = cv2.resize(img2_grey, (0,0), fx=0.5, fy=0.5)
interpolated2 = cv2.resize(small2,(0,0) ,fx=2,fy=2,interpolation=cv2.INTER_NEAREST) 
# print small.shape

cv2.imwrite("/home/aditya/diptemp/cameraman_near.png",interpolated)
cv2.imwrite("/home/aditya/diptemp/lena_near.jpg",interpolated2)



energy_original = np.sum(img1,dtype=np.int32)
energy_interpolated = np.sum(interpolated,dtype=np.int32)
Energy_Difference = energy_original - energy_interpolated
print "Interpolation using nearest neighbour"
print Energy_Difference
print abs(Energy_Difference)

error = np.sum((img1.astype("float") - interpolated.astype("float")) ** 2)
error /= float(img1.shape[0] * img1.shape[1])
print error

energy_original = np.sum(img2_grey,dtype=np.int32)
energy_interpolated = np.sum(interpolated2,dtype=np.int32)
Energy_Difference = energy_original - energy_interpolated
print "Interpolation using nearest neighbour"
print Energy_Difference
print abs(Energy_Difference)

error = np.sum((img2_grey.astype("float") - interpolated2.astype("float")) ** 2)
error /= float(img2_grey.shape[0] * img2_grey.shape[1])
print error