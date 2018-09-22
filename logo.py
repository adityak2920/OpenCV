import cv2
import numpy as np
img1 = cv2.imread('/Users/adityakumar/Downloads/wallpaper/BingWallpaper-2018-04-21.jpg')
img2 = cv2.imread('/Users/adityakumar/Downloads/logo.png')
#add = img1 + img2 ###this addition is modular operation means if pixel value is greater
###than 255 let's say 279 it will give 3 as the value of pixel
#add = cv2.add(img1/2, img2/2)###this is saturated operation means when we are adding these
###two if value exceeds greater than 255 it will convert to 255
#weighted = cv2.addWeighted(img1, 0.3, img2, 0.7, 0)
row, col, cha = img2.shape
roi = img1[0:row, 0:col]
img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 200, 255, cv2.THRESH_BINARY_INV)
mask_inv = cv2.bitwise_not(mask)
img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
img2_fg = cv2.bitwise_and(img2, img2, mask = mask)
img = cv2.add(img1_bg, img2_fg)
img1[0:row, 0:col] = img
cv2.imshow('mask_inv',mask_inv)
#cv2.imshow('gray', img1)
cv2.imshow('mask',mask)
cv2.imshow('img',img)
cv2.imshow('MSK', img1)
cv2.imshow('img1_bg',img1_bg)
cv2.imshow('img2_fg',img2_fg)
cv2.waitKey(0)
cv2.destroyAllWindows()
#(arithmetic(logo))