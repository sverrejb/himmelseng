Template.verse.helpers({
    domain: function() {
        var array = Verses.find().fetch();
        var randomIndex = Math.floor( Math.random() * array.length );
        var element = array[randomIndex];
        return element;
    }
});