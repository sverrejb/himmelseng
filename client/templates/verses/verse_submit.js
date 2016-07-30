Template.verseSubmit.events({
    'submit .new-verse': function(event) {
        event.preventDefault();
        
        const target = event.target;
        const post = {
            title: target.title.value,
            text: target.text.value
        };

        const lineBreakCount = (post.text.match(/\n/g) || []).length;
        if (lineBreakCount !== 3) {
            Materialize.toast('husk fire linjer! ', 4000)
        }
        else {
            post._id = Verses.insert(post);
            target.title.value = '';
            target.text.value = '';
            Materialize.toast('Takk for ditt bidrag!', 3000);
        }
        
    }
});