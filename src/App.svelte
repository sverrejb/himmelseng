<script>
	import Verse from './Verse.svelte';
	import verses from './verses-fixture.json';
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
	<form method="post" action="/.netlify/functions/submit">
        <div>
            <label for="name">Name: </label>
            <input type="text" name="name" id="name" required>
        </div>
        <div>
            <label for="verse">Verse: </label>
            <input type="text" name="verse" id="verse" required>
        </div>
        <div>
            <input type="submit" value="Submit!">
        </div>
    </form>
</main>