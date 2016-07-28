Template.allVerses.helpers({
    verses: function() {
        console.log('called');

        return Verses.find()
    }
});
