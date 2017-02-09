import cv2
import numpy as np
# from numpy import array
import math
import scipy.signal
from matplotlib import pyplot as plt

img = cv2.imread("/home/aditya/diptemp/cameraman.png")
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imwrite("/home/aditya/diptemp/cameraman_grey.png",img)
# print img.shape
blur = cv2.blur(img,(7,7))
cv2.imwrite("/home/aditya/diptemp/cameraman_average.png",blur)
gaussian = cv2.GaussianBlur(img,(7,7),math.sqrt(2),math.sqrt(2))
cv2.imwrite("/home/aditya/diptemp/cameraman_gaussian.png",gaussian)

img2 = cv2.imread("/home/aditya/diptemp/impulse_noise.png")
median = cv2.medianBlur(img2,5)
cv2.imwrite("/home/aditya/diptemp/impulse_noise_median.png",median)

img3 = cv2.imread("/home/aditya/diptemp/bilateral.png")
img_grey=cv2.cvtColor(img3,cv2.COLOR_BGR2GRAY)
cv2.imwrite("/home/aditya/diptemp/bilateral_grey.png",img_grey)
bil = cv2.bilateralFilter(img_grey,9,75,75)
cv2.imwrite("/home/aditya/diptemp/bilateral_filter.png",bil)

img4 = cv2.imread("/home/aditya/diptemp/cameraman_average.png")
img4 = cv2.cvtColor(img4,cv2.COLOR_BGR2GRAY)
cv2.imwrite("/home/aditya/diptemp/motion_grey.png",img4)
# print img4.shape
wiefil = scipy.signal.wiener(img4,mysize=3,noise=3)
cv2.imwrite("/home/aditya/diptemp/motion_wiener.png",wiefil)


kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))
# array([[1, 1, 1, 1, 1],
#        [1, 1, 1, 1, 1],
#        [1, 1, 1, 1, 1],
#        [1, 1, 1, 1, 1],
#        [1, 1, 1, 1, 1]], dtype=uint8)
img5 = cv2.imread("/home/aditya/diptemp/pepper.jpg")
img5 = cv2.cvtColor(img5,cv2.COLOR_BGR2GRAY)
closing = cv2.morphologyEx(img5, cv2.MORPH_CLOSE, kernel)
cv2.imwrite("/home/aditya/diptemp/pepper_closing.jpg",closing)