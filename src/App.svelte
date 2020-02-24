<script>
  import { NotificationDisplay } from '@beyonk/svelte-notifications'
  import AllVerses from "./AllVerses.svelte";
  import VerseForm from "./VerseForm.svelte";
  import RandomVerse from "./RandomVerse.svelte";
  import Info from "./Info.svelte"
</script>

<style>
  header {
    grid-area: Header;
    margin-left: 1rem;
  }

  main {
    grid-area: Main;
  }

  @media (max-width: 750px) {
    main {
      margin-left: 1rem;
    }
}

</style>

<NotificationDisplay />
<header>
  <h1>Himmelseng</h1>
</header>
<Info/>
<main>
  <RandomVerse />
  <VerseForm />
</main>

<AllVerses />