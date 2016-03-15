if (Verses.find().count() === 0) {
    for (var i = 0; i < 200; i++) {
        Verses.insert({
            title: 'Verse ' + i,
            text: Fake.paragraph(4)
        });
    }
}
