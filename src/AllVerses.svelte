<script>
  import Verse from "./Verse.svelte";
  import verses from "./verses.json";
</script>

<style>
  section {
    grid-area: All-verses;
    overflow: scroll;
    background-color: lightgray;
    width: 100%;
  }

  div {
    padding: 1rem;
  }

  @media (max-width: 950px) {
    section {
        overflow: unset;
    }
}

</style>

<section>
  <div>
    <h1>Alle vers</h1>
    {#each verses as verse}
      <Verse verse={verse} />
    {/each}
  </div>
</section>
