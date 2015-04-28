jar-of-django
==========================

A [cookiecutter](https://github.com/audreyr/cookiecutter) template for Django.

Description
-----------

Fork of [marcofucci/cookiecutter-simple-django](https://github.com/marcofucci/cookiecutter-simple-django).

Designed for Django 1.8+, Django Rest Framework 3.x, and Python 3.4

Built for SOA apps that use Django as their API backend. Future versions may include templates for a single page application, but I doubt it.

Heroku Setup
-----------
```bash
$ heroku create
$ git push heroku master
$ heroku config:add SECRET_KEY=CHANGME
$ heroku config:add ALLOWED_HOSTS=myapp.herokuapp.com
