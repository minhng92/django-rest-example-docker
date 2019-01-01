# USAGE

```
$ git clone https://github.com/minhng92/django-rest-example-docker
$ cd django-rest-example-docker
$ docker-compose build
# create admin user, fill in the admin user's password
$ docker-compose run web bash -c "python manage.py makemigrations rest_example && python manage.py migrate && python manage.py createsuperuser --email admin@example.com --username admin"
$ docker-compose up

Go to http://localhost:8000 or http://localhost:8000/admin
Log in with admin user:
+ Username: admin
+ Password: <the password you filled in at the step creating admin user>
```

## Migrate DB and create super user (once time set up)
```
$ docker-compose run web bash -c "python manage.py makemigrations rest_example && python manage.py migrate && python manage.py createsuperuser --email admin@example.com --username admin"
Password: password123
Password (again): password123
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
```

## Migrate DB for rest_example module
```
$ docker-compose run web bash -c "python manage.py makemigrations rest_example && python manage.py migrate"
```

## Start server

```
$ docker-compose up
```

Start server in detached mode:

```
$ docker-compose up -d
```

## API location

* Go to `http://localhost:8000` to browse public RESTful APIs
* Django Admin: `http://localhost:8000/admin`

## References

+ [https://docs.docker.com/compose/django/](https://docs.docker.com/compose/django/)
+ [https://www.django-rest-framework.org/tutorial/quickstart/](https://www.django-rest-framework.org/tutorial/quickstart/)