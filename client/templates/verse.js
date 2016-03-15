Template.verse.helpers({
    randomVerse: function() {
        var array = Verses.find().fetch();
        return Random.choice(array).text
    }
});
