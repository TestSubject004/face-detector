import cv2 as ez
import numpy as np

#program to cut out a portion of an image, no matter the orientation

img = ez.imread("Resources/cards.jpg")


print(img.shape) #checking the width and height of the image

width, height = 250, 350 #helps set the size of the image, (cards are generally 2.5 x 3.5 inches, so aspect ratio maintained in this case)

pts1 = np.float32([[222,92],[430,135],[162,381],[369,426]]) # points of the card we want to get, obtained by
#moving the image to paint and hovering cursor over the points needed

pts2 = np.float32([[0,0],[width, 0],[0,height],[width,height]])

matrix = ez.getPerspectiveTransform(pts1, pts2) #img matrix creation

imgOutput = ez.warpPerspective(img, matrix, (width, height)) #card obtained

ez.imshow("Output", imgOutput)
ez.waitKey(0)