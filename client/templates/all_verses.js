Template.verse.helpers({
    derp: function() {
        console.log('called')
        return Verses.find()
    }
});
