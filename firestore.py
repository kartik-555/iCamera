import time
import firebase_admin
from firebase_admin import credentials,storage
from firebase_admin import firestore


cred = credentials.Certificate("key.json")
firebase_admin.initialize_app(cred,{'storageBucket':'icamera-4d0e0.appspot.com'})


bucket = storage.bucket()
blob = bucket.blob('faces.jpg')
blob.upload_from_filename('detectedface/faces.jpg')
print(blob.public_url)


db=firestore.client()
data={'blob.public_url' : time.time()}
db.collection('links').add(data)
