import cv2 as ez
import numpy as np
def empty(a):
    pass
img1 = ez.imread("Resources/henlo.jpg")




ez.namedWindow("Trackbar")
ez.resizeWindow("Trackbar",320, 240)
ez.createTrackbar("Hue Min", "Trackbar", 9, 179, empty)
ez.createTrackbar("Hue Max", "Trackbar", 91, 179, empty)
ez.createTrackbar("Sat Min", "Trackbar", 39, 255, empty)
ez.createTrackbar("Sat Max", "Trackbar", 166, 255, empty)
ez.createTrackbar("Val Min", "Trackbar", 63, 255, empty)
ez.createTrackbar("Val Max", "Trackbar", 202, 255, empty)
while True:
    img = ez.resize(img1, (320,240))
    imgHSV = ez.cvtColor(img, ez.COLOR_BGR2HSV)
    h_min = ez.getTrackbarPos("Hue Min", "Trackbar")
    h_max = ez.getTrackbarPos("Hue Max", "Trackbar")
    s_min = ez.getTrackbarPos("Sat Min", "Trackbar")
    s_max = ez.getTrackbarPos("Sat Max", "Trackbar")
    v_min = ez.getTrackbarPos("Val Min", "Trackbar")
    v_max = ez.getTrackbarPos("Val Max", "Trackbar")
    print(h_min, h_max,s_min, s_max, v_min, v_max)
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = ez.inRange(imgHSV, lower, upper)
    imgResult = ez.bitwise_and(img, img, mask = mask)
    ez.imshow("Resulting color", imgResult)
    ez.imshow("Image", img)
    ez.imshow("ImageHSV", imgHSV)
    ez.imshow("mask", mask)
    if(ez.waitKey(1) & 0xFF == ord('q')):
        break