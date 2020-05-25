import cv2
import numpy as np


# cap = cv2.VideoCapture("2020-05-22-015325.webm")
cap = cv2.VideoCapture(0)

def empty(a):
    pass


cv2.namedWindow("Param")
cv2.resizeWindow("Param",640,240)
cv2.createTrackbar("thres1","Param",125,255,empty)
cv2.createTrackbar("thres2","Param",220,255,empty)

while True:
    ret,img = cap.read()


    imgBlur = cv2.GaussianBlur(img,(7,7),1)
    imgGray = cv2.cvtColor(imgBlur,cv2.COLOR_BGR2GRAY)

    thres1 = cv2.getTrackbarPos("thres1","Param")
    thres2 = cv2.getTrackbarPos("thres2","Param")

    imgCanny = cv2.Canny(imgGray,thres1,thres2)
    kernel = np.ones((5,5))
    imgDil = cv2.dilate(imgCanny,kernel,iterations=1)

    contours , hierarchy = cv2.findContours(imgDil,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

    for cnt in contours:
        peri = cv2.arcLength(cnt,True)
        approx = cv2.approxPolyDP(cnt,0.02*peri,True)
        print(len(approx))

        if len(approx) == 4:
            cv2.drawContours(img,[approx],0,(255,0,255),7)

    print(np.size(contours))

    cv2.imshow("raw",imgDil)
    cv2.imshow("blur",img)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break