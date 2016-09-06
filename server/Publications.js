Meteor.publish('verses', function() {
    return Verses.find();
});

Meteor.publish('student_organizations', function() {
    return Organizations.find();
});
