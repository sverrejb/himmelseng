function makeFakeVerse() {
    text = '';
    for (var i = 0; i < 4; i++) {
        text = text += Fake.sentence(5) + '\n'
    }
    return text
}

if (Organizations.find().count() === 0) {
    var data = JSON.parse(Assets.getText("student_organizations.json"))['student_organizations'];
    data.forEach(function (item, index, array) {
        console.log("inserting" + item);
        Organizations.insert(item);
    })
}

/*if (Organizations.find().count() === 0){
    Organizations.insert({
        name:"Online",
        id:0
    });

    Organizations.insert({
        name:"Abakus",
        id:1
    })
}*/

if (Verses.find().count() === 0) {
    Verses.insert({
        title: "Marius Krakeli's vers",
        text: "Vi var en tur på eventyr \npå eventyr med styret. \nKrakels dansa gangnam-style, \nslo dama si i tryne."
    })
}


if (Verses.find().count() === 0) {
    for (var i = 0; i < 50; i++) {
        Verses.insert({
            title: 'Vers ' + i,
            text: makeFakeVerse()
        });
    }
}
