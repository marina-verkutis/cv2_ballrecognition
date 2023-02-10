import numpy as np
import cv2

img = cv2.imread('img/football.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gaus = cv2.GaussianBlur(gray, (7, 7), 0)

circles = cv2.HoughCircles(gaus, cv2.HOUGH_GRADIENT, 1, 340)

if circles is not None:
    circles = np.round(circles[0,:]).astype("int")
    for(x, y, r) in circles:
        cv2.circle(img, (x, y), r, (0, 0, 255), 6)
        cv2.rectangle(img, (x-4, y-4), (x+4, y+4), (0, 0, 255), 7)

print(circles)

cv2.imshow("Picture", img)
cv2.waitKey(0)
