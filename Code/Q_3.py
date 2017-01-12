import numpy as np
import cv2

img = cv2.imread("/home/aditya/DIP/PRACTICE/DIP17_1_Images/1944.jpg")
#cv2.imshow("Image",img)
img_grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#cv2.imshow("Image",img_grey)
print img_grey.shape
#cv2.waitKey()
#print img[:,:,0]
(height,width) = img_grey.shape
img_grey_bit=np.zeros((height,width,8))
for h in range(height):
    for w in range(width):
        temp="{0:08b}".format(img_grey[h][w])
        for v in range(8):
            img_grey_bit[h][w][v] = temp[v]
        #img_grey_bit.append(temp)
#print img_grey_bit
cv2.imwrite("/home/aditya/DIP/PRACTICE/DIP17_1_Images/B_8.jpg",img_grey_bit[:,:,0])
# print img_grey_bit[:,:,0]
# print "dfgh"
# print img_grey_bit[:,:,1]
cv2.imwrite("/home/aditya/DIP/PRACTICE/DIP17_1_Images/B_7.jpg",img_grey_bit[:,:,1])
cv2.imwrite("/home/aditya/DIP/PRACTICE/DIP17_1_Images/B_6.jpg",img_grey_bit[:,:,2])
cv2.imwrite("/home/aditya/DIP/PRACTICE/DIP17_1_Images/B_5.jpg",img_grey_bit[:,:,3])
cv2.imwrite("/home/aditya/DIP/PRACTICE/DIP17_1_Images/B_4.jpg",img_grey_bit[:,:,4])
cv2.imwrite("/home/aditya/DIP/PRACTICE/DIP17_1_Images/B_3.jpg",img_grey_bit[:,:,5])
cv2.imwrite("/home/aditya/DIP/PRACTICE/DIP17_1_Images/B_2.jpg",img_grey_bit[:,:,6])
cv2.imwrite("/home/aditya/DIP/PRACTICE/DIP17_1_Images/B_1.jpg",img_grey_bit[:,:,7])
#print img_grey_bit
#print img_grey