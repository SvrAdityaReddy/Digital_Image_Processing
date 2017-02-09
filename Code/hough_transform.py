# import cv2
# import numpy as np
# import math

# img = cv2.imread("/home/aditya/diptemp/sudoku.png")
# grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# gau = cv2.GaussianBlur(grey,(11,11),math.sqrt(2),math.sqrt(2))
# edges = cv2.Canny(gau,50,150,apertureSize = 3)
# cv2.imwrite("/home/aditya/diptemp/sudoku_edges.png",edges)
# lines = cv2.HoughLines(edges,1,np.pi/180,50)
# # print lines
# print lines.shape
# for rho,theta in lines[0]:
#     a = np.cos(theta)
#     b = np.sin(theta)
#     x0 = a*rho
#     y0 = b*rho
#     x1 = int(x0 + 1000*(-b))
#     y1 = int(y0 + 1000*(a))
#     x2 = int(x0 - 1000*(-b))
#     y2 = int(y0 - 1000*(a))

#     cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)

# cv2.imwrite("/home/aditya/diptemp/sudoku_hough_transform.png",img)

import cv2
import numpy as np

img = cv2.imread("/home/aditya/diptemp/sudoku.png")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


edges = cv2.Canny(gray,100,200,apertureSize = 3)
cv2.imwrite("/home/aditya/diptemp/sudoku_edges.png",edges)
# cv2.waitKey(0)

minLineLength = 30
maxLineGap = 10
lines = cv2.HoughLinesP(edges,1,np.pi/180,15,minLineLength,maxLineGap)
for x in range(0, len(lines)):
    for x1,y1,x2,y2 in lines[x]:
        cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)

cv2.imwrite("/home/aditya/diptemp/sudoku_hough_transform.png",img)
# cv2.waitKey(0)