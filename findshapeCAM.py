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
        img_blur = cv2.GaussianBlur(img,(71,71),1)
        img_grey = cv2.cvtColor(img_blur, cv2.COLOR_BGR2GRAY)
        _, threshold = cv2.threshold(img_grey, 90, 255, cv2.THRESH_BINARY)
        contours, _ = cv2.findContours(threshold, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)


        for cnt in contours:
            approx = cv2.approxPolyDP(cnt, 0.02*cv2.arcLength(cnt, True), True)
            x = approx.ravel()[0]
            y = approx.ravel()[1]

            if len(approx) == 4:
                if y > 5:
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


        for cnt in contours:
            approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
            x = approx.ravel()[0]
            y = approx.ravel()[1]

            if len(approx) == 3:
                for cnt_trig in range(0, number_of_rect):
                    if x > rect_x_min[cnt_trig] and x < rect_x_max[cnt_trig] and y > rect_y_min[cnt_trig] and y < rect_y_max[cnt_trig]:
                        cv2.putText(img, "Triangle", (x, y), font, 1, (21,21,255))
                        cv2.drawContours(img, [approx], 0, (21,21,255), 3)


        cv2.imshow("shapes", img)
        cv2.imshow("Threshold", threshold)

        if cv2.waitKey(20) & 0xFF == ord('q'):
            break

    else:
        break
    

capture.release()
cv2.destroyAllWindows()
