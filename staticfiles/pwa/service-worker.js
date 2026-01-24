self.addEventListener("install", event => {
    event.waitUntil(
        caches.open("transport-v1").then(cache => {
            return cache.addAll([
                "/",
                "/driver/login/",
            ]);
        })
    );
});

self.addEventListener("fetch", event => {
    event.respondWith(
        fetch(event.request).catch(() => caches.match(event.request))
    );
});