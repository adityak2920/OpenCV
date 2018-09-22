import cv2
import numpy as np
import matplotlib.pyplot as plt
####ImageCapture#####
#img = cv2.imread('/Users/adityakumar/Downloads/Aditya.jpeg', cv2.IMREAD_GRAYSCALE)
#cv2.imshow('aditya', img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
#plt.imshow(img, cmap='gray', interpolation='bicubic')
#plt.show()
####VideoCapture####
#cap = cv2.VideoCapture(0)
#fourcc = cv2.VideoWriter_fourcc(*'XVID')
#out = cv2.VideoWriter('output.avi', fourcc, 12.0, (640, 480), True)
#while(cap.isOpened()):
#    ret, frame = cap.read()
#    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#    #hls = cv2.cvtColor(frame, cv2.COLOR_BGR2HLS)
#    #lab = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)
#    #adi=cv2.imread(frame)
#    out.write(frame)
#    cv2.imshow('frame', frame)
#    cv2.imshow('gray', gray)
#
#    #cv2.imshow('HLS', hls)
#    #cv2.imshow('LAB', lab)
#    if cv2.waitKey(40) & 0xFF == ord('q'):
#        break
#cap.release()
#out.release()
img = cv2.imread('/Users/adityakumar/Downloads/Aditya.jpeg', cv2.IMREAD_COLOR)
#cv2.line(img, (2, 3), (250, 590), (255, 100, 100), 10)
#cv2.rectangle(img, (2, 3), (250, 590), (255, 100, 100), -1)
#cv2.circle(img, (500, 700),65, (255, 150, 150), 15)
face = img[100:500, 200:800]
img[0:400, 0:600] = face
cv2.imshow('image', img)
cv2.waitKey(0)

cv2.destroyAllWindows()



