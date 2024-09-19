import cv2
import numpy as np
from matplotlib import pyplot as plt

# read file
img = cv2.imread("coins.jpg") 
assert img is not None, "File could not be read"

# change from BGR to RGB
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# create a copy of original
cimg = img.copy()

# change from RGB to Gray scale
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# apply blur to smooth edges
img = cv2.medianBlur(img, 5)

# detect circles
circles = cv2.HoughCircles(image=img, method=cv2.HOUGH_GRADIENT, dp=0.9,
                            minDist=80, param1= 110, param2= 39, minRadius=50, maxRadius=90)

for co, i in enumerate(circles[0, :], start=1):
    # draw the outer circle in green
    cv2.circle(cimg,(int(i[0]),int(i[1])),int(i[2]),(0,255,0),2)
    # draw the center of the circle in red
    cv2.circle(cimg,(int(i[0]),int(i[1])),2,(0,0,255),3)
    
# print the number of circles detected
print("Number of circles detected:", co)
# show the image
plt.imshow(cimg)
plt.show()

