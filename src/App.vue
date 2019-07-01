<template>
  <div id="app">
    <div class="container">
      <!-- Home -->
      <br><br><br>
      <div v-if="page == 0">
        <h1 class="mytitle">Prepro62 Hotmail</h1>
        <br>
        <div class="row m-3">
          <button @click="change(1)" class="btn btn-warning btn-lg col-12 col-md-4 p-5 m-2"><h1>Room A</h1></button>
          <button @click="change(2)" class="btn btn-warning btn-lg col-12 col-md-4 p-5 m-2"><h1>Room B</h1></button>
          <button @click="change(3)" class="btn btn-warning btn-lg col-12 col-md-4 p-5 m-2"><h1>Room C</h1></button>
          <button @click="change(4)" class="btn btn-warning btn-lg col-12 col-md-4 p-5 m-2"><h1>Room D</h1></button>
          <button @click="change(5)" class="btn btn-warning btn-lg col-12 col-md-4 p-5 m-2"><h1>Room E</h1></button>
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
      value: null,
      user_td_a: null,
      user_ta_a: null,
      user_td_b: null,
      user_ta_b: null,
      user_td_c: null,
      user_ta_c: null,
      user_td_d: null,
      user_ta_d: null,
      user_td_e: null,
      user_ta_e: null
    }
  },
  mounted () {
    let data = database().ref(this.select)
    let self = this
    data.on('value', function(snapshot) {
        self.value = snapshot.val()
        self.user_td_a = self.value.roomA.td.split(' ')
        self.user_ta_a = self.value.roomA.ta.split(' ')

        self.user_td_b = self.value.roomB.td.split(' ')
        self.user_ta_b = self.value.roomB.ta.split(' ')

        self.user_td_c = self.value.roomC.td.split(' ')
        self.user_ta_c = self.value.roomC.ta.split(' ')

        self.user_td_d = self.value.roomD.td.split(' ')
        self.user_ta_d = self.value.roomD.ta.split(' ')

        self.user_td_e = self.value.roomE.td.split(' ')
        self.user_ta_e = self.value.roomE.ta.split(' ')
    })
  }
}
</script>

<style lang="scss">
* {
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
