<script>
  import Verse from "./Verse.svelte";
  import verses from "./verses.json";
  export let randomVerse;
  const getRandomVerse = () => {
    randomVerse = verses[Math.floor(Math.random() * verses.length)]
  }
  getRandomVerse();
</script>

<style>

  h1 {
    margin-top: 0;
  }

  button {
    width: 100%;
  }

  section {
    min-width: 100%
  }
</style>

<section>
  <h1>Tilfeldig vers</h1>
  <Verse verse={randomVerse} />
  <button on:click="{getRandomVerse}">Nytt vers!</button>
</section>
