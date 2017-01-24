import cv2
import numpy as np

#Steganography

bits_used = 2
img_hide = cv2.imread("/home/aditya/DIP/DIP17_1_Images/hide.jpg")
img_hider = cv2.imread("/home/aditya/DIP/DIP17_1_Images/hider.jpg")
(height,width,column) = img_hider.shape
img_hided=np.zeros((height,width,column))

#Encoding

for h in range(height):
    for w in range(width):
        img_hided[h][w][0] = img_hide[h][w][0] - (img_hide[h][w][0] % (2**bits_used)) + ((2**bits_used) * img_hider[h][w][0]/255)
        img_hided[h][w][1] = img_hide[h][w][1] - (img_hide[h][w][1] % (2**bits_used)) + ((2**bits_used) * img_hider[h][w][1]/255)
        img_hided[h][w][2] = img_hide[h][w][2] - (img_hide[h][w][2] % (2**bits_used)) + ((2**bits_used) * img_hider[h][w][2]/255)
cv2.imwrite("/home/aditya/DIP/DIP17_1_Images/hidden_new.jpg",img_hided)
# cv2.waitKey()
# print img_hided
#Decoding

img_hided_new = np.zeros((height,width,column))
img_hider_new = np.zeros((height,width,column))
for h in range(height):
    for w in range(width):
        img_hider_new[h][w][0] = ((img_hided[h][w][0] % (2**bits_used)) * (255/(2**bits_used)))
        img_hider_new[h][w][1] = ((img_hided[h][w][1] % (2**bits_used)) * (255/(2**bits_used)))
        img_hider_new[h][w][2] = ((img_hided[h][w][2] % (2**bits_used)) * (255/(2**bits_used)))
        # img_hided_new[h][w][0] = (img_hided[h][w][0] - img_hider_new[h][w][0])
        # img_hided_new[h][w][1] = (img_hided[h][w][1] - img_hider_new[h][w][1])
        # img_hided_new[h][w][2] = (img_hided[h][w][2] - img_hider_new[h][w][2])
        img_hided_new[h][w][0] = (img_hided[h][w][0] - (img_hided[h][w][0] % (2**bits_used)))
        img_hided_new[h][w][1] = (img_hided[h][w][1] - (img_hided[h][w][0] % (2**bits_used)))
        img_hided_new[h][w][2] = (img_hided[h][w][2] - (img_hided[h][w][0] % (2**bits_used)))
        # img_hided_new[h][w][0] = ((img_hided[h][w][0] % (2**(8 - bits_used))))
        # img_hided_new[h][w][1] = ((img_hided[h][w][1] % (2**(8 - bits_used))))
        # img_hided_new[h][w][2] = ((img_hided[h][w][2] % (2**(8 - bits_used))))
cv2.imwrite("/home/aditya/DIP/DIP17_1_Images/extracted_hider.jpg",img_hider_new)        
cv2.imwrite("/home/aditya/DIP/DIP17_1_Images/extracted_hide.jpg",img_hided_new)        
# cv2.imshow("Image",img_hided_new)
# cv2.waitKey()



