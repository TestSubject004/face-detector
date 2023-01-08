import cv2 as ez
import numpy as np
'''print("Package imported")

img = ez.imread("C:/Users/Saurav/Desktop/aadhar.jpg") #image read(path)

ez.imshow("Output", img) # show image("window name", image object)
#cap = ez.VideoCapture("C:/Users/Saurav/Desktop/Twitch.mp4")
t = ez.VideoCapture(1) #using the input from the camera
t.set(3,640) #setting width = 640, 3 is the id of the width parameter
t.set(4,480) #setting height = 480
t.set(10,100) #setting brightness = 100
while(True):
    success, img1 = t.read() #success returns a bool value, denotes if image read
    ez.imshow("Video", img1)
    if ez.waitKey(1) & 0xFF == ord('q'):
        break
'''
img = ez.imread("Resources/henlo.jpg")
kernel = np.ones((5,5), np.uint8) #kernel is a matrix of defined values, used to draw edges(eg. imgCanny)
imgGray = ez.cvtColor(img,ez.COLOR_BGR2GRAY) #converting to grayscale, bgr2gray = rgb to grayscale
imgBlur = ez.GaussianBlur(imgGray,(7,7), 0) #blurring image ksize = (7,7), sigmax = sigmay = 0 more the sigmax, higher the bluriness
imgCanny = ez.Canny(img, 50,50) #lower the values, more the no. of edges # canny used to detect edges
imgDilation = ez.dilate(imgCanny, kernel, iterations = 1) #the more the no. of iterations, the greater the thickness of edges
imgEroded = ez.erode(imgDilation, kernel, iterations = 1)#decreases the thickness of the edges
#ez.imshow("BlurImage", imgBlur)
ez.imshow("ErodedImage", imgEroded)
ez.waitKey(0)
