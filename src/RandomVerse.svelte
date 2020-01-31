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
  section {
    grid-area: Random-Verse;
  }

</style>

<section>
  <h1>Tilfeldig vers</h1>
<Verse bind:verse={randomVerse} />
<button on:click="{getRandomVerse}">Nytt vers!</button>
</section>
