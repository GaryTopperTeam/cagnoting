<template lang="pug">
  main#app
    .core
      button.big-fuking-button(type="button" @click="faitT") faitT !!!!!
    .cagnotte La cagnotte est de {{cagnotte}} moula

</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
import server from './api/server.vue'

export default {
  name: 'App',
  components: {
    HelloWorld
  },
  data () {
    return {
      cagnotte: 0
    }
  },
  methods: {
    faitT () {
      server.addCagnoting(1).then((result) => {
        this.cagnotte += 1
      })
    }
  },
  mounted () {
    server.getCagnoting().then((result) => {
      this.cagnotte = result.sum
    })
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #ebedef;
  margin-top: 60px;
}
body {
  background: #282923;
  color: #ebedef;
}
.big-fuking-button {
  width: 25%;
  height: 20vh;
  margin: auto;
}
</style>
