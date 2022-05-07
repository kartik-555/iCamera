import cv2
import os
import time
import pickle
import firebase_admin
from firebase_admin import credentials,storage
from firebase_admin import firestore

cred = credentials.Certificate("key.json")
firebase_admin.initialize_app(cred,{'storageBucket':'icamera-4d0e0.appspot.com'})


bucket = storage.bucket()


start_time=time.time()



face_cascade=cv2.CascadeClassifier('src/haarcascade_frontalface_alt2.xml')
recognizer=cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainner.yml")
labels={}

with open("labels.pickle", 'rb') as f:
    og_labels=pickle.load(f)
    labels={v:k for k,v in og_labels.items()}

cap=cv2.VideoCapture(0)


while(True):
    ret,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.05,5)
    ct=int(time.time()-start_time)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]

        id_, conf=recognizer.predict(roi_gray)
        if conf<60:# and conf<=85:
            # print(id_)
            # print (labels[id_])
            font=cv2.FONT_HERSHEY_SIMPLEX
            name=labels[id_]
            color=(255,255,255)
            stoke=2
            cv2.putText(frame,name,(x,y),font,1,color,stoke,cv2.LINE_AA)
            cv2.putText(frame,str(conf),(x+5,y+h-5),font,1,(255,255,0),1)
        else:
            # print("[INFO] Object found. Saving locally.  ")
            font = cv2.FONT_HERSHEY_SIMPLEX
            name = "UNKNOWN"
            color = (255, 255, 255)
            stoke = 2
            cv2.putText(frame, name, (x, y), font, 1, color, stoke, cv2.LINE_AA)
            path_unknown='detectedface'
            cv2.imwrite(os.path.join(path_unknown,'faces.jpg'), frame)
            # blob = bucket.blob('faces.jpg')
            # blob.upload_from_filename('detectedface/faces.jpg')
            # db = firestore.client()
            # data = {blob.public_url : time.time()}
            # db.collection('links').add(data)



    cv2.imshow('video',frame)
    if cv2.waitKey(20) & 0xFF ==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
