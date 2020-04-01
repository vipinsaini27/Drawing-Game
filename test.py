import cv2
import json
import numpy as np


img = np.full((500, 1200, 3), 255, np.uint8)
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edge = cv2.Canny(imgray, 100, 200)
cv2.imwrite('img.jpg', edge)
# print(imgray.shape)