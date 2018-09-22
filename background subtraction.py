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
#cap = cv2.VideoCapture(0)
##cascade_fn = args.get('--cascade', "../../data/haarcascades/haarcascade_frontalface_alt.xml")
##nested_fn  = args.get('--nested-cascade', "../../data/haarcascades/haarcascade_eye.xml")
#face_cascade = cv2.CascadeClassifier('/Users/adityakumar/Desktop/haarcascade/haarcascade_frontalface_default.xml')
#eye_cascade = cv2.CascadeClassifier('/Users/adityakumar/Desktop/haarcascade/haarcascade_eye.xml')
#while True:
#    ret, frame = cap.read()
#    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
#    for (x, y, w, h) in faces:
#        cv2.rectangle(frame, (x, y), (x+w, y+h),(255, 0, 0), 2)
#        roi_gray = gray[y:y+h, x:x+w]
#        roi_color = frame[y:y+h, x:x+w]
#        eyes = eye_cascade.detectMultiScale(roi_gray)
#        for (ex, ey, ew, eh) in eyes:
#            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (255, 0, 0), 2)
#    cv2.imshow('frame', frame)
#    if cv2.waitKey(10) & 0xff == ord('q'):
#        break
#
#cap.release()
#cv2.destroyAllWindows()
