<template>
  <v-container fluid>
    <v-slide-y-transition mode="out-in">
      <v-layout column align-center>
        <div v-for="verse in store.verses" :key="verse.text">
          <Card :title=verse.title :verse=verse.text>
            {{verse}}
          </Card>
        </div>
      </v-layout>
    </v-slide-y-transition>
  </v-container>
</template>

<script>
  import { store } from '../main';
  import Card from '../components/Card.vue';

  export default {
    name: 'All',
    components: {
      Card
    },
    data() {
      return {
        store,
      }
    }

  }
</script>