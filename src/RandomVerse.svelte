<script>
  import Verse from "./Verse.svelte";
  import verses from "./verses-fixture.json";
  export const title = "foo";
  export let randomVerse = verses[Math.floor(Math.random() * verses.length)];
</script>

<style>

</style>

<Verse verse={randomVerse} />
<button>Tilfeldig vers</button>
