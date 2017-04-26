"use strict";

var url = [];
var count = 0;

self.addEventListener('install', function(event) {
  event.waitUntil(self.skipWaiting()); //will install the service worker
});

self.addEventListener('activate', function(event) {
  event.waitUntil(self.clients.claim()); //will activate the serviceworker
});

// Register event listener for the 'notificationclick' event.
self.addEventListener('notificationclick', function(event) {
  event.notification.close();

  event.waitUntil(
    clients.matchAll({
      type: "window"
    })
    .then(function(clientList) {

      if (clients.openWindow) {
        var c = count;
        count++;
        return clients.openWindow(url[c]);
      }
    })
  );

});

