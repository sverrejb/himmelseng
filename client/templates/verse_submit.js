Template.verseSubmit.events({
    'submit form': function(e) {
        e.preventDefault();

        var post = {
            title: 'foo',
            text: $(e.target).find('[name=text]').val()
        };

        post._id = Verses.insert(post);
        Router.go('verse');
    }
});