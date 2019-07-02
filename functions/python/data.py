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

ta_a = ""
ta_b = ""
ta_c = ""
ta_d = ""
ta_e = ""
ta_f = ""

td_a = ""
td_b = ""
td_c = ""
td_d = ""
td_e = ""
td_f = ""

for i in range(len(name)):

    room = "room"+roomList[i]
    staff_id = int(staff_id_list[i])
    nickname = name[i]
    state = stateList[i].lower()
    img = imgLink[i]
    payload = {
        "nickname": nickname,
        "state": state,
        "image": img,
        "mails": ["Sample Mails"]
    }

    if state == "ta":
        if room == "roomA": ta_a += str(staff_id)+" "
        if room == "roomB": ta_b += str(staff_id)+" "
        if room == "roomC": ta_c += str(staff_id)+" "
        if room == "roomD": ta_d += str(staff_id)+" "
        if room == "roomE": ta_e += str(staff_id)+" "
    elif state == "td":
        if room == "roomA": td_a += str(staff_id)+" "
        if room == "roomB": td_b += str(staff_id)+" "
        if room == "roomC": td_c += str(staff_id)+" "
        if room == "roomD": td_d += str(staff_id)+" "
        if room == "roomE": td_e += str(staff_id)+" "


    if payload:
        db.child(room).child(staff_id).set(payload)
        print(json.dumps(payload, indent=4), room, staff_id, i,)
    else:
        print("ERROR at", i)

db.child("roomA").child("ta").set(ta_a.rstrip(" "))
db.child("roomB").child("ta").set(ta_b.rstrip(" "))
db.child("roomC").child("ta").set(ta_c.rstrip(" "))
db.child("roomD").child("ta").set(ta_d.rstrip(" "))
db.child("roomE").child("ta").set(ta_e.rstrip(" "))

db.child("roomA").child("td").set(td_a.rstrip(" "))
db.child("roomB").child("td").set(td_b.rstrip(" "))
db.child("roomC").child("td").set(td_c.rstrip(" "))
db.child("roomD").child("td").set(td_d.rstrip(" "))
db.child("roomE").child("td").set(td_e.rstrip(" "))
