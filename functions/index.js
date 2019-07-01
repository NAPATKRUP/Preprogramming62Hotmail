const functions = require('firebase-functions');
const firebase = require("firebase-admin");

firebaseConfig = {
    apiKey: "AIzaSyDX-79Q7RsqKRqQC3dQQRTv60DRLW7pucA",
    authDomain: "preprogramming62hotmail.firebaseapp.com",
    databaseURL: "https://preprogramming62hotmail.firebaseio.com",
    projectId: "preprogramming62hotmail",
    storageBucket: "",
    messagingSenderId: "368921862371",
    appId: "1:368921862371:web:d7976d8e35a2a5c5"
};

firebase.initializeApp(firebaseConfig);
var database = firebase.database();

// Create and Deploy Your First Cloud Functions
// https://firebase.google.com/docs/functions/write-firebase-functions

exports.helloWorld = functions.https.onRequest((request, response) => {
    response.send("Hello from Firebase!");
});

exports.sendMail = functions.https.onRequest((request, response) => {
    room = request.body.room; // room-A, room-B, room-C, room-D, room-E
    id = request.body.id;
    comment = request.body.comment;
    payload = {
        "room": room,
        "id": id,
        "comment": comment
    };
    var path = database.ref(room+"/"+id+"/mails");
    var setPath = database.ref(room+"/"+id);
    try {
        if (payload) {
            path.on("value", (snapshot) => {
                var mailArray = snapshot.val();
                mailArray.push(comment);
                path.update(mailArray)
            }, (errorObject) => {
                console.log("The read failed: " + errorObject.code);
            });
        }
    } catch (e) {
        response.send(e)
    }

});

exports.getMail = functions.https.onRequest((request, response) => {
    room = request.body.room;
    id = request.body.id;
    var path = database.ref(room+"/"+id+"/mails");

    try {
        path.on("value", (snapshot) => {
            response.send(snapshot.val())
        })
    } catch (e) {
        response.send(e);
    }
});
