# Import the required packages
import cv2
import argparse



parser = argparse.ArgumentParser()

parser.add_argument("index_camera", help="index of the camera to read from", type=int)
args = parser.parse_args()

capture = cv2.VideoCapture(args.index_camera)

frame_width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
frame_height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps = capture.get(cv2.CAP_PROP_FPS)

print("CV_CAP_PROP_FRAME_WIDTH: '{}'".format(frame_width))
print("CV_CAP_PROP_FRAME_HEIGHT : '{}'".format(frame_height))
print("CAP_PROP_FPS : '{}'".format(fps))

if capture.isOpened()is False:
    print("Error opening the camera")

while capture.isOpened():

    ret, frame = capture.read()

    if ret is True:

        cv2.imshow('Input Frame',frame)
        gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('Gray Cam ',gray_frame)

        if cv2.waitKey(20) & 0xFF == ord('q'):
            break

    else :

        break

capture.release()
cv2.destroyAllWindows()

