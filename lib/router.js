Router.configure({
    layoutTemplate: 'layout',
    loadingTemplate: 'loading',
    waitOn: function() { return Meteor.subscribe('verses'); }
});

Router.route('/', {name: 'verse'});
