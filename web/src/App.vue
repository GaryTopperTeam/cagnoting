<template lang="pug">
  main#app.h-100
    .d-flex.flex-column.justify-content-center.container-fluid.h-100
      .row.align-items-center.text-center
        .col
          ul.actions.nav.row.row-cols-1.row-cols-md-3.justify-content-center.my-3
            li.action.col.mb-3
              button.btn.btn-lg.btn-danger.rounded-pill.d-block.d-sm-inline-block.h-100.w-100.w-sm-auto(type="button" @click="increase")
                span.fs-2 en faiT
                br
                small.d-inline-block.lh-sm.mx-3.my-2 y'a pas de -e,
                  i  jamais
            li.action.col.mb-3
              button.btn.btn-lg.btn-warning.rounded-pill.d-block.d-sm-inline-block.h-100.w-100.w-sm-auto(type="button" @click="increase")
                span.fs-2 :'( con-ne
                br
                small.d-inline-block.lh-sm.mx-3.my-2 c'est pas gentil pour les vulves
            li.action.col.mb-3
              button.btn.btn-lg.btn-danger.rounded-pill.d-block.d-sm-inline-block.h-100.w-100.w-sm-auto(type="button" @click="increase")
                span.fs-2 unE espèce
                br
                small.d-inline-block.lh-sm.mx-3.my-2 un genre, une sorte
            li.action.col.mb-3
              button.btn.btn-lg.btn-danger.rounded-pill.d-block.d-sm-inline-block.h-100.w-100.w-sm-auto(type="button" @click="increase")
                // FIXME: FUCKING WHITESPACE NEEDED HERE ESLINT SUCKS PLEASE HELP
                span.fs-2 HUMAIN(s)
                br
                small.d-inline-block.lh-sm.mx-3.my-2 personne(s), gens...

          p.fs-lg.fw-bold.text-light.my-3
            | La cagnotte est de
            span.text-white  {{cagnotte}}
            |  moula

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
    increase () {
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
