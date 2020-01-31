<script>
  import { NotificationDisplay } from '@beyonk/svelte-notifications'
  import AllVerses from "./AllVerses.svelte";
  import VerseForm from "./VerseForm.svelte";
  import RandomVerse from "./RandomVerse.svelte";
</script>

<style>
  footer {
    grid-area: Footer;
    background-color: dimgrey;
    width: 100%;
  }
</style>

<NotificationDisplay />
<RandomVerse />
<VerseForm />
<AllVerses />
<footer>
  Footer her
</footer>