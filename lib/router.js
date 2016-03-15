Router.configure({
    layoutTemplate: 'layout',
    loadingTemplate: 'loading',
    notFoundTemplate: 'notFound',
    waitOn: function() { return Meteor.subscribe('verses'); }
});

Router.route('/', {name: 'verse'});
Router.route('/alle', {name: 'allVerses'});
Router.route('/submit', {name: 'verseSubmit'});
