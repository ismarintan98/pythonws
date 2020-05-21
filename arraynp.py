import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np


img_raw = mpimg.imread('images/img1.jpg')


plt.imshow(img_raw)
# plt.show()
# print(img_raw)

pj = len(img_raw)
# print(img_raw[0][1][0])

m = [[[1, 12, 13], [14, 15, 16], [270, 280, 290], [270, 280, 290]],
     [[21, 22, 23], [24, 25, 26], [272, 282, 292], [270, 280, 290]]]
# print(m[1][1][2])

a = np.array(m)
b = np.size(m, 0)
# print(a.shape)
# print(b)

ma = [1, 2, 3]

for z in range(0, np.size(m, 0)):

    for y in range(0, np.size(m, 1)):

            for x in range(0, np.size(m, 2)):
                if x != np.size(m, 2)-1:
                    print(m[z][y][x], end=',')
                else:
                    print(m[z][y][x], end='     ')

    if y == np.size(m,1)-1:
        print()   





