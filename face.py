import cv2
face_cascade=cv2.CascadeClassifier(r"C:\Users\lenovo\OneDrive\Documents\haar-cascade-files\haarcascade_frontalface_default.xml")
img = cv2.imread(r"F:\Trip Alaparaigal\IMG_20230227_004903.jpg")

gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces=face_cascade.detectMultiScale(gray_img,1.1,4)
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,225),2)
cv2.imshow('Detected faces',img)
cv2.waitKey()
