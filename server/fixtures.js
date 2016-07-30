function makeFakeVerse() {
    text = '';
    for (var i = 0; i < 4; i++){
        text = text += Fake.sentence(5) + '\n'
    }
    return text
}

if (Verses.find().count() === 0) {
    for (var i = 0; i < 50; i++) {
        Verses.insert({
            title: 'Vers ' + i,
            text: makeFakeVerse()
        });
    }
}
