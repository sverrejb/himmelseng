Template.verseSubmit.events({
    'submit form': function(e) {
        e.preventDefault();

        var post = {
            title: $(e.target).find('[name=title]').val(),
            text: $(e.target).find('[name=text]').val()
        };

        post._id = Verses.insert(post);
        Materialize.toast('Takk for ditt bidrag!', 3000);
        Router.go('verse');
    }
});