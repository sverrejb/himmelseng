<script>
  import AllVerses from "./AllVerses.svelte";
  import VerseForm from "./VerseForm.svelte";
  import RandomVerse from "./RandomVerse.svelte";
</script>

<style>
  footer {
    grid-area: Footer;
    background-color: dimgrey;
  }
</style>


<RandomVerse />
<VerseForm />
<AllVerses />
<footer>
  Footer her
</footer>