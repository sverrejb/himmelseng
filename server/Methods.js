/**
 * Created by sverre on 08/09/16.
 */

function getEnvEmails() {
    var addresses = process.env.ADMIN_EMAILS;
    if (typeof(addresses) !== 'undefined') {
        return addresses.split(",");
    }
    log("No admin emails set in env variable ADMIN_EMAILS");
}

Meteor.methods({
    sendEmail: function (post) {
        this.unblock();
        Email.send({
            to: getEnvEmails(),
            from: "admin@himmelseng.no",
            subject: "Nytt himmelsengvers",
            text: "Det har blitt lagt inn et nytt vers på himmelseng.no \nTittel: " + post.title + "\nTekst: " + post.text
        });
    }
});
