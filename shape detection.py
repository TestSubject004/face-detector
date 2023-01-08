import cv2 as ez
import numpy as np

def getContours(img):
    contours, hierarchy = ez.findContours(img, ez.RETR_EXTERNAL,ez.CHAIN_APPROX_NONE) #fetches outer contours/boundaries and does not approximate i.e, gets all contours
    for cnt in contours:
        area = ez.contourArea(cnt) #finds the area of the contour/shape
        print(area)
        if(area > 3000):
            ez.drawContours(imgContour, cnt, -1, (255, 0, 0), 3) #outlining the contours on hte image
            peri = ez.arcLength(cnt, True)# true means boundary is closed
            print(peri)
            approx = ez.approxPolyDP(cnt, 0.012*peri, True) #approximating no. of corner points, true means shape is closec
            print(len(approx))
            objCor = len(approx) #gets no. of corners in object
            x, y, w, h = ez.boundingRect(approx) #gets origin and width, height of the bounding rectangle
            if objCor == 3: objectType = "Tri"
            elif objCor == 4:
                    aspRatio = w/float(h)
                    if aspRatio > 0.95 and aspRatio < 1.05:
                        objectType = "Square"
                    else:
                        objectType = "Rectangle"
            elif objCor == 5: objectType = "Pentagon"
            elif objCor == 6: objectType = "Hexagon"
            elif objCor == 7: objectType = "Heptagon"
            elif objCor == 8: objectType = "Octagon"
            elif objCor == 9: objectType = "Nonagon"
            elif objCor == 10: objectType = "Decagon"
            else: objectType = "Circle"
            ez.rectangle(imgContour, (x,y), (x + w, y + h), (0, 255, 0), 2)
            ez.putText(imgContour,objectType,
                       (x + (w//2) - 10, y + (h//2) - 10), ez.FONT_HERSHEY_COMPLEX,
                       0.5, (0,0, 0), 2)
path = "Resources/shapes.png"
im = ez.imread(path)

img = ez.resize(im, (640,640))
imgContour = img.copy()
imgGray = ez.cvtColor(img, ez.COLOR_BGR2GRAY)
imgBlur = ez.GaussianBlur(imgGray, (7,7),1)
imgCanny = ez.Canny(imgBlur, 50, 50)
getContours(imgCanny)
ez.imshow("imgContour", imgContour)
ez.imshow("Output", img)
ez.waitKey(0)


imgBlank = np.zeros_like(img) # creates a blank image(all black) with the resolution of img
