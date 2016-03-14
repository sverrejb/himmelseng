Template.verse.helpers({
    random_verse: function() {
        var array = Verses.find().fetch();
        return Random.choice(array).text
    }
});