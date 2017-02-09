import numpy as np
import cv2
from matplotlib import pyplot as plt



img = cv2.imread("/home/aditya/diptemp/cameraman_grey.png")
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img2 = cv2.imread("/home/aditya/diptemp/lena.jpg")
img2_grey=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
# print img_grey.shape
# cv2.imwrite("/home/aditya/diptemp/cameraman_grey.png",img_grey)
small = cv2.resize(img, (0,0), fx=0.5, fy=0.5)
interpolated = cv2.resize(small,(0,0) ,fx=2,fy=2,interpolation=cv2.INTER_CUBIC)
small2 = cv2.resize(img2_grey, (0,0), fx=0.5, fy=0.5)
interpolated2 = cv2.resize(small2,(0,0) ,fx=2,fy=2,interpolation=cv2.INTER_CUBIC)  
# print small.shape

cv2.imwrite("/home/aditya/diptemp/cameraman_bicubic.png",interpolated)
cv2.imwrite("/home/aditya/diptemp/lena_bicubic.jpg",interpolated2)
# print img.shape
# print interpolated.shape

energy_original = np.sum(img,dtype=np.float)
energy_interpolated = np.sum(interpolated,dtype=np.float)
print energy_original
print energy_interpolated
Energy_Difference = energy_original - energy_interpolated
print "Interpolation using bicubic"
print Energy_Difference
print abs(Energy_Difference)

print img.shape
print interpolated.shape

# diff_ene = np.sum(img.astype("int32") - interpolated.astype("int32") )
# print diff_ene
error = np.sum((img.astype("float") - interpolated.astype("float")) ** 2)
error /= float(img.shape[0] * img.shape[1])
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