# Create an image of size 100 x 100, of intensity 0. Draw a square of size 40 x 40
# at the bottom of the image, of intensity 125. 
# Add a circle of radius 10 units on top of the square, of intensity 150.
# The resulting image is "I".

# http://docs.opencv.org/3.1.0/dc/da5/tutorial_py_drawing_functions.html

import numpy as np
import cv2
import math
from matplotlib import pyplot as plt

img = np.zeros((100,100,1), np.uint8)
cv2.rectangle(img,(35,55),(75,95),125,1)
cv2.circle(img,(55,44),10,150,1)
cv2.imwrite("/home/aditya/diptemp/tkh/imgs/created_image.jpeg",img)

# http://stackoverflow.com/questions/22937589/how-to-add-noise-gaussian-salt-and-pepper-etc-to-image-in-python-with-opencv

# Adding Gaussian noise of variance 0.5 to the entire image.

# Size of Image
(row,column,dim) = img.shape
mean = 0
variance = 0.5
standard_deviation = variance ** (0.5)
Noisy_Image1 = np.random.normal(mean,standard_deviation,(row,column,dim))

plt.hist(Noisy_Image1.ravel(),256,[-256,256]); plt.show()

Noisy_Image1 = img + Noisy_Image1

plt.hist(Noisy_Image1.ravel(),256,[-256,256]); plt.show()

# Extracting Circle

temp1 = np.copy(Noisy_Image1)
temp2 = np.copy(Noisy_Image1)

for h in range(row):
    for w in range(column):
        if (temp1[h,w,0] < 148 or temp1[h,w,0] > 152): # 148 to 152
            temp1[h][w][0] = 0

cv2.imwrite("/home/aditya/diptemp/tkh/imgs/created_image_circle_extract.jpeg",temp1)

# Extracting Rectangle

for h in range(row):
    for w in range(column):
        if (temp2[h,w,0] < 122 or temp2[h,w,0] > 128): # 122 to 128
            temp2[h][w][0] = 0

cv2.imwrite("/home/aditya/diptemp/tkh/imgs/created_image_rectangle_extract.jpeg",temp2)

# Adding Gaussian noise of variance 1.5 to the entire image.

# Size of Image
(row,column,dim) = img.shape
mean = 0
variance = 1.5
standard_deviation = variance ** (0.5)
Noisy_Image2 = np.random.normal(mean,standard_deviation,(row,column,dim))

plt.hist(Noisy_Image2.ravel(),256,[-256,256]); plt.show()

Noisy_Image2 = img + Noisy_Image2

plt.hist(Noisy_Image2.ravel(),256,[-256,256]); plt.show()

# Extracting Circle

temp1 = np.copy(Noisy_Image2)
temp2 = np.copy(Noisy_Image2)

for h in range(row):
    for w in range(column):
        if (temp1[h,w,0] < 144 or temp1[h,w,0] > 154): # 146 to 154, 144 to 154
            temp1[h][w][0] = 0

cv2.imwrite("/home/aditya/diptemp/tkh/imgs/created_image_circle_extract_G_Noise_1.5_var.jpeg",temp1)

# Extracting Rectangle

for h in range(row):
    for w in range(column):
        if (temp2[h,w,0] < 120 or temp2[h,w,0] > 132): # 122 to 130, 120 to 128, 120 to 130, 120 to 132
            temp2[h][w][0] = 0

cv2.imwrite("/home/aditya/diptemp/tkh/imgs/created_image_rectangle_extract_G_Noise_1.5_var.jpeg",temp2)
            