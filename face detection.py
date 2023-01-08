import cv2 as ez

faceCascade = ez.CascadeClassifier(ez.data.haarcascades + "haarcascade_frontalface_default.xml")
im = ez.imread("Resources/ez.jpg")
img = ez.resize(im, (640,480))
imgGray = ez.cvtColor(img,ez.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imgGray, 1.1, 10) #stores the parameters of the faces

for (x,y,w,h) in faces:
     ez.rectangle(img,(x,y),(x+w, y+h), (255, 0, 0), 2)

ez.imshow("Result", img)
ez.waitKey(0)