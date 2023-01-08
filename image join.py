import cv2 as ez
import numpy as np

def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    print(rows,cols)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = ez.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = ez.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2:
                    imgArray[x][y]= ez.cvtColor( imgArray[x][y], ez.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = ez.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = ez.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2:
                imgArray[x] = ez.cvtColor(imgArray[x], ez.COLOR_GRAY2BGR)
        hor = np.hstack(imgArray)
        ver = hor
    return ver

im = ez.imread("Resources/henlo.jpg")
img = ez.resize(im, (640,480))
'''
print(img.shape)

imgResize = ez.resize(img,(320,240))

imgHor = np.hstack((imgResize, imgResize)) #stacking 2 images horizontally(side by side)

imgVert = np.vstack((imgHor,imgHor)) #stacking images on vertically
ez.imshow("Horizontal", imgHor)
ez.imshow("Vertical", imgVert)
#also there is no scaling, so the stacked images may go out of frame
#one drawback is that images with different color channels cannot be stacked using this, so a user defined function is required
'''
imgGray = ez.cvtColor(im, ez.COLOR_BGR2GRAY)
imgStack = stackImages(0.5,[[img,img, img], [imgGray, img, imgGray]])
ez.imshow("Stacked images", imgStack)
ez.waitKey(0)