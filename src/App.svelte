<script>
  import AllVerses from "./AllVerses.svelte";
  import VerseForm from "./VerseForm.svelte";
  import RandomVerse from "./RandomVerse.svelte";
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

<header>
  <h1>Himmelseng</h1>
</header>

<main>
  <RandomVerse />
  <VerseForm />
  <AllVerses />
</main>

<footer>
Made with Svelte. Hosted on Netlify.
</footer>