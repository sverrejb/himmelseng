<script>
  import { NotificationDisplay } from '@beyonk/svelte-notifications'
  import AllVerses from "./AllVerses.svelte";
  import VerseForm from "./VerseForm.svelte";
  import RandomVerse from "./RandomVerse.svelte";
  import Info from "./Info.svelte"
</script>

<style>
  main {
    margin-top: 4rem;
    grid-area: Main;
  }
</style>

<NotificationDisplay />
<Info/>
<main>
  <RandomVerse />
    <VerseForm />
</main>

<AllVerses />