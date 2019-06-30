const firebase = require('firebase-functions');
const admin = require("firebase-admin");
const express  = require("express");
import config from "./config/config"
admin.initializeApp(config);

var db = admin.database();

exports.sendMail = firebase.https.onRequest((request, response) => {
    room = request.body.room; // room-A, room-B, room-C, room-D, room-E
    id = request.body.id;
    comment = request.body.comment;
    console.log(room, id, comment)
    
    var path = db.ref(room+"/"+id+"/mails");
    path.on('values', (data) => {
        var object = data.val();
        var newMail = Object.mails(object);
        newMail.push(comment)

        if (newMail) {
            firebase.database().ref(path).set({
                mail: newMail
            });
        }

    });

    // path.on('value', (snapshot) => {
    //     updateStarCount(postElement, snapshot.val());
    // });

    // firebase.database().ref(path).set({
    //     mail: []
    // });
});

