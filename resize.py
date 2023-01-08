import cv2 as ez
import numpy as np

img = ez.imread("Resources/henlo.jpg")
print(img.shape) # (1280, 960, 3) height, width, code for channel(rbg or bgr)

imgResize = ez.resize(img,(320, 240)) #parameter should be (width, height)
print(imgResize.shape)
ez.imshow("ImageResized", imgResize)

ez.waitKey(0)
