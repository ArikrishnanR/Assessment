import cv2
trainedfacemodel=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
webcam=cv2.VideoCapture(0)
while True:
    working,video=webcam.read()
    color=cv2.cvtColor(video,cv2.COLOR_BGR2GRAY)
    face=trainedfacemodel.detectMultiScale(color)
    for (x,y,w,h) in face:
        cv2.rectangle(video,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow("Rajinikanth",video)
    key=cv2.waitKey(1)
    if key== 27:
        break
