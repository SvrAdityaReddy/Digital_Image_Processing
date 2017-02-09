import cv2
import numpy as np
import math
from matplotlib import pyplot as plt



img = cv2.imread("/home/aditya/diptemp/bridge.png")
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img = cv2.GaussianBlur(img,(11,11),math.sqrt(2),math.sqrt(2))
horizon = np.array(([-1,-1,-1],[2,2,2],[-1,-1,-1]),dtype ="int")
vertic = np.array(([-1,2,-1],[-1,2,-1],[-1,2,-1]),dtype ="int")
pos = np.array(([-1,-1,2],[-1,2,-1],[2,-1,-1]),dtype ="int")
neg = np.array(([2,-1,-1],[-1,2,-1],[-1,-1,2]),dtype ="int")
img1 = cv2.filter2D(img,-1,horizon)
img2 = cv2.filter2D(img,-1,vertic)
img3 = cv2.filter2D(img,-1,pos)
img4 = cv2.filter2D(img,-1,neg)
cv2.imwrite("/home/aditya/diptemp/bridge_line_detection.png",img1+img2+img3+img4)