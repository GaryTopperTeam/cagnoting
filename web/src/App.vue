<template lang="pug">
  main#app.h-100
    .d-flex.flex-column.justify-content-center.container-fluid.h-100
      .row.align-items-center.text-center
        .col
          button.btn.btn-primary.big-fuking-button(type="button" @click="faitT") faitT !!!!!
          p La cagnotte est de {{cagnotte}} moula

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
        console.log(result)
        this.cagnotte += 1
      })
    }
  },
  mounted () {
    server.getCagnoting().then((result) => {
      this.cagnotte = result.sum
      console.log(result)
    })
  }
}
</script>

<style lang="scss">
  /* No CSS here, just global import please =) */
  @import './assets/stylesheets/main.scss';
</style>
