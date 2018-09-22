import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_red = np.array([110, 100, 110])
    upper_red = np.array([180, 180,180])

    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame, frame, mask=mask)
    
#    kernel = np.ones((15, 15), np.float32)/255
#    filter = cv2.filter2D(res, -1, kernel)
#
#    blur = cv2.GaussianBlur(res, (15, 15), 0)
#
#    mblur = cv2.medianBlur(res, 15)
    kernel = np.ones((5, 5), np.uint8)
    erosion = cv2.erode(mask, kernel, iterations=1)
    dilation = cv2.dilate(mask, kernel, iterations=1)
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    gradient = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernel)

    cv2.imshow('frame', frame)
#    cv2.imshow('mask', mask)
    cv2.imshow('res', res)
    cv2.imshow('erosion', erosion)
    cv2.imshow('dilation', dilation)
    cv2.imshow('opening', opening)
    cv2.imshow('closing', closing)
    cv2.imshow('gradien', gradient)
    #cv2.imshow('filter', filter)
    #cv2.imshow('blur', blur)
#    cv2.imshow('mblur', mblur)
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break


cv2.destroyAllWindows()
cap.release()
