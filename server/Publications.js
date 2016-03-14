Meteor.publish('verses', function() {
    return Verses.find();
});
