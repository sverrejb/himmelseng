Meteor.publish('verses', function() {
    return Verses.find();
});

Meteor.publish('organizations', function() {
    return Organizations.find();
});
