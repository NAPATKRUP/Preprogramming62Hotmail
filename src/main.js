import Vue from 'vue'
import App from './App.vue'
import Bootstrap from 'bootstrap/dist/css/bootstrap.min.css'
import firebase from 'firebase'

Vue.config.productionTip = false

var firebaseConfig = {
  apiKey: "AIzaSyDX-79Q7RsqKRqQC3dQQRTv60DRLW7pucA",
  authDomain: "preprogramming62hotmail.firebaseapp.com",
  databaseURL: "https://preprogramming62hotmail.firebaseio.com",
  projectId: "preprogramming62hotmail",
  storageBucket: "",
  messagingSenderId: "368921862371",
  appId: "1:368921862371:web:d7976d8e35a2a5c5"
};
firebase.initializeApp(firebaseConfig);

new Vue({
  render: h => h(App),
  Bootstrap,
}).$mount('#app')
