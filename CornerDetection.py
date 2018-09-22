import numpy as np
import cv2 as cv
filename = '/Users/adityakumar/Downloads/logo.png'
img = cv.imread(filename)
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#print gray
#gray = np.float32(gray)
#print gray
#dst = cv.cornerHarris(gray,2,3,0.04)
##result is dilated for marking the corners, not important
#dst = cv.dilate(dst,None)
## Threshold for an optimal value, it may vary depending on the image.
#img[dst>0.05*dst.max()]=[0,0,255]
#cv.imshow('dst',img)
corners = cv.goodFeaturesToTrack(gray, 45, 0.01, 10)
#corners = np.int0(corners)
#print corners

for corner in corners:
    x, y = corner.ravel()
    cv.circle(img, (x, y), 1, (255, 255, 0), 2)

cv.imshow('corners', img)
cv.waitKey(0)
cv.destroyAllWindows()
