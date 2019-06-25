<template>
  <div class="col-12 col-md-3 mycard">
    <h3 class="m-2">{{ value.name }}</h3>
    <img class="w-100 my-1" :src="value.image">
    <b-button v-b-modal.modal-1 @click="opencomment()" class="tocomment my-1">Comment</b-button>
    <button class="showcomment m-1"><img src="../assets/find.png" width="30px" height="30px"/></button>

    <b-modal :id="modal-1" title="Send comment" :ref="select" @ok="pushcomment">
      <p class="my-4">To {{ value.name }}</p>
      <div class="form-group shadow-textarea">
        <label>From</label>
        <textarea class="form-control z-depth-1" rows="1" placeholder="Your name..." v-model="name"> </textarea><br>
        <label>Comment</label>
        <textarea class="form-control z-depth-1" rows="3" placeholder="Write something here..." v-model="comment"></textarea>
      </div>
    </b-modal>
  </div>
</template>

<script>
import { database } from 'firebase'
import Vue from 'vue'
import BootstrapVue from 'bootstrap-vue'

Vue.use(BootstrapVue)

export default {
  name: 'DataCard',
  props: ['select'],
  data () {
    return {
      value: null,
      statuscomment: 0,
      name: "",
      comment: "",
    }
  },

  mounted () {
    let data = database().ref(this.select)
    let self = this
    data.on('value', function(snapshot) {
        self.value = snapshot.val()
    })
  },
  methods: {
    opencomment() {
      var self = this
      this.$refs[self.select].show()
    },
    pushcomment() {
      console.log(this.name, this.comment)
      database().ref(this.value.comment).update([this.name, this.comment])
    },
  }
}
</script>

<style lang="scss" scoped>
.mycard {
    display: inline;
    background: rgb(209, 209, 209);
    width: 50%;
    border: 5px solid black;
    border-radius: 5%;
    margin: 3px;
    padding: 5px;
}
.tocomment {
  width: 100%;
  background: black;
  color: white;
  border: 2px solid black;
  border-radius: 5px;
}
.showcomment {
  background: none;
  border: none;
}
.showcomment:hover {
  opacity: 0.7;
}
</style>