import numpy as np
import cv2
import math

# img = cv2.imread("/home/aditya/DIP/DIP17_1_Images/noise.jpeg")
img = cv2.imread("/home/aditya/DIP/DIP17_1_Images/cameraman.png")
blur = cv2.blur(img,(11,11))
# cv2.imwrite("/home/aditya/DIP/DIP17_1_Images/removed_noise_blur.jpeg",blur)
cv2.imwrite("/home/aditya/DIP/DIP17_1_Images/cameraman_mean_blur.png",blur)
g_blur = cv2.GaussianBlur(img,(7,7),math.sqrt(3))
# cv2.imwrite("/home/aditya/DIP/DIP17_1_Images/removed_noise_g_blur.jpeg",g_blur)
cv2.imwrite("/home/aditya/DIP/DIP17_1_Images/cameraman_g_blur.png",g_blur)