import pyrebase

config = {
  "apiKey": "AIzaSyDX-79Q7RsqKRqQC3dQQRTv60DRLW7pucA",
  "authDomain": "preprogramming62hotmail.firebaseapp.com",
  "databaseURL": "https://preprogramming62hotmail.firebaseio.com",
  "storageBucket": ""
}

firebase = pyrebase.initialize_app(config)

##################################################################

db = firebase.database()
data = {"name": "Mortimer 'Morty' Smith"}
db.child("users").child("Morty").set(data)

