<script>
  import Verse from "./Verse.svelte";
  import verses from "./verses-fixture.json";
</script>

<style>
section {
    background-color: cadetblue;
}

</style>

<section>
  {#each verses as verse}
    <Verse verse={verse} />
  {/each}
</section>
