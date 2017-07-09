# Hola Stack

*Hola Stack* is a dockerized stack containing :
- a [PostgreSQL](https://www.postgresql.org/) database
- a backend REST service powered by a python [Flask](http://flask.pocoo.org/) app ([SQLAlchemy](http://flask-sqlalchemy.pocoo.org/), [Restless](https://flask-restless.readthedocs.io/)) and exposed using [Gunicorn](http://gunicorn.org/)
- a frontend volume for an [Angular](https://angular.io/) build
- and a [NGINX](https://nginx.org/) web server

## Requirements
This stack requires [docker-compose](https://docs.docker.com/compose/) 1.13 or higher.

## Usage

- download this repository
- write an `environment.properties` taking example on [`environment.properties.sample`](https://github.com/clemtoy/hola-stack/blob/master/environment.properties.sample)
- configure your model in [`backend/api.py`](https://github.com/clemtoy/hola-stack/blob/master/backend/api.py)
- in your Angular app, use the prefix `'/api/[...]'` to call the backend
- build your Angular app and copy the `dist/` content to [`frontend/`](https://github.com/clemtoy/hola-stack/tree/master/frontend)  
- run [`./reset.sh`](https://github.com/clemtoy/hola-stack/blob/master/reset.sh)
