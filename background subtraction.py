import numpy as np
import cv2
###Background Subtractor
cap = cv2.VideoCapture('/Users/adityakumar/Desktop/ML/people-walking.mp4')
fgbg = cv2.createBackgroundSubtractorMOG2()

while(1):
    ret, frame = cap.read()

    fgmask = fgbg.apply(frame)

    cv2.imshow('fgmask',frame)
    cv2.imshow('frame',fgmask)


    if cv2.waitKey(10) & 0xff == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
