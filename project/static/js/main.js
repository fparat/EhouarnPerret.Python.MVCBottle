$(function() {
    // Check and ask if needed desktop notification right
    DesktopNotification.checkRights();

    // Activate Bootstrap 4 tooltips and po(o)povers everRrrRryWhere!!!
    $('[data-toggle="tooltip"]').tooltip();
    $('[data-toggle="popover"]').popover();
});

// Module pattern + Loose augmentation (across files)
var DesktopNotification = (function () {

    var checkRights = function () {

        // Let's check if the browser supports notifications
        if (!("Notification" in window)) {
            console.log("This browser does not support desktop notification.");
        }
        // Let's check whether notification permissions have already been granted
        else if (Notification.permission === "granted") {
            console.log("Notifications have been granted access.");
        }
        // Otherwise, we need to ask the user for permission
        else if (Notification.permission !== "denied") {
            Notification.requestPermission(function (permission) {
            // If the user accepts, let's create a notification
            if (Notification.permission === "granted") {
                console.log("Notifications have now been granted access.");
            }
            });
        }
        else {
            console.log("Notifications are not allowed at this time.");
        }
    };

    var send = function(title, body, icon, sound, requiresInteraction) {
        var options = {
              body: body,
              icon: icon,
              badge: icon,
              requiresInteraction: requiresInteraction || true
        };

        var notification = new Notification(title, options);

        return notification;
    };

    return {
        checkRights: checkRights,
        send: send
  };

}(DesktopNotification || {}));

function sendDemo() {
    var title = 'Mister Pool Notification';
    var body = new Date().toISOString() + ': CRAP-NADA!!!';
    var icon = '/img/deadpool-dino.jpg';

    DesktopNotification.send(title, body, icon);
}
