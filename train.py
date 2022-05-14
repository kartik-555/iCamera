import os
import cv2
from PIL import Image
import numpy as np
import pickle

base_dir=os.path.dirname(os.path.abspath(__file__))
image_dir=os.path.join(base_dir,"images")

face_cascade=cv2.CascadeClassifier('src/haarcascade_frontalface_alt2.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()


current_id=0
label_ids={}
y_labels=[]
x_labels=[]

for root,dirs,files in os.walk(image_dir):
    for file in files:
        if file.endswith("png") or file.endswith("jpg"):
            path=os.path.join(root,file)
            label=os.path.basename(root).replace(" ","-").lower()
            # print(label,path)
            if  not label in label_ids:
                label_ids[label]=current_id
                current_id+=1
            id_=label_ids[label]

            pil_image=Image.open(path).convert("L")
            image_array=np.array(pil_image,"uint8")
            # print(image_array)
            faces=face_cascade.detectMultiScale(image_array,1.05,10)

            for (x,y,w,h) in faces:
                roi=image_array[y:y+h,x:x+w]
                x_labels.append(roi)
                y_labels.append(id_)


print(y_labels)
print(x_labels)

with open("labels.pickle",'wb') as f:
     pickle.dump(label_ids,f)

recognizer.train(x_labels,np.array(y_labels))
recognizer.save("trainner.yml")

