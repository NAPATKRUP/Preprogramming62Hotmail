<template>
  <div id="app">
    <div class="container">
      <!-- Home -->
      <br><br><br>
      <div v-if="page == 0">
        <h1 class="mytitle">Prepro62 Hotmail</h1>
        <br>
        <div class="row m-3 justify-content-center">
          <button @click="change(1)" class="btn btn-warning btn-lg col-12 col-md-4 p-5 m-2"><h1>Room A</h1></button>
          <button @click="change(2)" class="btn btn-warning btn-lg col-12 col-md-4 p-5 m-2"><h1>Room B</h1></button>
          <button @click="change(3)" class="btn btn-warning btn-lg col-12 col-md-4 p-5 m-2"><h1>Room C</h1></button>
          <button @click="change(4)" class="btn btn-warning btn-lg col-12 col-md-4 p-5 m-2"><h1>Room D</h1></button>
          <button @click="change(5)" class="btn btn-warning btn-lg col-12 col-md-4 p-5 m-2"><h1>Room E</h1></button>
          <button @click="change(6)" class="btn btn-warning btn-lg col-12 col-md-4 p-5 m-2"><h1>Head/Staff</h1></button>
        </div>
      </div>

      <!-- Room A -->
      <div v-if="page == 1">
        <h1 class="myroom">Room A</h1><br><br>
        <h3>TD | Teaching Director</h3><br>
        <div class="row m-3">
          <data-card v-for="i in user_td_a" :select="i" myclass="roomA" v-bind:key="i"/>
        </div><br>
        <h3>TA | Teaching Assistant</h3><br>
        <div class="row m-3">
          <data-card v-for="i in user_ta_a" :select="i" myclass="roomA" v-bind:key="i"/>
        </div>
      </div>

      <!-- Room B -->
      <div v-if="page == 2">
        <h1 class="myroom">Room B</h1><br><br>
        <h3>TD | Teaching Director</h3><br>
        <div class="row m-3">
          <data-card v-for="i in user_td_b" :select="i" myclass="roomB" v-bind:key="i"/>
        </div><br>
        <h3>TA | Teaching Assistant</h3><br>
        <div class="row m-3">
          <data-card v-for="i in user_ta_b" :select="i" myclass="roomB" v-bind:key="i"/>
        </div>
      </div>

      <!-- Room C -->
      <div v-if="page == 3">
        <h1 class="myroom">Room C</h1><br>
        <h3>TD | Teaching Director</h3><br>
        <div class="row m-3">
          <data-card v-for="i in user_td_c" :select="i" myclass="roomC" v-bind:key="i"/>
        </div><br>
        <h3>TA | Teaching Assistant</h3><br>
        <div class="row m-3">
          <data-card v-for="i in user_ta_c" :select="i" myclass="roomC" v-bind:key="i"/>
        </div>
      </div>

      <!-- Room D -->
      <div v-if="page == 4">
        <h1 class="myroom">Room D</h1><br>
        <h3>TD | Teaching Director</h3><br>
        <div class="row m-3">
          <data-card v-for="i in user_td_d" :select="i" myclass="roomD" v-bind:key="i"/>
        </div><br>
        <h3>TA | Teaching Assistant</h3><br>
        <div class="row m-3">
          <data-card v-for="i in user_ta_d" :select="i" myclass="roomD" v-bind:key="i"/>
        </div>
      </div>

      <!-- Room E -->
      <div v-if="page == 5">
        <h1 class="myroom">Room E</h1><br>
        <h3>TD | Teaching Director</h3><br>
        <div class="row m-3">
          <data-card v-for="i in user_td_e" :select="i" myclass="roomE" v-bind:key="i"/>
        </div><br>
        <h3>TA | Teaching Assistant</h3><br>
        <div class="row m-3">
          <data-card v-for="i in user_ta_e" :select="i" myclass="roomE" v-bind:key="i"/>
        </div>
      </div>

      <!-- Head -->
      <div v-if="page == 6">
        <h1 class="myroom">Head/staff</h1><br>
        <h3>Head</h3><br>
        <div class="row m-3">
          <data-card v-for="i in user_head" :select="i" myclass="head_staff" v-bind:key="i"/>
        </div>
        <h3>Staff</h3><br>
        <div class="row m-3">
          <data-card v-for="i in user_staff" :select="i" myclass="head_staff" v-bind:key="i"/>
        </div>
      </div>

      <!-- button home and up -->
      <div v-if="page != 0">
        <button class="gohome" @click="page = 0"><img src="./assets/home.png" width="60px" height="60px"/></button>
      </div>
      <br><br>
    </div>
  </div>
</template>

<script>
import { database } from 'firebase'
import DataCard from '@/components/DataCard'
export default {
  name: 'app',
  components: {
    DataCard,
  },
  methods: {
    change (n) {
      this.page = n
    }
  },
  data() {
    return {
      page: 0,
      user_td_a: null,
      user_ta_a: null,
      user_td_b: null,
      user_ta_b: null,
      user_td_c: null,
      user_ta_c: null,
      user_td_d: null,
      user_ta_d: null,
      user_td_e: null,
      user_ta_e: null,
      user_head: null,
      user_staff: null
    }
  },
  mounted () {
    let self = this

    // A
    let td_a = database().ref("roomA/td")
    let ta_a = database().ref("roomA/ta")
    td_a.on('value', function(snapshot) {
        self.user_td_a = snapshot.val().split(' ')
    })
    ta_a.on('value', function(snapshot) {
        self.user_ta_a = snapshot.val().split(' ')
    })

    // B
    let td_b = database().ref("roomB/td")
    let ta_b = database().ref("roomB/ta")
    td_b.on('value', function(snapshot) {
        self.user_td_b = snapshot.val().split(' ')
    })
    ta_b.on('value', function(snapshot) {
        self.user_ta_b = snapshot.val().split(' ')
    })

    // C
    let td_c = database().ref("roomC/td")
    let ta_c = database().ref("roomC/ta")
    td_c.on('value', function(snapshot) {
        self.user_td_c = snapshot.val().split(' ')
    })
    ta_c.on('value', function(snapshot) {
        self.user_ta_c = snapshot.val().split(' ')
    })

    // D
    let td_d = database().ref("roomD/td")
    let ta_d = database().ref("roomD/ta")
    td_d.on('value', function(snapshot) {
        self.user_td_d = snapshot.val().split(' ')
    })
    ta_d.on('value', function(snapshot) {
        self.user_ta_d = snapshot.val().split(' ')
    })

    // E
    let td_e = database().ref("roomE/td")
    let ta_e = database().ref("roomE/ta")
    td_e.on('value', function(snapshot) {
        self.user_td_e = snapshot.val().split(' ')
    })
    ta_e.on('value', function(snapshot) {
        self.user_ta_e = snapshot.val().split(' ')
    })

    // Head
    let head_id = database().ref("head_staff/id_head")
    head_id.on('value', function(snapshot) {
        self.user_head = snapshot.val().split(' ')
    })

    // Staff
    let staff_id = database().ref("head_staff/id_staff")
    staff_id.on('value', function(snapshot) {
        self.user_staff = snapshot.val().split(' ')
    })
  }
}
</script>

<style lang="scss">
h1, h3 {
  color: white;
}
#app {
  font-family: 'Russo One', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  background: #002D40;
  background-size: cover;
  margin: 0;
  min-height: 100vh;
}
.mytitle {
  font-size: 50px;
}
.myroom{
  background:#D9ECF2;
  color: black;
}
.gohome {
  position: fixed;
  bottom: 5%;
  right: 2%;
  background: none;
  border: none;
}
.gohome:hover {
  opacity: 0.7;
}
</style>
