""" Import Data To Firebase Using pyrebase4 """

import pyrebase
import json
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

config = {
    "apiKey": "AIzaSyDX-79Q7RsqKRqQC3dQQRTv60DRLW7pucA",
    "authDomain": "preprogramming62hotmail.firebaseapp.com",
    "databaseURL": "https://preprogramming62hotmail.firebaseio.com",
    "storageBucket": ""
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

##################################################################

df = pd.read_excel('name_list.xlsx', sheet_name='Sheet1')
roomList = df['Room']
staff_id_list = df['ID']
name = df['Name']
stateList = df['State']
imgLink = df['Image']


for i in range(len(name)):

    room = "room-"+roomList[i]
    staff_id = int(staff_id_list[i])
    nickname = name[i]
    state = stateList[i]
    img = imgLink[i]
    payload = {
        "nickname": nickname,
        "state": state,
        "image": img,
        "mails": [0]
    }
    if payload:
         db.child(room).child(staff_id).set(payload)
         print(json.dumps(payload, indent=4), room, staff_id, i,)
    else:
        print("ERROR at", i)

