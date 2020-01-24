<script>
  import Verse from "./Verse.svelte";
  import VerseForm from './VerseForm.svelte';
  import verses from "./verses-fixture.json";
  export const title = "foo";
  export const txt = verses[Math.floor(Math.random() * verses.length)].text;
</script>

<style>
  main {
    text-align: center;
    padding: 1em;
    max-width: 90vw;
    margin: 0 auto;
  }

  h1 {
    color: darkgray;
    text-transform: uppercase;
    font-size: 4em;
    font-weight: 100;
  }

  @media (min-width: 640px) {
    main {
      max-width: none;
    }
  }
</style>

<main>
  <h1>Himmelseng</h1>
  <Verse rverse={txt} />
  <VerseForm/>
</main>
