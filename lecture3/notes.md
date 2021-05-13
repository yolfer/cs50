# Lecture 3 Notes

think about the web in terms of request and response

## request

GET / HTTP/1.1
Host: www.example.com

## response

HTTP/1.1 200 OK # could be 301, 403, 404, 500, etc
Content-Type: text/html

## new django project

`django-admin startproject PROJECT_NAME`

## start webserver

python3 manage.py runserver

a django project may have 1 or more apps in it
to create django app:
`python3 manage.py startapp hello`
then add to `INSTALLED_APPS` in `settings.py`

## About this django project

Django project called lecture3, inside is a master `urls.py` file with two projects
`admin` (default) and `hello`.
Inside `urls.py` for `hello` app, there's a view 'index' and 'joe',
plus a parameterized path 'greet' that takes a name

## Django Middleware CSRF

in `settings.py`, see `CsrfViewMiddleware`

## Sessions

remembers who you are and stores data specific to you (tasks, in this case)
be sure to run `python manage.py migrate`
