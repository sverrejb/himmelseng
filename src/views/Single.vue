<template>
  <v-container fluid>
    <v-slide-y-transition mode="out-in">
      <v-layout column align-center>
          <Card :title=title :verse=verse>
              {{verse}}
          </Card>
      </v-layout>
    </v-slide-y-transition>
  </v-container>
</template>

<script>
  import Card from '../components/Card.vue';

  export default {
      name: 'Single',
    components: {
        Card
    },
    data() {
        return {
          title: '',
          verse: "Jeg hoppet ut fra Bybrua, \njeg trodde det var whisky. \nMen akk og stakkars arme meg, \ndet var jo vann med fisk i.",
        }
    }

  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
