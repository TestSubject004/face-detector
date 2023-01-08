import cv2 as ez
import numpy as np

img = ez.imread("Resources/henlo.jpg")

imgCropped = img[80:800][100:700] #no function required to crop, just treat the image as a matrix and use matrix[height][width] to crop
ez.imshow("CroppedImage", imgCropped)
ez.waitKey(0)

