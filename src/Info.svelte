<script>
  import Verse from "./Verse.svelte";

  const firstVerse = {title: 'Første vers',
  text: `Jeg ønsker meg en himmelseng
en himmelseng med speil i
så jeg kan ligge og speile meg
og se hvor jeg er deilig.`}

  const refrain = {title: 'Refreng',
  text: `Hey lå li lå li lå
li lå li lå li låa,
hey lå li lå li lå
li lå li lå li låa!
Ompa ompa ompa sprut,
ompa ompa sprut sprut!`
}
  const lastVerse = {title: 'Siste vers',
  text: `Jeg trenger ingen himmelseng,
en himmelseng med speil i.
Jeg trenger ikke speile meg,
jeg vet hvor jeg er deilig.`}

</script>

<style>
    aside {
        margin-left: 1rem;
    }
    @media (min-width: 950px) {
        h2 {display: none;}
}
</style>

<aside>
    <h2>
        Om himmelseng
    </h2>
    <p>Himmelseng er en sang som synges i godt lag av studentene i Trondheim. Opphavet til sangen er ukjent, men den ser opprinnelig ut til å komme fra Danmark. Sangen har et start- og et sluttvers, og innimellom der kommer vers av forskjellig art. Disse følger som regel et mønster med fire linjer, der andre og fjerde linje rimer. Himmelseng.no ble laget i et forsøk på å samle og bevare de mange versene som finnest i studentmiljøet i Trondheim, samt være til hjelp når sangen synges.</p>
    <Verse verse={firstVerse}/>
    <Verse verse={refrain}/>
    <Verse verse={lastVerse}/>

</aside>