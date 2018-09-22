import cv2
import numpy as np
import matplotlib.pyplot as plt

img1 = cv2.imread('/Users/adityakumar/Downloads/a.jpeg', 0)
img2 = cv2.imread('/Users/adityakumar/Downloads/ab.jpeg', 0)

#orb = cv2.ORB_create()#ORB is just feature descriptor(Oriented Fast and Rotated Brief)
sift = cv2.SIFT()#Scale Invariant Feature Transform
kp1, des1 = sift.detectAndCompute(img1, None)
kp2, des2 = sift.detectAndCompute(img2, None)
# create BFMatcher object
#bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
bf = cv2.BFMatcher()
# Match descriptors.
#matches = bf.match(des1, des2)
matches = bf.knnMatch(des1,des2, k=2)
# Sort them in the order of their distance.
#matches = sorted(matches, key = lambda x:x.distance)
print matches
good=[]
for m,n in matches:
    if m.distance < 0.75*n.distance:
        good.append([m])

#img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], flags=2, outImg=None)
img3 = cv2.drawMatchesKnn(img1,kp1,img2,kp2,good,flags=2)
plt.imshow(img3), plt.show()
