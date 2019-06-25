<template>
  <div id="app">
    <div class="container">
      <!-- Home -->
      <br><br><br>
      <div v-if="page == 0">
        <h1 class="titlepage">Preprogramming62 | Hotmail</h1>
        <br>
        <div class="row m-3">
          <button @click="change(1)" class="btn btn-secondary btn-lg col-12 col-md-4 p-5 m-2"><h1>Room A</h1></button>
          <button @click="change(2)" class="btn btn-success btn-lg col-12 col-md-4 p-5 m-2"><h1>Room B</h1></button>
          <button @click="change(3)" class="btn btn-danger btn-lg col-12 col-md-4 p-5 m-2"><h1>Room C</h1></button>
          <button @click="change(4)" class="btn btn-warning btn-lg col-12 col-md-4 p-5 m-2"><h1>Room D</h1></button>
          <button @click="change(5)" class="btn btn-info btn-lg col-12 col-md-4 p-5 m-2"><h1>Room E</h1></button>
        </div>
      </div>
      <!-- Room A -->
      <div v-if="page == 1">
        <h1 class="titlepage myrooma">Room A</h1><br><br>
        <h3>TD | Teaching Director</h3><br>
        <div class="row m-3">
          <data-card v-for="i in user_td_a" :select="i" v-bind:key="i"/>
        </div><br>
        <h3>TA | Teaching Assistant</h3><br>
        <div class="row m-3">
          <data-card v-for="i in user_ta_a" :select="i" v-bind:key="i"/>
        </div>
      </div>

      <!-- Room B -->
      <div v-if="page == 2">
        <h1 class="titlepage myroomb">Room B</h1><br><br>
        <h3>TD | Teaching Director</h3><br>
        <div class="row m-3">
          <data-card v-for="i in user_td_b" :select="i" v-bind:key="i"/>
        </div><br>
        <h3>TA | Teaching Assistant</h3><br>
        <div class="row m-3">
          <data-card v-for="i in user_ta_b" :select="i" v-bind:key="i"/>
        </div>
      </div>

      <!-- Room C -->
      <div v-if="page == 3">
        <h1 class="titlepage myroomc">Room C</h1><br>
        <h3>TD | Teaching Director</h3><br>
        <div class="row m-3">
          <data-card v-for="i in user_td_c" :select="i" v-bind:key="i"/>
        </div><br>
        <h3>TA | Teaching Assistant</h3><br>
        <div class="row m-3">
          <data-card v-for="i in user_ta_c" :select="i" v-bind:key="i"/>
        </div>
      </div>

      <!-- Room D -->
      <div v-if="page == 4">
        <h1 class="titlepage myroomd">Room D</h1><br>
        <h3>TD | Teaching Director</h3><br>
        <div class="row m-3">
          <data-card v-for="i in user_td_d" :select="i" v-bind:key="i"/>
        </div><br>
        <h3>TA | Teaching Assistant</h3><br>
        <div class="row m-3">
          <data-card v-for="i in user_ta_d" :select="i" v-bind:key="i"/>
        </div>
      </div>

      <!-- Room E -->
      <div v-if="page == 5">
        <h1 class="titlepage myroome">Room E</h1><br>
        <h3>TD | Teaching Director</h3><br>
        <div class="row m-3">
          <data-card v-for="i in user_td_e" :select="i" v-bind:key="i"/>
        </div><br>
        <h3>TA | Teaching Assistant</h3><br>
        <div class="row m-3">
          <data-card v-for="i in user_ta_e" :select="i" v-bind:key="i"/>
        </div>
      </div>

      <!-- button home and up -->
      <div v-if="page != 0">
        <button class="gohome" @click="page = 0"><img src="./assets/home.png" width="60px" height="60px"/></button>
      </div>
      <br><br><br>
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
        self.user_td_a = self.value.classroom.rooma.td.split(' ')
        self.user_ta_a = self.value.classroom.rooma.ta.split(' ')

        self.user_td_b = self.value.classroom.roomb.td.split(' ')
        self.user_ta_b = self.value.classroom.roomb.ta.split(' ')

        self.user_td_c = self.value.classroom.roomc.td.split(' ')
        self.user_ta_c = self.value.classroom.roomc.ta.split(' ')

        self.user_td_d = self.value.classroom.roomd.td.split(' ')
        self.user_ta_d = self.value.classroom.roomd.ta.split(' ')

        self.user_td_e = self.value.classroom.roome.td.split(' ')
        self.user_ta_e = self.value.classroom.roome.ta.split(' ')
    })
  }
}
</script>

<style lang="scss">
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  background: white;
  background-size: cover;
  margin: 0;
  min-height: 100vh;
}
.myrooma {
  background:#6c757d;
  color: white;
}
.myroomb {
  background:#28a745;
  color: white;
}
.myroomc {
  background:#dc3545;
  color: white;
}
.myroomd {
  background:#ffc107;
  color: white;
}
.myroome {
  background:#17a2b8;
  color: white;
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
