import cv2
import numpy as np
# from numpy import array
import math
from scipy import interpolate
from matplotlib import pyplot as plt


img = cv2.imread("/home/aditya/diptemp/cameraman_grey.png")
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
small = cv2.resize(img, (0,0), fx=0.5, fy=0.5)
img2 = cv2.imread("/home/aditya/diptemp/lena.jpg")
img2_grey=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
small2 = cv2.resize(img2_grey, (0,0), fx=0.5, fy=0.5)
# large = cv2.resize(small, (0,0), fx=2, fy=2)
(height,width) = img.shape
large = np.zeros((height,width))
for h in range(height):
    for w in range(width):
        large[h][w] = 0

# print img.shape
# print small.shape
print large.shape
x = range(0,256,2)
y = range(0,256,2)
# print x
# print y
# xx, yy = np.meshgrid(x, y)
# z = small[xx][yy]
for h in range(height/2):
    for w in range(width/2):
        large[h*2][w*2] = small[h][w]
f = interpolate.interp2d(x,y,small,kind='linear')
xnew = range(0,256,1)
ynew = range(0,256,1)
interpolated = f(xnew,ynew)
print interpolated.shape
cv2.imwrite("/home/aditya/diptemp/cameraman_grey_linear_spline.png",interpolated)

energy_original = np.sum(img,dtype=np.float)
energy_interpolated = np.sum(interpolated,dtype=np.float)
# print energy_original
# print energy_interpolated
Energy_Difference = energy_original - energy_interpolated
print "Interpolation using linear spline"
print Energy_Difference
print abs(Energy_Difference)

error = np.sum((img.astype("float") - interpolated.astype("float")) ** 2)
error /= float(img.shape[0] * img.shape[1])
print error

(height,width) = img2_grey.shape
large = np.zeros((height,width))
for h in range(height):
    for w in range(width):
        large[h][w] = 0

print large.shape
x = range(0,256,2)
y = range(0,256,2)

for h in range(height/2):
    for w in range(width/2):
        large[h*2][w*2] = small2[h][w]
f = interpolate.interp2d(x,y,small2,kind='linear')
xnew = range(0,256,1)
ynew = range(0,256,1)
interpolated = f(xnew,ynew)
print interpolated.shape
cv2.imwrite("/home/aditya/diptemp/lena_linear_spline.png",interpolated)

energy_original = np.sum(img2_grey,dtype=np.float)
energy_interpolated = np.sum(interpolated,dtype=np.float)
# print energy_original
# print energy_interpolated
Energy_Difference = energy_original - energy_interpolated
print "Interpolation using linear spline"
print Energy_Difference
print abs(Energy_Difference)

error = np.sum((img2_grey.astype("float") - interpolated.astype("float")) ** 2)
error /= float(img2_grey.shape[0] * img2_grey.shape[1])
print error