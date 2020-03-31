import numpy as np
import cv2
print("extract_image")
def get_crop(img):
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edge = cv2.Canny(imgray, 100, 200)

    contours, hierarchy = cv2.findContours(edge, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    box = []

    for c in contours:
        (x, y, w, h) = cv2.boundingRect(c)
        box.append([x, y, x+w, y+h])

    box = np.asarray(box)

    left = np.min(box[:,0])
    top = np.min(box[:,1])
    right = np.max(box[:,2])
    bottom = np.max(box[:,3])

    image = img[top:bottom, left:right]

    return image

def resize_image(img):
    img = cv2.resize(img, (32, 32), interpolation=cv2.INTER_AREA)
    img = img.reshape((1, 32, 32, 3))
    return img