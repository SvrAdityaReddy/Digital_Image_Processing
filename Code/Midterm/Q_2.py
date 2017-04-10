import cv2
import numpy as np
import math
from matplotlib import pyplot as plt

image_path = "/home/aditya/diptemp/tkh/imgs/"
image_name = "index"
image_format = ".jpeg"

img = cv2.imread(image_path + image_name + image_format)
img = cv2.cvtColor(img,cv2.COLOR_BGR2Lab)
# print img.shape
Z = img.reshape((-1,3))
Z = np.float32(Z)
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
# K = 5
# For index.jpeg
K = 8
(ret,label,center) = cv2.kmeans(Z,K,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)
center = np.uint8(center)
res = center[label.flatten()]
res2 = res.reshape((img.shape))
cv2.imshow('res2',res2)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Extracting Grass

component1=np.zeros(img.shape,np.uint8)
label_image = label.reshape((img.shape[0],img.shape[1]))
component1[label_image==2]=img[label_image==2]
# component1[label_image==0]=img[label_image==0]
component1 = cv2.cvtColor(component1,cv2.COLOR_Lab2BGR)
cv2.imshow('component1',component1)
cv2.waitKey(0)
cv2.destroyAllWindows()
print component1.shape
cv2.imwrite(image_path + image_name + "_Grass" + image_format,component1 )

# Extracting Sky

component2=np.zeros(img.shape,np.uint8)
label_image = label.reshape((img.shape[0],img.shape[1]))
# component2[label_image==3]=img[label_image==3]
# Extracting Sky for index.jpeg
component2[label_image==5]=img[label_image==5]
component2[label_image==6]=img[label_image==6]
component2[label_image==7]=img[label_image==7]
component2 = cv2.cvtColor(component2,cv2.COLOR_Lab2BGR)
cv2.imshow('component2',component2)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite(image_path + image_name + "_Sky" + image_format,component2 )


# Extracting Water

component3=np.zeros(img.shape,np.uint8)
label_image = label.reshape((img.shape[0],img.shape[1]))
# component3[label_image==4]=img[label_image==4]
# Extracting Water for index.jpeg
component3[label_image==0]=img[label_image==0]
component3 = cv2.cvtColor(component3,cv2.COLOR_Lab2BGR)
cv2.imshow('component3',component3)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite(image_path + image_name + "_Water" + image_format,component3 )


# Extracting Colored Foliage

component4=np.zeros(img.shape,np.uint8)
label_image = label.reshape((img.shape[0],img.shape[1]))
component4[label_image==1]=img[label_image==1]
component4 = cv2.cvtColor(component4,cv2.COLOR_Lab2BGR)
cv2.imshow('component4',component4)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite(image_path + image_name + "_Colored_Foliage" + image_format,component4 )
