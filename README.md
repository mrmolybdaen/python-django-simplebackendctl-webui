# python-django-simplebackendctl-webui

This project aims to provide a simplified web based user interface to switch between maintenance and ready/up states
in HAProxy Open Source edition.
If You are using HAProxy Enterprise edition you already have a sufficient UI to control your proxy.

By default, the application uses the HAProxy backend to post specific states. This means it uses the stats site to manage states.
This way one does not have to publish an application which has to write into the HAProxy socket which can do a lot more
than the statistics backend.

The project also provides controls for Hetzner Cloud API routing and floating IP to manage which server should be attached.

## Install

### Requirements

See `requirements.txt`
In production you will need a WSGI service and a webserver such as Gunicor and Nginx.

- Django
- django[argon2,bcrypt]
- numpy
- argon2 >= 0.1
- bcrypt >= 4.2
- haproxyctl

#### Test

#### Build

### How to install

### Configuration

#### `src/haposctl_webui/haposctl_webui/settings.py`

1. Change `SECRET_KEY` to a save and secret value.
2. Change `DEBUG` to `False`
3. Change `LANGUAGE_CODE` according to your needs. Default is `'de-de'`
4. Change `TIME_ZONE` according to your needs. Default is `'Europe/Berlin'`
5. Change `ALLOWED_HOSTS` according to your needs. Default is `['*']`
6. Set up your database connections with `DATABASE`. By default, a SQLITE database is used.


## Contribute

Contributions are appreciated.

### Before you commit

We strongly advise to use `pre-commit` with our provided `.pre-commit-config.yaml` before you commit and push your
contribution.

This assures code style and some quality standards are met before you create some unclean states of your work.
However, since nobody can be trusted the same tools run in CI pipelines.

```shell
foo@bar:~$ pip install pre-commit
foo@bar:~$ pre-commit install
```

Pre commit hooks running `pylint`, `pytest` and `flake8` with `flake8-bandit` and `flake8-black`.

### Pipeline tests

Additionally, we use `atheris` to provide fuzzing and `pytest` for unit testing purposes.

We do not merge until everything is green.
