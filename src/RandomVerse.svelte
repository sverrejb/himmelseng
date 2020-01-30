<script>
  import Verse from "./Verse.svelte";
  import verses from "./verses-fixture.json";
  export const title = "foo";
  export const txt = verses[Math.floor(Math.random() * verses.length)].text;
</script>

<style>

</style>

<Verse rverse={txt} />
<button>Tilfeldig vers</button>
