import cv2
face_case= cv2.CascadeClassifier(r"C:\Users\lenovo\OneDrive\Documents\haar-cascade-files\haarcascade_frontalface_default.xml")
v_cap = cv2.VideoCapture(0)
while True:
    _,img= v_cap.read()
    gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_case.detectMultiScale(gray_img,1.1,4)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,225,0),2)
    cv2.imshow('Detected Faces',img)
    p=cv2.waitKey(20)
    if p==10:
        break
v_cap.release()    
