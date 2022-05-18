import cv2
import os
import time

face_cascade=cv2.CascadeClassifier('src/haarcascade_frontalface_alt2.xml')

name=input("Enter your name: ")
path_unknown=("images")
path=os.path.join(path_unknown,name)
os.mkdir(path)
start_time=time.time()
cap=cv2.VideoCapture(0)
i=int(0)
a1=0
a2=1
ti=0



while(ti<40):
    ret,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.05,5)
    escape_time=time.time()-start_time
    ti= int(time.time() - start_time)
    print (ti)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        print(" <<<Saving>>>")
        if (a2<a1):
            a2=a2+1
            cv2.imwrite(os.path.join(path,str(ti)+'faces.jpg'), roi_gray)
        a1=ti

    cv2.imshow('video', frame)
    if cv2.waitKey(20) & 0xFF ==ord('q'):
        breakv


cap.release()
cv2.destroyAllWindows()
