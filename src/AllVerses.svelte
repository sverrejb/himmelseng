<script>
  import Verse from "./Verse.svelte";
  import verses from "./verses-fixture.json";
</script>

<style>
  section {
    grid-area: All-verses;
  }
</style>

<section>
  <h1>Alle vers</h1>
  {#each verses as verse}
    <Verse verse={verse} />
  {/each}
</section>
