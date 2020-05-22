# Import the required packages
import argparse
import cv2

parser = argparse.ArgumentParser()

parser.add_argument("path_image_input", help="path to input image to be displayed")
parser.add_argument("path_image_output", help="path of the processed image to be saved")

args = vars(parser.parse_args())

image_input = cv2.imread(args["path_image_input"])
cv2.imshow("loaded image", image_input)
gray_image = cv2.cvtColor(image_input, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray image", gray_image)
cv2.imwrite(args["path_image_output"], gray_image)



cv2.waitKey(0)

cv2.destroyAllWindows()