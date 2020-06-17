
var CACHE_NAME = 'Remesas-cache-v1';
var urlsToCache = [
    '/',
    '/static/mdbootstrap/css/bootstrap.min.css',
    '/static/mdbootstrap/css/mdb.min.css',
    '/static/mdbootstrap/css/style.css',
    '/static/mdbootstrap/css/compiled-4.16.0.min.css',
    '/static/templates/js/sweetalert2.js',
    '/static/templates/js/funciones.js',
    '/static/mdbootstrap/img/logo.png'
];

self.addEventListener('install', function(event) {
  // Perform install steps
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(function(cache) {
        //console.log('Opened cache');
        return cache.addAll(urlsToCache);
      })
  );
});

self.addEventListener('fetch', function(event) {
    event.respondWith(
        caches.match(event.request).then(function(response) {

          return fetch(event.request)
          .catch(function(rsp) {
             return response; 
          });
          
          
        })
    );
});
