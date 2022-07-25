# HTTP server/client

## curl

try:

- `curl https://api.publicapis.org/entries`
- `curl "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m,relativehumidity_2m,windspeed_10m"`

(2)

## http.server

### Iterations
- Implement basic http server and test it with curl
- for `self.path` equal to `/` send current directory's entry list (files, dirs, etc)
- for `self.path` equal to `/some_file.txt` respond with `some_file.txt`'s contents, or `404 not found`
- clean up your code

### Guide

1- Read the docs!

[docs](https://docs.python.org/3/library/http.server.html)

2- Search!

(12)

