<script>
    import { notifier } from "@beyonk/svelte-notifications";
    let form;
    let disabled = false;
    
    async function handleSubmit(event) {
        disabled = true;
        const title = event.target.title.value;
        const text = event.target.text.value;

        if (text.split('\n').filter(i => i.length > 0).length !== 4) {
            notifier.info('Tekst på fire linjer, takk! :)', 5000)
            disabled = false;
            return
        }

        const response = await fetch("/.netlify/functions/submit-verse", {
            method: "POST",
            headers: {
                Accept: "application/json",
                "Content-Type": "application/json"
            },
            body: JSON.stringify({title, text})
        });
        
        if (response.ok) {
            notifier.success('Takk! Ditt vers er mottatt.', 5000);
            form.reset();
        } else {
            notifier.danger('Noe gikk galt :(', 5000);
        }
        disabled = false;
    }
</script>

<style>

    h1 {
        margin-bottom: 0;
    }

    p {
        font-size: 0.8em;
    }
    input {
        width: 100%;
    }
    textarea {
        resize: none;
        width: 100%
    }
</style>

<section>
    <h1>Send inn vers!</h1>
    <p>Innsendte bidrag blir kvalitetssjekket før publisering.</p>
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
            <input type="submit" value="Send inn!" disabled={disabled} />
        </div>
    </form>
</section>
