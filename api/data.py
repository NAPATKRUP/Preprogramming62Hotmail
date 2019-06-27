""" Import Data To Firebase Using pyrebase4 """

import pyrebase

config = {
    "apiKey": "AIzaSyDX-79Q7RsqKRqQC3dQQRTv60DRLW7pucA",
    "authDomain": "preprogramming62hotmail.firebaseapp.com",
    "databaseURL": "https://preprogramming62hotmail.firebaseio.com",
    "storageBucket": ""
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

##################################################################


room = ["room-a", "room-b", "roomb-c", "room-c", "room-d", "room-e"]

for current_room in room:
    staff_id = place_holder
    payload = {
        "nickname": "nickname",
        "state": "TD",
        "mails": []
    }
    if payload:
        db.child(current_room).child(staff_id).set(payload)




# data = {"name": "Mortimer 'Morty' Smith"}
# db.child("users").child("Morty").set(data)

