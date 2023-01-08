import cv2 as ez
import numpy as np

'''im = np.zeros((512,512))

#ez.imshow("matrix", im)
print(im.shape)# checking dimensionality of an image or matrix
# #this image has only 1 channel, so it's a grayscale image
img = np.zeros((512,512, 3), np.uint8)
print(img.shape)
#img[:] = 255, 0, 0 #blue [:] means whole image
img[200:300,100:300] = 255, 0, 0#height from 200 to 300, width from 100 to 300
ez.imshow("3 channel image", img)
t = ez.imread("C:/Users/Saurav/Desktop/henlo.jpg")
imgResize = ez.resize(t,(480,640))
ez.line(imgResize,(0,0), (t.shape[1], t.shape[0]),(0,255,0),2)'''

img = np.zeros((512,512, 3), np.uint8)


ez.line(img,(0,0), (img.shape[1], img.shape[0]),(0,255,0),2) #draw line(img, starting point, ending point, color, thickness)

ez.rectangle(img,(0, 0),(250, 350),(0,255,255),2) #use cv2.FILLED for filling the rectangle with border color

ez.circle(img,(400,50),30,(255,2550,0),ez.FILLED)

ez.putText(img,"My name is anythony", (50,100),ez.FONT_ITALIC,1,(255,255,255),1) #org is the origin point of the text

ez.imshow("Image", img)

ez.waitKey(0)