<template>
  <div class="col-12 col-md-3 mycard">
    <div class="idcard">
      <h3 class="myname">พี่{{ showname }}</h3>
      <img class="w-100 my-1" :src="showimage">
      <b-button v-b-modal.modal-1 @click="openmail()" class="tomail my-1">Send Mail</b-button>
      <b-button v-b-modal.modal-2 @click="loginmail()" class="showmail m-1"><img src="../assets/find.png" width="30px" height="30px"/></b-button>

      <b-modal :id="modal-1" title="Send mail" :ref="select" @ok="pushmail">
        <p class="my-4">To พี่{{ showname }}</p>
        <div class="form-group shadow-textarea">
          <label>Form</label>
          <textarea class="form-control z-depth-1" rows="1" placeholder="Your name..." v-model="name"></textarea><br>
          <label>Comment</label>
          <textarea class="form-control z-depth-1" rows="3" placeholder="Write something here..." v-model="mail"></textarea>
        </div>
      </b-modal>

      <b-modal :id="modal-2" size="xl" title="Log in" :ref="showmailid" ok-only no-stacking @ok="clearpass">
        <h2 class="my-4">พี่{{ showname }}</h2>
        <div class="form-group shadow-textarea" v-if="this.getyourpass != this.correctpass">
          <label>Password</label>
          <textarea class="form-control z-depth-1" rows="1" placeholder="Your pass..." v-model="password"></textarea><br>
          <button @click="login">Login</button>
        </div>
        <div v-if="this.getyourpass == this.correctpass">
          <mail-card v-for="i in mymail" :maillist="i" :room="myclass" :id="select" v-bind:key="i"/>
        </div>
      </b-modal>
    </div>
  </div>
</template>

<script>
import { database } from 'firebase'
import Vue from 'vue'
import BootstrapVue from 'bootstrap-vue'
import MailCard from '@/components/MailCard'

Vue.use(BootstrapVue)

export default {
  name: 'DataCard',
  components: {
    MailCard,
  },
  props: ['select', 'myclass'],
  data () {
    return {
      value: null,
      showname: null,
      showimage: null,
      mymail: null,
      getyourpass: null,
      correctpass: null,
      showmailid: this.select + "mail",
      name: "",
      mail: "",
    }
  },

  mounted () {
    let self = this
    let data = database().ref(this.myclass + "/" + this.select)
    data.on('value', function(snapshot) {
        self.value = snapshot.val()
        self.showname = self.value.nickname
        self.showimage = self.value.image
        self.mymail = self.value.mails
    })

    let getpass = database().ref("password")
    getpass.on('value', function(snapshot) {
        self.correctpass = snapshot.val()
    })
  },

  methods: {
    openmail() {
      var self = this
      this.$refs[self.select].show()
    },
    pushmail() {
      if(this.name != "" && this.mail != "") {
        database().ref(this.myclass + "/" + this.select + "/mails").push(this.name + "-||-" + this.mail)
        alert("Mails has been send")
      }
      else {
        alert("Please check your name and comment to try again")
      }
      this.name = ""
      this.mail = ""
    },
    loginmail() {
      var self = this
      this.$refs[self.showmailid].show()
    },
    login() {
      this.getyourpass = this.password
      this.password = ""
    },
    clearpass() {
      this.getyourpass = ""
    }
  }
}
</script>

<style lang="scss" scoped>
.mycard {
  font-family: 'Pridi', serif;
  margin: 1em 0;
}
.idcard {
  padding: 10px;
  background: rgb(209, 209, 209);
  border: 5px solid black;
  border-radius: 5%;
}
.myname {
  color: black;
}
.tomail {
  font-family: 'Russo One', sans-serif;
  width: 100%;
  background: #F56A79;
  color: white;
  border: 2px solid black;
  border-radius: 5px;
}
.showmail {
  background: none;
  border: none;
}
.showmail:hover {
  opacity: 0.7;
}
</style>