<script>
  import Verse from "./Verse.svelte";
  import verses from "./verses.json";
</script>

<style>
  section {
    grid-area: All-verses;
    overflow: scroll;
  }

  @media (max-width: 860px) {
    section {
        overflow: unset;
    }
}

</style>

<section>
  <h1>Alle vers</h1>
  {#each verses as verse}
    <Verse verse={verse} />
  {/each}
</section>
