<template>
  <div class="col-12 mymailshow my-3" v-if="value[0] != 'Sample Mails'">
    <h5>{{ name }}</h5>
    <hr>
    <p>{{ mail }}</p>
  </div>
</template>

<script>
import Vue from 'vue'
import BootstrapVue from 'bootstrap-vue'

Vue.use(BootstrapVue)

export default {
  name: 'MailCard',
  props: ['maillist', 'room', 'id'],
  data () {
    return {
      value: null,
      name: "noname",
      mail: "nocomment"
    }
  },

  mounted () {
      this.value = this.maillist.split("-||-")
      this.name = this.value[0]
      this.mail = this.value[1]
  }
}
</script>

<style lang="scss" scoped>
.mymailshow {
  background: #D9ECF2;
  border: 5px solid black;
  border-radius: 20px;
  padding: 20px;
}
</style>