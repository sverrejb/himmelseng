function setRandomVerseInSession(){
    var array = Verses.find().fetch();
    var randomId = Random.choice(array)._id;
    Session.set('currentVerse', randomId);
}

Template.verse.helpers({
    randomVerse: function() {
        return Verses.findOne(Session.get("currentVerse"));
    }
});

Template.verse.events({
    'click #refresh_button': function(e){
        setRandomVerseInSession();
    }
});

Template.verse.onCreated(function () {
    setRandomVerseInSession();
});
