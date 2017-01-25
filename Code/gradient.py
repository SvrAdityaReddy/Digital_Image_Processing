import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread("/home/aditya/DIP/DIP17_1_Images/pipe.jpeg")
img_grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imwrite("/home/aditya/DIP/DIP17_1_Images/pipe_GREY.jpeg",img_grey)
sobelx = cv2.Sobel(img,cv2.CV_8U,1,0,ksize=3)
sobely = cv2.Sobel(img,cv2.CV_8U,0,1,ksize=3)
# s_sobel64f = np.absolute(sobelx64f)
# sobel_8u = np.uint8(abs_sobel64f)
cv2.imwrite("/home/aditya/DIP/DIP17_1_Images/pipe_y_edge_GREY.jpeg",sobelx)
cv2.imwrite("/home/aditya/DIP/DIP17_1_Images/pipe_x_edge_GREY.jpeg",sobely)