import '@babel/polyfill'
import Vue from 'vue'
import './plugins/vuetify'
import App from './App.vue'
import router from './router'
import axios from 'axios'

Vue.config.productionTip = false

const store = {
    defaults: {
    },
    verses: [
        {
            "title": "Homo",
            "text": "Jeg møtte på en homofil \nhan ville ta meg bakfra, \nmen jeg tok å lurte han, \njeg snudde meg og gapa!"
        },
        {
            "title": "",
            "text": "Jeg møtte på en lommemann, \nhan hadde no' i lomma. \nDet var ikke sukkertøy, \njeg klemte til, det skumma!"
        },
        {
            "title": "",
            "text": "Jeg sku' en tur på landsmøtet, \njeg skulle møte Terje, \nmen terje vakke oppdrive, \nhan pulte barn i sverige."
        },
        {
            "title": "",
            "text": "Jeg sku' en tur til østerrike, \ndet skulle ringt noen bjeller, \nfor Bjarne vakke å oppdrive, \nhan satt fast i en kjeller."
        },
        {
            "title": "",
            "text": "Jeg sku' en tur på Karl Johan, \njeg skulle kjøp meg hore. \nSexen den var kjempebra, \nmen hora hette tore."
        },
        {
            "title": "",
            "text": "Jeg ble nå med ei kjerring hjem, \nhun sa hun hadde mensen. \nDet burde ikke vært så galt, \nmen det flomma jo som Themsen!"
        },
        {
            "title": "",
            "text": "Jeg drakk min egen sæd i går \nog havna på klinikken. \nDoktor'n sa 'det va'kke bra' \nog amputerte pikken."
        },
        {
            "title": "",
            "text": "Jeg hoppet ut fra Bybrua, \njeg trodde det var whisky. \nMen akk og stakkars arme meg, \ndet var jo vann med fisk i."
        },
        {
            "title": "",
            "text": "En jægermann på linja gikk, \nså hørt'n toget ula. \nKonduktør'n av toget gikk \nog skrapt'n vekk fra hjula."
        },
        {
            "title": "",
            "text": "Jeg hadd' en onkel Theodor, \nhan har jeg ikke mere, \nfor han tok feil av H2O \nog H2SO4."
        },
        {
            "title": "",
            "text": "Jeg var så kåt, så kåt en kveld, \njeg putta den i kverna. \nDa jeg trakk den ut igjen \nvar hele hodet fjerna!"
        },
        {
            "title": "",
            "text": "Jeg satt på sal en fredagskveld, \njeg følte meg litt sliten. \nØvinga den ble for lang, \njeg kokte hele skiten!"
        }
    ]
};

axios.get(process.env.VUE_APP_API_PATH + "/api/verse")
    .then((response) => {
        console.log(response.data)
        store.verses = response.data;
    })
    .catch((e) => {
        console.error(e);
    });

export { store };

console.log(process.env.NODE_ENV)

new Vue({
  router,
  data: store,
  render: h => h(App)
}).$mount('#app')
