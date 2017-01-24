import numpy as np
import cv2

img = cv2.imread("/home/aditya/DIP/DIP17_1_Images/impulse_noise.png")
img = cv2.medianBlur(img,7)
cv2.imwrite("/home/aditya/DIP/DIP17_1_Images/removed_impulse_noise.png",img)