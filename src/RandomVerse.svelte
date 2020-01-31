<script>
  import Verse from "./Verse.svelte";
  import verses from "./verses-fixture.json";
  export const title = "foo";
  export let randomVerse = verses[Math.floor(Math.random() * verses.length)];
</script>

<style>
  section {
    grid-area: Random-Verse;
  }

</style>

<section>
  <h1>Tilfeldig vers</h1>
<Verse verse={randomVerse} />
<button>Nytt vers</button>
</section>
