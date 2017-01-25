import numpy as np
import cv2
from matplotlib import pyplot as plt
import math

img = cv2.imread("/home/aditya/DIP/DIP17_1_Images/pipe.jpeg")
img_grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imwrite("/home/aditya/DIP/DIP17_1_Images/pipe_GREY.jpeg",img_grey)
blur = cv2.blur(img_grey,(5,5))
cv2.imwrite("/home/aditya/DIP/DIP17_1_Images/pipe_blur_GREY.jpeg",blur)
sobelx = cv2.Sobel(blur,cv2.CV_8U,1,0,ksize=3)
sobely = cv2.Sobel(blur,cv2.CV_8U,0,1,ksize=3)
gradient_image = sobelx + sobely
cv2.imwrite("/home/aditya/DIP/DIP17_1_Images/pipe_blur_gradient_GREY.jpeg",gradient_image)
(height,width) = gradient_image.shape
threshold = gradient_image[0][0]
for h in range(height):
    for w in range(width):
        if threshold < gradient_image[h][w]:
            threshold = gradient_image[h][w]
threshold = threshold * (33.00/100)

for h in range(height):
    for w in range(width):
        if gradient_image[h][w] < threshold:
            gradient_image[h][w] = 0

cv2.imwrite("/home/aditya/DIP/DIP17_1_Images/pipe_blur_gradient_GREY_threshold_33_percent.jpeg",gradient_image)




