import pyrebase

firebaseConfig = {
    "apiKey": "AIzaSyCyMFXHR-E7fvM60uvoiotlMUkd-YIx_WM",
    "authDomain": "python-project-cb18d.firebaseapp.com",
    "projectId": "python-project-cb18d",
    "storageBucket": "python-project-cb18d.appspot.com",
    "messagingSenderId": "196913902266",
    "appId": "1:196913902266:web:b30135e54f7ff03c1e8883",
    "databaseURL": "https://python-project-cb18d-default-rtdb.firebaseio.com/"
}
firebase = pyrebase.initialize_app(firebaseConfig)
database = firebase.database()
auth = firebase.auth()
storage = firebase.storage()

# update
# remove
