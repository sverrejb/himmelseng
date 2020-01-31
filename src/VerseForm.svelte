<script>
  async function handleSubmit(event) {
    const name = event.target.name.value;
    const verse = event.target.verse.value;

    const response = await fetch("/.netlify/functions/submit-verse", {
      method: "POST",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ name: name, verse: verse })
    });
    console.log(response);
  }
</script>

<style>
  form {
    grid-area: Submit-Verse;
  }
</style>

<form on:submit|preventDefault={handleSubmit}>
  <h1>Send inn vers!</h1>
  <div>
    <label for="name">Name:</label>
    <input type="text" name="name" id="name" required />
  </div>
  <div>
    <label for="verse">Verse:</label>
    <input type="text" name="verse" id="verse" required />
  </div>
  <div>
    <input type="submit" value="Submit!" />
  </div>
</form>