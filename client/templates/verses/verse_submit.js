Template.verseSubmit.events({
    'submit .new-verse': function(event) {
        event.preventDefault();

        const target = event.target;
        const post = {
            title: target.title.value,
            text: target.text.value,
            freetextMetadata: target.metadata.value,
            studorg: target.studorg.value
        };

        const lineBreakCount = (post.text.match(/\n/g) || []).length;
        if (lineBreakCount !== 3) {
            Materialize.toast('husk fire linjer! ', 4000)
        }
        else {
            post._id = Verses.insert(post);
            target.title.value = '';
            target.text.value = '';
            target.metadata.value = '';
            Materialize.toast('Takk for ditt bidrag!', 3000);
        }

    }
});

Template.verseSubmit.helpers({
    getLinjeforeninger: function() {
        $('select').material_select();
        console.log(Organizations.find().fetch());
        return Organizations.find().fetch().to_array();
    }
});

Template.verseSubmit.onRendered(function() {
    $('select').material_select();
});
