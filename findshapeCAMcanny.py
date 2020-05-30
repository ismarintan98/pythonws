import cv2
import numpy as np

font = cv2.FONT_HERSHEY_COMPLEX

cap = cv2.VideoCapture()

rect_x_max = np.full(100000, 0)
rect_y_max = np.full(100000, 0)

rect_x_min = np.full(100000, 0)
rect_y_min = np.full(100000, 0)

number_of_rect = 0
detetected = 0

capture = cv2.VideoCapture(0)

if capture.isOpened()is False:
    print("Error opening the camera")

while capture.isOpened():
    ret,frame = capture.read()
    if ret is True :
        img = frame

        lbr = int(np.size(img,1) * 40/100)
        tgi = int(np.size(img,0) * 40/100)
        dim = (lbr,tgi)

        # img_rsz = cv2.resize(img,dim,interpolation=cv2.INTER_AREA)
        img_rsz = img

        img_crop = img_rsz[10:(np.size(img_rsz,0)-10),10:(np.size(img_rsz,1)-10)]
        img_blur = cv2.GaussianBlur(img_crop,(7,7),1)
        img_grey = cv2.cvtColor(img_blur,cv2.COLOR_BGR2GRAY)
        img_canny = cv2.Canny(img_grey,40,70)
        kernel_dil = np.ones((5,5))
        img_dil = cv2.dilate(img_canny,kernel_dil,iterations=1)
        _, threshold = cv2.threshold(img_grey, 90, 255, cv2.THRESH_BINARY)
        contours, _ = cv2.findContours(img_dil, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)


        for cnt in contours:
            area = cv2.contourArea(cnt)
            if(area>100):            
                approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
                x = approx.ravel()[0]
                y = approx.ravel()[1]

                if len(approx) == 4:
                    # cv2.drawContours(img_crop, [approx], 0, (255,0,255), 3)
                    if y > 2:
                        # find x_max
                        rect_x_max[number_of_rect] = approx[0][0][0]
                        if approx[1][0][0] > rect_x_max[number_of_rect]:
                            rect_x_max[number_of_rect] = approx[1][0][0]
                        if approx[2][0][0] > rect_x_max[number_of_rect]:
                            rect_x_max[number_of_rect] = approx[2][0][0]
                        if approx[3][0][0] > rect_x_max[number_of_rect]:
                            rect_x_max[number_of_rect] = approx[3][0][0]

                        # find y_max
                        rect_y_max[number_of_rect] = approx[0][0][1]
                        if approx[1][0][1] > rect_y_max[number_of_rect]:
                            rect_y_max[number_of_rect] = approx[1][0][1]
                        if approx[2][0][1] > rect_y_max[number_of_rect]:
                            rect_y_max[number_of_rect] = approx[2][0][1]
                        if approx[3][0][0] > rect_x_max[number_of_rect]:
                            rect_y_max[number_of_rect] = approx[3][0][y]

                        # find x_min
                        rect_x_min[number_of_rect] = approx[0][0][0]
                        if approx[1][0][0] < rect_x_min[number_of_rect]:
                            rect_x_min[number_of_rect] = approx[1][0][0]
                        if approx[2][0][0] < rect_x_min[number_of_rect]:
                            rect_x_min[number_of_rect] = approx[2][0][0]
                        if approx[3][0][0] < rect_x_min[number_of_rect]:
                            rect_x_min[number_of_rect] = approx[3][0][0]

                        # find y_min
                        rect_y_min[number_of_rect] = approx[0][0][1]
                        if approx[1][0][1] < rect_y_min[number_of_rect]:
                            rect_y_min[number_of_rect] = approx[1][0][1]
                        if approx[2][0][1] < rect_y_min[number_of_rect]:
                            rect_y_min[number_of_rect] = approx[2][0][1]
                        if approx[3][0][1] < rect_y_min[number_of_rect]:
                            rect_y_min[number_of_rect] = approx[3][0][1]

                        number_of_rect += 1

                        # cv2.drawContours(img_crop, [approx], 0, (255,0,255), 3)

        # number_of_rect -=1
        contours2, _2 = cv2.findContours(img_dil, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        
        for cnt in contours2:
            area = cv2.contourArea(cnt)
            if(area>100):            
                approx = cv2.approxPolyDP(cnt, 0.08*cv2.arcLength(cnt, True), True)
                x = approx.ravel()[0]
                y = approx.ravel()[1]

                if len(approx) == 3:
                    # cv2.drawContours(img_crop, [approx], 0, (255,0,255), 3)
                    for cnt_trig in range(0, number_of_rect):
                        if x > rect_x_min[cnt_trig] and x < rect_x_max[cnt_trig] and y > rect_y_min[cnt_trig] and y < rect_y_max[cnt_trig]:
                            cv2.putText(img_crop, "Target", (x, y), font, 1, (255,0,255))
                            # cv2.drawContours(img_crop, [approx], 0, (255,0,255), 3)
                            cv2.rectangle(img_crop,(rect_x_min[cnt_trig],rect_y_min[cnt_trig]),(rect_x_max[cnt_trig],rect_y_max[cnt_trig]),(255,0,255),3)


        rect_x_max = np.full(100000, 0)
        rect_y_max = np.full(100000, 0)

        rect_x_min = np.full(100000, 0)
        rect_y_min = np.full(100000, 0)

        number_of_rect = 0

        cv2.imshow("shapes", img_crop)
        cv2.imshow("Threshold", img_canny)

        if cv2.waitKey(20) & 0xFF == ord('q'):
            break

    else:
        break
    

capture.release()
cv2.destroyAllWindows()
