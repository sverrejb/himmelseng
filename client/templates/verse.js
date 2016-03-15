function setRandomVerse () {
    Meteor.call("randomVerse", function (err, verseId) {
        //TODO: handle error

        Session.set("randomVerseId", verseId);
    });
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

setRandomVerseInSession = function(){
    var array = Verses.find().fetch();
    var randomId = Random.choice(array)._id;
    Session.set('currentVerse', randomId);
};

Template.verse.onCreated(function () {
    // Kjøres igjen hver gang en "reaktiv" kilde endrer seg,
    // altså en funksjon som returnerer en verdi som kan endre seg
    // i dette tilfellet er Session.get en reaktiv funksjon
    setRandomVerseInSession();
    //this.autorun(function () {
    //    var verseId = Session.get("randomVerseId");

        // Meteor vil holde det nåværende verset oppdatert
    //    Meteor.subscribe("verse", verseId);
    //});


});
