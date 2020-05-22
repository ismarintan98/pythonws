import cv2
import numpy as np
from matplotlib import pyplot as plt

def show_wMatplotlib(color_img,tittle,pos):

    img_RGB  = color_img[:,:,::-1]

    ax = plt.subplot(2,3,pos)
    plt.imshow(img_RGB)
    plt.title(tittle)
    plt.axis('off')

def show_wMatplotlib_grey(hist,title,pos,color):
    
    ax = plt.subplot(2,3,pos)

    plt.xlabel("bins")
    plt.ylabel("number of pixel")
    plt.xlim([0,256])
    plt.plot(hist,color = color)

plt.figure(figsize=(15,6))
plt.suptitle("Grayscale histogram",fontsize=14,fontweight='bold')

image = cv2.imread('lenna.png')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
hist = cv2.calcHist([gray_image], [0], None, [256], [0, 256])

show_wMatplotlib(cv2.cvtColor(gray_image,cv2.COLOR_GRAY2BGR),"gray",1)
show_wMatplotlib_grey(hist,"gray histo",4,'m')


M = np.ones(gray_image.shape,dtype="uint8") * 35

added_image = cv2.add(gray_image,M)
hist_added_image = cv2.calcHist([added_image],[0],None,[256],[0,256])

substracted_image = cv2.subtract(gray_image,M)
hist_subtracted_image = cv2.calcHist([substracted_image],[0],None,[256],[0,256])

show_wMatplotlib(cv2.cvtColor(added_image,cv2.COLOR_GRAY2BGR),"gray light",2)
show_wMatplotlib_grey(hist_added_image,"grayscale histo",5,'m')
show_wMatplotlib(cv2.cvtColor(substracted_image,cv2.COLOR_GRAY2BGR),"gray darker",3)
show_wMatplotlib_grey(hist_subtracted_image,"grayscale histo",6,'m')

plt.show()