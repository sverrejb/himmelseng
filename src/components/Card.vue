<template>
    <v-card class="card white--text" color="blue-grey darken-2">
        <v-card-title primary-title v-if="title">
            <h1 class="title">{{title}}</h1>
        </v-card-title>
        <v-card-text>
            <div v-for="line in splitVerse" :key="line">
                <span>{{line}}</span>
            </div>
        </v-card-text>
    </v-card>
</template>

<script>
  export default {
    name: "Card",
    props: {
      title: {
        type: String,
        default: '',
        required: false
      },
      verse: {
        type: String,
        default: '',
        required: false
      }
    },
    computed: {
      splitVerse() {
        return this.verse.split(/\r?\n/)
      }
    }
  }
</script>

<style scoped>
    .card {
        min-height: 6em;
        margin: 0.5em;
        min-width: 20em;
        max-width: 20em;
    }
    h1 {
        .padding-left: 1em;
        .padding-bottom: 0.0em;
    }

</style>