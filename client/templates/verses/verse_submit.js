Template.verseSubmit.events({
    'submit .new-verse': function(event) {
        event.preventDefault();
        
        const target = event.target;
        
        const post = {
            title: target.title.value,
            text: target.text.value
        };

        post._id = Verses.insert(post);
        target.title.value = '';
        target.text.value = '';
        Materialize.toast('Takk for ditt bidrag!', 3000);
        
    }
});