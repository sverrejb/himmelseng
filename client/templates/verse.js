Template.verse.helpers({
    randomVerse: function() {
        var array = Verses.find().fetch();
        var verse = Random.choice(array)
        return  verse.title +": "+  verse.text
    }
});

Template.verse.events({
    'click #refresh_button': function(e){ alert('hello!'); }
});
