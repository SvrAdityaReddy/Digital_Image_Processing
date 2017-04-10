# Reference Links
# http://dsp.stackexchange.com/questions/11326/difference-between-snr-and-psnr
# http://stackoverflow.com/questions/21117415/finding-the-value-of-the-min-and-max-pixel
# http://stackoverflow.com/questions/2440504/noise-estimation-noise-measurement-in-image

import numpy as np
import cv2
import math
from scipy import signal

img = cv2.imread("/home/aditya/diptemp/tkh/imgs/cameraman.png")
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# Adding Noise of power 0.5 = n1
(row,column) = img.shape
mean = 0
variance = 0.5
standard_deviation = variance ** (0.5)

Noisy_Image1 =  np.random.normal(mean,standard_deviation,(row,column))
Noisy_Image1 = img + Noisy_Image1

# Adding Noise of power 1 = n2
(row,column) = img.shape
mean = 0
variance = 1
standard_deviation = variance ** (0.5)


Noisy_Image2 = np.random.normal(mean,standard_deviation,(row,column))

Noisy_Image2 = img + Noisy_Image2

#Distinguishing between between Noise levels using variance

Noise1 = Noisy_Image1 - img
var1 = np.var(Noise1)

Noise2 = Noisy_Image2 - img
var2 = np.var(Noise2)


Difference = var1 - var2

# print Difference

if (Difference > 0):
    print "n1 > n2"
else:
    if (Difference < 0):
        print "n1 < n2"
    else:
        print "n1 = n2"

#Distinguishing between between Noise levels using PSNR (Peak Signal to Noise Ratio)

MAX_INTENSITY = np.amax(img)

MSE1 = np.sum((img.astype("float") - Noisy_Image1.astype("float")) ** 2)
MSE1 /= float(img.shape[0] * img.shape[1])

MSE2 = np.sum((img.astype("float") - Noisy_Image2.astype("float")) ** 2)
MSE2 /= float(img.shape[0] * img.shape[1])

PSNR1 = ((MAX_INTENSITY)**2)/MSE1
PSNR2 = ((MAX_INTENSITY)**2)/MSE2

if (PSNR1 < PSNR2):
    print "n1 > n2"
else:
    if (PSNR1 > PSNR2):
        print "n1 < n2"
    else:
        print "n1 = n2"

# Distinguishing between between Noise levels with the help of Laplacian operator, Assumption is noise added is zero mean Gaussian Noise  

(H, W) = Noisy_Image1.shape
M = [[1, -2, 1],[-2, 4, -2],[1, -2, 1]]
sigma1 = np.sum(np.sum(np.absolute(signal.convolve2d(Noisy_Image1, M))))
sigma1 = sigma1 * math.sqrt(0.5 * math.pi) / (6 * (W-2) * (H-2))

sigma2 = np.sum(np.sum(np.absolute(signal.convolve2d(Noisy_Image2, M))))
sigma2 = sigma2 * math.sqrt(0.5 * math.pi) / (6 * (W-2) * (H-2))

if (sigma1 > sigma2):
    print "n1 > n2"
else:
    if (sigma1 < sigma2):
        print "n1 < n2"
    else:
        print "n1 = n2"