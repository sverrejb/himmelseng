# Himmelseng 🌌🛏
Jeg ønsker meg en himmelseng ...

Himmelseng er en sang som synges i godt lag av studentene i Trondheim. Opphavet til sangen er ukjent, men den ser opprinnelig ut til å komme fra Danmark.
Sangen har et start- og et sluttvers, og innimellom der kommer vers av forskjellig art. Disse følger som regel et mønster med fire linjer, der andre og fjerde linje rimer.
Himmelseng.no ble laget i et forsøk på å samle og bevare de mange versene som finnest i studentmiljøet i Trondheim, samt være til hjelp når sangen synges.

## Get started

Install the dependencies...

```bash
npm install
```

... Start [Rollup](https://rollupjs.org):

```bash
npm run dev
```

Navigate to [localhost:5000](http://localhost:5000). You should see your app running. 

By default, the server will only respond to requests from localhost. To allow connections from other computers, edit the `sirv` commands in package.json to include the option `--host 0.0.0.0`.


## Building and running in production mode

To create an optimised version of the app:

```bash
npm run build
```

You can run the newly built app with `npm run start`. This uses [sirv](https://github.com/lukeed/sirv), which is included in your package.json's `dependencies` so that the app will work when you deploy to platforms like [Heroku](https://heroku.com).


## Single-page app mode

By default, sirv will only respond to requests that match files in `public`. This is to maximise compatibility with static fileservers, allowing you to deploy your app anywhere.

If you're building a single-page app (SPA) with multiple routes, sirv needs to be able to respond to requests for *any* path. You can make it so by editing the `"start"` command in package.json:

```js
"start": "sirv public --single"
```