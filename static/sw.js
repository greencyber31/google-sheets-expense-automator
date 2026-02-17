const CACHE_NAME = 'expenses-tracker-v28';
const ASSETS = [
    '/',
    '/static/manifest.json',
    '/static/icon.svg',
    '/sw.js'
];

self.addEventListener('install', (event) => {
    self.skipWaiting(); // Force new service worker to take over
    event.waitUntil(
        caches.open(CACHE_NAME).then((cache) => {
            return cache.addAll(ASSETS);
        })
    );
});

self.addEventListener('activate', (event) => {
    event.waitUntil(clients.claim()); // Take control of all pages immediately
});

self.addEventListener('fetch', (event) => {
    event.respondWith(
        caches.match(event.request).then((response) => {
            return response || fetch(event.request);
        })
    );
});
