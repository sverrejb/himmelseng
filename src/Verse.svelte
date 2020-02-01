<script>
  export let verse = {text: "Placholder", title: "Foo"};
</script>

<style>
  div {
    box-shadow: 0 2px 1px -1px rgba(0, 0, 0, 0.2),
      0 1px 1px 0 rgba(0, 0, 0, 0.14), 0 1px 3px 0 rgba(0, 0, 0, 0.12);
    padding: 0.2rem 0.7rem;
    margin: 0.7rem 0;
    background-color: white;
    width: 20rem;
  }
</style>

<div>
  <h3>{verse.title}</h3>
  <pre>{verse.text}</pre>
</div>
