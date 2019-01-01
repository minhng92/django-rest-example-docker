# Migrate DB and create super user (once time set up)
```
$ docker-compose run web bash -c "python manage.py makemigrations rest_example && python manage.py migrate && python manage.py createsuperuser --email admin@example.com --username admin"
Password: password123
Password (again): password123
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
```

# Migrate DB for rest_example module
```
$ docker-compose run web bash -c "python manage.py makemigrations rest_example && python manage.py migrate"
```

# Start server

```
$ docker-compose up
```

Start server in detached mode:

```
$ docker-compose up -d
```

# API location

* Go to `http://localhost:8000` to browse public RESTful APIs
* Django Admin: `http://localhost:8000/admin`

# References
+ [https://docs.docker.com/compose/django/](https://docs.docker.com/compose/django/)