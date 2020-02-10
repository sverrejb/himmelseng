<script>
    import { notifier } from "@beyonk/svelte-notifications";
    let form;
    
    async function handleSubmit(event) {
        const name = event.target.title.value;
        const verse = event.target.text.value;

        const response = await fetch("/.netlify/functions/submit-verse", {
            method: "POST",
            headers: {
                Accept: "application/json",
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ name: name, verse: verse })
        });
        console.log(response);
        form.reset();
        notifier.success('Takk! Ditt bidrag er mottatt.');
    }
</script>

<style>
    section {
        grid-area: Submit-Verse;
    }
    textarea {
        resize: none;
    }
</style>

<section>
    <h1>Send inn vers!</h1>
    <form bind:this={form} on:submit|preventDefault="{handleSubmit}">
        <div>
            <label for="title">Tittel:</label>
            <input type="text" placeholder="Valgfritt" name="title" id="title"/>
        </div>
        <div>
            <label for="text">Vers:</label>
            <textarea
                name="text"
                id="text"
                rows="4"
                placeholder="Tekst på fire linjer, takk! :)"
                required
            ></textarea>
        </div>
        <div>
            <input type="submit" value="Send inn!" />
        </div>
    </form>
</section>
